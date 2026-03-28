"""
Step 2: 3D 작물 표현형(Phenotyping) 자동 측정
==============================================
Step 1에서 트랙터 LiDAR로 수집한 과수원 Point Cloud를 분석하여
각 나무의 수고(Tree Height), 수관 폭(Canopy Width)을 자동 추출하고,
빨간 바운딩 박스로 표시하는 실습.

학습 목표:
  - 3D Point Cloud에서 개별 객체를 분리(Segmentation)하는 원리 이해
  - 바운딩 박스(AABB)를 이용한 작물 치수 자동 산출 체험
  - 수작업 측정을 자동화하는 디지털 농업의 효율성 체감
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os

# ============================================================
# 1. 포인트 클라우드에서 개별 나무 자동 탐지 (Grid-based Segmentation)
# ============================================================
def detect_trees(pts, grid_size=3.0, min_height=1.5, min_pts=50):
    """
    Point Cloud를 격자(Grid)로 나누고,
    각 격자 내에서 Z가 높은(min_height 이상) 포인트 군집이 있으면
    '나무가 있다'고 판단하는 간이 세그멘테이션 함수.
    
    실제 연구에서는 DBSCAN, PointNet 등 고급 알고리즘을 사용.
    """
    trees = []
    
    x_min, x_max = pts[:, 0].min(), pts[:, 0].max()
    y_min, y_max = pts[:, 1].min(), pts[:, 1].max()
    
    # 격자 단위로 순회
    x_bins = np.arange(x_min, x_max, grid_size)
    y_bins = np.arange(y_min, y_max, grid_size)
    
    for x_start in x_bins:
        for y_start in y_bins:
            # 격자 내부 포인트 선택
            mask = (
                (pts[:, 0] >= x_start) & (pts[:, 0] < x_start + grid_size) &
                (pts[:, 1] >= y_start) & (pts[:, 1] < y_start + grid_size) &
                (pts[:, 2] > min_height)  # 지면 필터링
            )
            cell_pts = pts[mask]
            
            if len(cell_pts) >= min_pts:
                # 바운딩 박스 산출
                bb_min = np.min(cell_pts, axis=0)
                bb_max = np.max(cell_pts, axis=0)
                
                # 지면 레벨 보정 (해당 격자 전체 점의 Z 최소값)
                all_mask = (
                    (pts[:, 0] >= x_start) & (pts[:, 0] < x_start + grid_size) &
                    (pts[:, 1] >= y_start) & (pts[:, 1] < y_start + grid_size)
                )
                ground_z = np.percentile(pts[all_mask][:, 2], 5)  # 하위 5% → 지면 추정
                
                tree_height = bb_max[2] - ground_z
                canopy_w_x = bb_max[0] - bb_min[0]
                canopy_w_y = bb_max[1] - bb_min[1]
                canopy_spread = max(canopy_w_x, canopy_w_y)
                
                center_x = (bb_min[0] + bb_max[0]) / 2
                center_y = (bb_min[1] + bb_max[1]) / 2
                
                trees.append({
                    'id': len(trees) + 1,
                    'center': (center_x, center_y),
                    'height': tree_height,
                    'spread': canopy_spread,
                    'bb_min': np.array([bb_min[0], bb_min[1], ground_z]),
                    'bb_max': bb_max,
                    'pts': cell_pts
                })
    
    return trees

# ============================================================
# 2. 3D 바운딩 박스 그리기 유틸리티
# ============================================================
def draw_bbox_3d(ax, bb_min, bb_max, color='red', alpha=0.15):
    """3D 축에 와이어프레임 바운딩 박스를 그리는 헬퍼 함수"""
    x0, y0, z0 = bb_min
    x1, y1, z1 = bb_max
    
    # 8개 꼭짓점
    corners = np.array([
        [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
        [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]
    ])
    
    # 12개 모서리 연결
    edges = [
        [0,1], [1,2], [2,3], [3,0],  # 바닥
        [4,5], [5,6], [6,7], [7,4],  # 지붕
        [0,4], [1,5], [2,6], [3,7]   # 기둥
    ]
    for e in edges:
        ax.plot3D(*zip(corners[e[0]], corners[e[1]]), color=color, linewidth=1.5, alpha=0.8)
    
    # 반투명 면 (선택적)
    faces = [
        [corners[0], corners[1], corners[5], corners[4]],
        [corners[2], corners[3], corners[7], corners[6]],
        [corners[0], corners[3], corners[7], corners[4]],
        [corners[1], corners[2], corners[6], corners[5]],
        [corners[0], corners[1], corners[2], corners[3]],
        [corners[4], corners[5], corners[6], corners[7]]
    ]
    face_col = Poly3DCollection(faces, alpha=alpha, facecolor=color, edgecolor=color)
    ax.add_collection3d(face_col)


# ============================================================
# 3. 메인 시각화 및 측정
# ============================================================
def run_measurement():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    npy_path = os.path.join(base_dir, "scanned_orchard.npy")
    save_path = os.path.join(base_dir, "step2_result.png")
    
    # Step 1에서 생성된 누적 Point Cloud 로드
    if not os.path.exists(npy_path):
        # Step 1을 먼저 실행하지 않은 경우 → 자체 생성
        print("⚠️ Step 1의 스캔 데이터가 없어서, 자체적으로 과수원 데이터를 생성합니다.")
        print("   (더 나은 결과를 위해 step1_lidar_scanning_simulation.py를 먼저 실행하세요!)")
        from step1_lidar_scanning_simulation import create_orchard_environment
        pts, _ = create_orchard_environment()
    else:
        pts = np.load(npy_path)
    
    print(f"📊 로드 완료. 총 포인트 수: {len(pts):,}")
    
    # 나무 자동 탐지
    print("🌳 개별 나무 자동 탐지(Grid Segmentation) 중...")
    trees = detect_trees(pts)
    print(f"   → {len(trees)}그루 탐지 완료!")
    
    # 측정 결과 출력
    print("\n" + "=" * 60)
    print(f"🌳 3D Phenotyping 자동 측정 결과 (총 {len(trees)}그루)")
    print("=" * 60)
    print(f"{'No.':<5} {'중심좌표 (X,Y)':<18} {'수고(m)':<10} {'수관폭(m)':<10}")
    print("-" * 50)
    for t in trees:
        cx, cy = t['center']
        print(f"  {t['id']:<3}  ({cx:5.1f}, {cy:5.1f})     {t['height']:5.2f}     {t['spread']:5.2f}")
    
    if len(trees) > 0:
        heights = [t['height'] for t in trees]
        spreads = [t['spread'] for t in trees]
        print("-" * 50)
        print(f"  평균 수고: {np.mean(heights):.2f}m  (표준편차: {np.std(heights):.2f}m)")
        print(f"  평균 수관 폭: {np.mean(spreads):.2f}m  (표준편차: {np.std(spreads):.2f}m)")
    print("=" * 60 + "\n")
    
    # ============ 시각화 ============
    fig = plt.figure(figsize=(16, 6))
    
    # --- 좌측: 2D 탑뷰 (나무 위치 + 바운딩 박스) ---
    ax1 = fig.add_subplot(121)
    ax1.set_facecolor('#2a2a2a')
    ax1.scatter(pts[::5, 0], pts[::5, 1], c='gray', s=0.1, alpha=0.2)
    
    for t in trees:
        bb = t['bb_min']
        w = t['bb_max'][0] - t['bb_min'][0]
        h = t['bb_max'][1] - t['bb_min'][1]
        rect = plt.Rectangle((bb[0], bb[1]), w, h, linewidth=2, 
                             edgecolor='red', facecolor='none', linestyle='-')
        ax1.add_patch(rect)
        cx, cy = t['center']
        ax1.annotate(f"#{t['id']}\n{t['height']:.1f}m", (cx, cy),
                    color='yellow', fontsize=7, ha='center', va='center',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='black', alpha=0.7))
    
    ax1.set_title("Top View: Detected Trees & Bounding Boxes")
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Y (m)")
    ax1.set_aspect('equal')
    
    # --- 우측: 3D 뷰 (바운딩 박스 + 높이 컬러맵) ---
    ax2 = fig.add_subplot(122, projection='3d')
    
    # 전체 Point Cloud (Height Ramp)
    show_step = max(1, len(pts) // 15000)
    z = pts[::show_step, 2]
    z_norm = (z - z.min()) / (z.max() - z.min() + 1e-6)
    ax2.scatter(pts[::show_step, 0], pts[::show_step, 1], pts[::show_step, 2],
                c=z_norm, cmap='jet', s=0.3, alpha=0.4)
    
    # 바운딩 박스 오버레이
    for t in trees:
        draw_bbox_3d(ax2, t['bb_min'], t['bb_max'])
    
    ax2.set_title(f"3D Phenotyping ({len(trees)} trees detected)")
    ax2.set_xlabel("X (m)")
    ax2.set_ylabel("Y (m)")
    ax2.set_zlabel("Z (Height, m)")
    ax2.view_init(elev=30, azim=-55)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    print(f"✅ 3D Phenotyping 측정 결과 이미지가 저장되었습니다: {save_path}")
    plt.show()

if __name__ == "__main__":
    run_measurement()
