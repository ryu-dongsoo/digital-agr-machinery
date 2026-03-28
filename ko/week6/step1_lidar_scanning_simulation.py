"""
Step 1: 트랙터 LiDAR 스캐닝 시뮬레이션
========================================
과수원 통로를 주행하는 트랙터에 장착된 LiDAR가
레이저 빔을 발사하여 3D Point Cloud를 실시간으로 구축하는 과정을 애니메이션으로 보여줌.

학습 목표:
  - LiDAR의 ToF(Time-of-Flight) 원리를 직관적으로 체험
  - Point Cloud가 '점 하나하나가 레이저 한 발의 반사점'임을 시각적으로 이해
  - 트랙터 이동에 따라 3D 지도가 점진적으로 완성되는 SLAM 개념 체득
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import os

# ============================================================
# 1. 가상 과수원 환경 생성
# ============================================================
def create_orchard_environment():
    """
    규칙적으로 심어진 과수원(5열 x 4행, 총 20그루)과
    평탄한 지면 데이터를 생성하는 함수.
    각 나무는 원뿔(Cone) 형태의 수관 + 원기둥 줄기로 구성.
    """
    all_pts = []
    tree_centers = []
    
    # 나무 배치: 5열 x 4행, 간격 4m x 5m
    for row in range(4):
        for col in range(5):
            cx = col * 4.0 + 2.0   # X 중심
            cy = row * 5.0 + 2.5   # Y 중심
            
            # 나무마다 약간의 높이/폭 변이 (실제처럼)
            tree_h = np.random.uniform(3.5, 5.5)
            canopy_r = np.random.uniform(1.2, 2.0)
            
            tree_centers.append((cx, cy, tree_h, canopy_r))
            
            # 줄기 (원기둥, 높이 0~1.5m)
            n_trunk = 200
            trunk_h = np.random.uniform(0, 1.5, n_trunk)
            trunk_angle = np.random.uniform(0, 2*np.pi, n_trunk)
            trunk_r = 0.15
            trunk_x = cx + trunk_r * np.cos(trunk_angle)
            trunk_y = cy + trunk_r * np.sin(trunk_angle)
            all_pts.append(np.column_stack((trunk_x, trunk_y, trunk_h)))
            
            # 수관 (원뿔, 높이 1.5m ~ tree_h)
            n_canopy = 800
            canopy_z = np.random.uniform(1.5, tree_h, n_canopy)
            # 높이가 올라갈수록 반지름이 줄어드는 원뿔 구조
            frac = (canopy_z - 1.5) / (tree_h - 1.5)
            local_r = canopy_r * (1.0 - frac * 0.8)  # 꼭대기에서 20%까지 좁아짐
            canopy_angle = np.random.uniform(0, 2*np.pi, n_canopy)
            canopy_x = cx + local_r * np.cos(canopy_angle) + np.random.normal(0, 0.05, n_canopy)
            canopy_y = cy + local_r * np.sin(canopy_angle) + np.random.normal(0, 0.05, n_canopy)
            all_pts.append(np.column_stack((canopy_x, canopy_y, canopy_z)))
    
    # 지면 (평탄한 바닥면, Z ≈ 0)
    n_ground = 3000
    gx = np.random.uniform(-1, 22, n_ground)
    gy = np.random.uniform(-1, 22, n_ground)
    gz = np.random.normal(0, 0.05, n_ground)
    all_pts.append(np.column_stack((gx, gy, gz)))
    
    world_pts = np.vstack(all_pts)
    return world_pts, tree_centers


# ============================================================
# 2. LiDAR 스캐닝 시뮬레이션 (트랙터 이동 + 빔 발사)
# ============================================================
def simulate_lidar_scan(world_pts, tractor_pos, scan_range=8.0, fov_deg=270):
    """
    트랙터의 현재 위치에서 LiDAR가 주변을 스캔할 때
    감지 범위(scan_range) 내에 있는 점들만 반환하는 함수.
    실제 LiDAR는 레이저 펄스의 ToF로 거리를 측정하지만,
    본 시뮬레이션에서는 유클리드 거리로 간이 시뮬레이션.
    """
    tx, ty = tractor_pos
    dx = world_pts[:, 0] - tx
    dy = world_pts[:, 1] - ty
    dist = np.sqrt(dx**2 + dy**2)
    
    # 스캔 범위 내의 점만 선택
    mask = dist < scan_range
    scanned = world_pts[mask]
    
    return scanned


# ============================================================
# 3. 애니메이션 실행
# ============================================================
def run_animation():
    print("🚜 트랙터 LiDAR 스캐닝 시뮬레이션을 시작합니다...")
    print("   과수원 통로를 주행하며 3D Point Cloud가 실시간으로 구축되는 과정을 관찰하세요.")
    
    # 과수원 월드 데이터 생성
    world_pts, tree_centers = create_orchard_environment()
    
    # 트랙터 경로 설정: 과수원 통로(Y방향)를 따라 직진
    # 1열-2열 사이 통로 → 유턴 → 3열-4열 사이 통로 복귀
    path_y_fwd = np.linspace(-1, 22, 30)   # 전진
    path_y_rev = np.linspace(22, -1, 30)   # 복귀
    
    # 경로 1: X=10 (2열-3열 사이) 전진
    path1_x = np.full_like(path_y_fwd, 10.0)
    path1 = np.column_stack((path1_x, path_y_fwd))
    
    # 경로 2: X=6 (1열-2열 사이) 복귀
    path2_x = np.full_like(path_y_rev, 6.0)
    path2 = np.column_stack((path2_x, path_y_rev))
    
    tractor_path = np.vstack((path1, path2))
    n_frames = len(tractor_path)
    
    # 누적 Point Cloud 저장
    accumulated_pts = np.empty((0, 3))
    
    # Figure 설정
    fig = plt.figure(figsize=(14, 6))
    
    # 좌측: 2D 탑뷰 (트랙터 위치 + 스캔 범위)
    ax1 = fig.add_subplot(121)
    ax1.set_xlim(-2, 24)
    ax1.set_ylim(-2, 24)
    ax1.set_aspect('equal')
    ax1.set_title("Top View: Tractor Path & LiDAR Scan")
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Y (m)")
    ax1.set_facecolor('#2a2a2a')
    
    # 나무 위치 표시 (고정)
    for cx, cy, th, cr in tree_centers:
        tree_circle = plt.Circle((cx, cy), cr, color='green', alpha=0.3)
        ax1.add_patch(tree_circle)
        ax1.plot(cx, cy, 'g^', markersize=4)
    
    # 트랙터 경로 표시 (고정)
    ax1.plot(tractor_path[:, 0], tractor_path[:, 1], '--', color='gray', alpha=0.3, linewidth=1)
    
    # 동적 요소
    tractor_dot, = ax1.plot([], [], 'rs', markersize=10, label='Tractor')
    scan_circle = plt.Circle((0, 0), 8.0, color='yellow', fill=False, linewidth=1.5, linestyle='--', alpha=0.6)
    ax1.add_patch(scan_circle)
    scan_pts_2d, = ax1.plot([], [], '.', color='cyan', markersize=0.5, alpha=0.3)
    ax1.legend(loc='upper right', fontsize=8)
    
    # 우측: 3D 누적 Point Cloud
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_xlim(-2, 24)
    ax2.set_ylim(-2, 24)
    ax2.set_zlim(-1, 7)
    ax2.set_title("Accumulated 3D Point Cloud")
    ax2.set_xlabel("X (m)")
    ax2.set_ylabel("Y (m)")
    ax2.set_zlabel("Z (Height, m)")
    ax2.view_init(elev=25, azim=-60)
    
    # 프레임 카운터 텍스트
    info_text = ax1.text(0.02, 0.98, '', transform=ax1.transAxes, 
                         fontsize=9, verticalalignment='top', color='white',
                         bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
    
    def update(frame):
        nonlocal accumulated_pts
        
        tx, ty = tractor_path[frame]
        
        # LiDAR 스캔 실행
        scanned = simulate_lidar_scan(world_pts, (tx, ty), scan_range=8.0)
        
        # 누적 (성능을 위해 랜덤 다운샘플링)
        if len(scanned) > 500:
            idx = np.random.choice(len(scanned), 500, replace=False)
            scanned = scanned[idx]
        accumulated_pts = np.vstack((accumulated_pts, scanned))
        
        # === 2D 탑뷰 업데이트 ===
        tractor_dot.set_data([tx], [ty])
        scan_circle.center = (tx, ty)
        scan_pts_2d.set_data(accumulated_pts[:, 0], accumulated_pts[:, 1])
        
        # === 3D 뷰 업데이트 ===
        ax2.cla()
        ax2.set_xlim(-2, 24)
        ax2.set_ylim(-2, 24)
        ax2.set_zlim(-1, 7)
        ax2.set_xlabel("X (m)")
        ax2.set_ylabel("Y (m)")
        ax2.set_zlabel("Z (m)")
        
        # Height Ramp 컬러맵
        z = accumulated_pts[:, 2]
        z_norm = (z - z.min()) / (z.max() - z.min() + 1e-6)
        
        # 포인트가 너무 많으면 샘플링
        show_step = max(1, len(accumulated_pts) // 15000)
        ax2.scatter(accumulated_pts[::show_step, 0], 
                    accumulated_pts[::show_step, 1], 
                    accumulated_pts[::show_step, 2], 
                    c=z_norm[::show_step], cmap='jet', s=0.5, alpha=0.6)
        
        # 트랙터 현재 위치 3D 표시
        ax2.scatter([tx], [ty], [0], c='red', s=80, marker='s', edgecolors='white', zorder=10)
        
        ax2.set_title(f"Accumulated 3D Point Cloud ({len(accumulated_pts):,} pts)")
        ax2.view_init(elev=25, azim=-60 + frame * 0.5)
        
        # 정보 텍스트 업데이트
        info_text.set_text(
            f"Frame: {frame+1}/{n_frames}\n"
            f"Tractor: ({tx:.1f}, {ty:.1f})m\n"
            f"Total Points: {len(accumulated_pts):,}"
        )
        
        return tractor_dot, scan_circle, scan_pts_2d, info_text
    
    ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=120, blit=False, repeat=False)
    
    plt.tight_layout()
    
    # 결과 이미지 저장 (최종 프레임)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step1_result.png")
    
    # 최종 프레임까지 모두 실행 후 저장을 위해 콜백 등록
    def on_finish(event=None):
        fig.savefig(save_path, dpi=200, bbox_inches='tight')
        print(f"✅ LiDAR 스캐닝 시뮬레이션 최종 결과가 저장되었습니다: {save_path}")
    
    # 애니메이션 종료 후 또는 창 닫을 때 저장
    fig.canvas.mpl_connect('close_event', on_finish)
    
    print("   (창을 닫으면 최종 결과 이미지가 자동 저장됩니다)")
    plt.show()
    
    # 누적 Point Cloud를 NPY로 저장 (Step 2에서 재사용)
    npy_path = os.path.join(base_dir, "scanned_orchard.npy")
    np.save(npy_path, accumulated_pts)
    print(f"✅ 누적 Point Cloud 저장 완료: {npy_path} ({len(accumulated_pts):,} points)")
    
    return accumulated_pts

if __name__ == "__main__":
    run_animation()
