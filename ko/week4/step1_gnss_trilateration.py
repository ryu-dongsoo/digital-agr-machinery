"""
Step 1: GNSS 삼변측량(Trilateration) 시뮬레이션
==================================================
위성 4개의 신호가 수신기 위치를 결정하는 과정을
원(Circle) 교차 애니메이션으로 시각적으로 체험

학습 목표:
  - 삼변측량 원리: 각 위성까지의 거리(반지름)가 원을 형성, 교차점이 수신기 위치
  - GNSS 오차 원인: 대기 지연, 시계 오차 등으로 원이 정확히 한 점에서 만나지 않음
  - 위성 수 증가에 따른 정밀도 향상 효과 확인
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import os

# Windows 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ============================================================
# 1. 위성 배치 및 삼변측량 시뮬레이션
# ============================================================
def trilateration_simulation():
    print("📡 GNSS 삼변측량(Trilateration) 시뮬레이션 시작...")
    print("   위성 4개의 거리 원이 교차하여 수신기 위치를 결정하는 과정을 관찰하세요.")
    
    # 실제 수신기(트랙터) 위치 (정답)
    true_pos = np.array([5.0, 4.0])
    
    # 위성 4개 위치 (하늘 위에서 바라본 2D 투영)
    satellites = np.array([
        [1.0, 9.0],   # GPS 위성 1
        [9.0, 8.0],   # GPS 위성 2
        [8.0, 1.0],   # GPS 위성 3
        [2.0, 2.0],   # GPS 위성 4
    ])
    sat_names = ["GPS-1", "GPS-2", "GPS-3", "GPS-4"]
    sat_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    # 실제 거리 계산
    true_distances = np.sqrt(np.sum((satellites - true_pos)**2, axis=1))
    
    # 오차가 포함된 거리 (대기 지연, 시계 오차 시뮬레이션)
    np.random.seed(42)
    noisy_distances = true_distances + np.random.normal(0, 0.4, len(true_distances))
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # ── Panel 1: 이상적 삼변측량 (오차 없음) ──
    ax1 = axes[0]
    ax1.set_xlim(-1, 11)
    ax1.set_ylim(-1, 11)
    ax1.set_aspect('equal')
    ax1.set_title("① 이상적 삼변측량 (오차 0)", fontsize=12, fontweight='bold')
    ax1.set_xlabel("X (km)")
    ax1.set_ylabel("Y (km)")
    ax1.set_facecolor('#1a1a2e')
    ax1.grid(True, alpha=0.2, color='white')
    
    for i, (sx, sy) in enumerate(satellites):
        circle = Circle((sx, sy), true_distances[i], fill=False, 
                        color=sat_colors[i], linewidth=2, linestyle='--', alpha=0.7)
        ax1.add_patch(circle)
        ax1.plot(sx, sy, '*', color=sat_colors[i], markersize=15, 
                markeredgecolor='white', markeredgewidth=0.5)
        ax1.annotate(f'🛰️ {sat_names[i]}', (sx, sy), color=sat_colors[i],
                    fontsize=8, ha='center', va='bottom', 
                    xytext=(0, 10), textcoords='offset points')
    
    ax1.plot(*true_pos, 'r^', markersize=15, markeredgecolor='white', 
             markeredgewidth=1.5, zorder=10)
    ax1.annotate('🚜 수신기\n(정확한 위치)', true_pos, color='white', fontsize=9,
                ha='center', va='top', xytext=(0, -15), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='green', alpha=0.7))
    ax1.text(0.5, 0.95, "✅ 4개 원이 정확히 한 점에서 교차",
            transform=ax1.transAxes, ha='center', va='top', color='lime',
            fontsize=9, bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
    
    # ── Panel 2: 현실적 삼변측량 (오차 포함) ──
    ax2 = axes[1]
    ax2.set_xlim(-1, 11)
    ax2.set_ylim(-1, 11)
    ax2.set_aspect('equal')
    ax2.set_title("② 현실 GNSS (대기 오차 포함)", fontsize=12, fontweight='bold')
    ax2.set_xlabel("X (km)")
    ax2.set_facecolor('#1a1a2e')
    ax2.grid(True, alpha=0.2, color='white')
    
    for i, (sx, sy) in enumerate(satellites):
        circle = Circle((sx, sy), noisy_distances[i], fill=False,
                        color=sat_colors[i], linewidth=2, linestyle='--', alpha=0.7)
        ax2.add_patch(circle)
        ax2.plot(sx, sy, '*', color=sat_colors[i], markersize=15,
                markeredgecolor='white', markeredgewidth=0.5)
        ax2.annotate(f'🛰️ {sat_names[i]}', (sx, sy), color=sat_colors[i],
                    fontsize=8, ha='center', va='bottom',
                    xytext=(0, 10), textcoords='offset points')
    
    # 오차 범위 표시 (진한 원)
    error_circle = Circle(true_pos, 0.8, fill=True, color='red', alpha=0.2)
    ax2.add_patch(error_circle)
    
    # 여러 번 측정한 결과 (산점도)
    np.random.seed(123)
    scatter_pts = true_pos + np.random.normal(0, 0.5, (30, 2))
    ax2.scatter(scatter_pts[:, 0], scatter_pts[:, 1], c='yellow', s=10, alpha=0.6, zorder=5)
    
    ax2.plot(*true_pos, 'r^', markersize=15, markeredgecolor='white',
             markeredgewidth=1.5, zorder=10)
    estimated_pos = np.mean(scatter_pts, axis=0)
    ax2.plot(*estimated_pos, 'o', color='yellow', markersize=10,
             markeredgecolor='white', markeredgewidth=1.5, zorder=10)
    ax2.annotate(f'추정 위치\n(오차 ≈ 2~5m)', estimated_pos, color='yellow', fontsize=8,
                ha='center', va='top', xytext=(0, -15), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='darkred', alpha=0.7))
    ax2.text(0.5, 0.95, "⚠️ 원들이 한 점에서 만나지 않음 → 오차 발생",
            transform=ax2.transAxes, ha='center', va='top', color='orange',
            fontsize=9, bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
    
    # ── Panel 3: 위성 수에 따른 정밀도 비교 ──
    ax3 = axes[2]
    sat_counts = [4, 8, 12, 20, 30, 40]
    errors = [4.5, 2.8, 1.9, 1.2, 0.8, 0.5]  # 대략적 오차 (미터)
    
    bars = ax3.bar(range(len(sat_counts)), errors, color=['#FF6B6B', '#FFA07A', '#FFD700', '#90EE90', '#4ECDC4', '#45B7D1'],
                   edgecolor='white', linewidth=0.5)
    ax3.set_xticks(range(len(sat_counts)))
    ax3.set_xticklabels([f'{n}개' for n in sat_counts])
    ax3.set_xlabel("수신 가능 위성 수")
    ax3.set_ylabel("평균 위치 오차 (m)")
    ax3.set_title("③ Multi-Constellation 효과", fontsize=12, fontweight='bold')
    ax3.set_facecolor('#1a1a2e')
    ax3.grid(True, alpha=0.2, axis='y', color='white')
    
    for bar, err in zip(bars, errors):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{err}m', ha='center', va='bottom', fontsize=9, fontweight='bold', color='white')
    
    ax3.axhline(y=2.0, color='red', linestyle=':', linewidth=1.5, alpha=0.7)
    ax3.text(5.5, 2.2, "← 일반 GNSS 한계선 (2m)", color='red', fontsize=8, ha='right')
    
    ax3.axhline(y=0.02, color='lime', linestyle=':', linewidth=1.5, alpha=0.7)
    ax3.text(5.5, 0.15, "← RTK 목표 (2cm)", color='lime', fontsize=8, ha='right')
    
    plt.tight_layout()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step1_result.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight', facecolor='#0d1117')
    print(f"✅ 삼변측량 시뮬레이션 결과 저장: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    trilateration_simulation()
