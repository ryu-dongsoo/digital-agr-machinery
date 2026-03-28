"""
Step 2: RTK 보정 전/후 트랙터 주행 경로 비교
=============================================
일반 GNSS(2~5m 오차) vs RTK(2cm 오차)로 트랙터가 고랑을 따라
주행할 때의 경로 차이를 애니메이션으로 비교 시뮬레이션

학습 목표:
  - 일반 GNSS의 미터급 오차가 농업 현장에서 얼마나 치명적인지 체감
  - RTK 보정 시스템의 cm급 정밀도 효과를 직관적으로 이해
  - Cross-track Error(궤적 이탈) 개념 습득
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# Windows 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def rtk_comparison_simulation():
    print("🚜 RTK 보정 전/후 트랙터 경로 비교 시뮬레이션 시작...")
    print("   일반 GNSS(좌측)와 RTK(우측) 트랙터가 동일한 고랑을 따라 주행합니다.")
    
    # 목표 경로: 직선 고랑 (100m 직진)
    n_points = 200
    target_x = np.linspace(0, 100, n_points)  # 0~100m 직진
    target_y = np.zeros(n_points)               # 고랑 중심선 (y=0)
    
    # 고랑 폭 설정 (30cm = 한쪽 15cm)
    row_width = 0.30  # 미터
    
    # ── 일반 GNSS 궤적 (오차 2~5m, 랜덤 워크) ── 
    np.random.seed(42)
    gnss_noise = np.cumsum(np.random.normal(0, 0.15, n_points))  # 누적 드리프트
    gnss_noise = gnss_noise - np.mean(gnss_noise)  # 평균 0 보정
    gnss_noise *= 2.5 / np.std(gnss_noise)  # 표준편차 2.5m 수준
    gnss_y = target_y + gnss_noise
    
    # ── RTK 궤적 (오차 2cm) ──
    np.random.seed(42)
    rtk_noise = np.random.normal(0, 0.02, n_points)  # 2cm 가우시안 노이즈
    rtk_y = target_y + rtk_noise
    
    # 작물 위치 (고랑 양쪽 15cm에 배치)
    crop_x = np.linspace(0, 100, 50)
    crop_y_upper = np.full_like(crop_x, 0.15)
    crop_y_lower = np.full_like(crop_x, -0.15)
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 10),
                              gridspec_kw={'height_ratios': [3, 1]})
    
    # ═════════════ 상단: 주행 궤적 ═════════════
    # Left: 일반 GNSS
    ax1 = axes[0, 0]
    ax1.set_xlim(-5, 105)
    ax1.set_ylim(-5, 5)
    ax1.set_title("① 일반 GNSS (오차 2~5m)", fontsize=13, fontweight='bold', color='red')
    ax1.set_xlabel("주행 거리 (m)")
    ax1.set_ylabel("횡방향 이탈 (m)")
    ax1.set_facecolor('#f5f0e1')
    
    # 고랑 영역
    ax1.fill_between([-5, 105], -row_width/2, row_width/2, 
                     color='#8B4513', alpha=0.3, label='고랑 영역')
    ax1.axhline(0, color='#8B4513', linestyle='--', linewidth=1, alpha=0.5, label='목표 경로')
    
    # 작물 표시
    ax1.scatter(crop_x, crop_y_upper, c='green', marker='^', s=30, alpha=0.6, label='작물')
    ax1.scatter(crop_x, crop_y_lower, c='green', marker='^', s=30, alpha=0.6)
    
    # GNSS 궤적
    ax1.plot(target_x, gnss_y, 'r-', linewidth=1.5, alpha=0.8, label='GNSS 궤적')
    
    gnss_error = np.abs(gnss_y)
    crushed = gnss_error > row_width / 2
    ax1.scatter(target_x[crushed], gnss_y[crushed], c='red', s=5, alpha=0.5, zorder=5)
    
    crush_pct = np.sum(crushed) / len(crushed) * 100
    ax1.text(0.02, 0.95, f"⚠️ 작물 밟은 구간: {crush_pct:.0f}%",
            transform=ax1.transAxes, fontsize=11, color='red',
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax1.legend(loc='upper right', fontsize=8)
    
    # Right: RTK
    ax2 = axes[0, 1]
    ax2.set_xlim(-5, 105)
    ax2.set_ylim(-5, 5)
    ax2.set_title("② RTK 보정 (오차 2cm)", fontsize=13, fontweight='bold', color='green')
    ax2.set_xlabel("주행 거리 (m)")
    ax2.set_ylabel("횡방향 이탈 (m)")
    ax2.set_facecolor('#f5f0e1')
    
    ax2.fill_between([-5, 105], -row_width/2, row_width/2,
                     color='#8B4513', alpha=0.3, label='고랑 영역')
    ax2.axhline(0, color='#8B4513', linestyle='--', linewidth=1, alpha=0.5, label='목표 경로')
    
    ax2.scatter(crop_x, crop_y_upper, c='green', marker='^', s=30, alpha=0.6, label='작물')
    ax2.scatter(crop_x, crop_y_lower, c='green', marker='^', s=30, alpha=0.6)
    
    ax2.plot(target_x, rtk_y, 'b-', linewidth=1.5, alpha=0.8, label='RTK 궤적')
    
    rtk_error = np.abs(rtk_y)
    rtk_crush_pct = np.sum(rtk_error > row_width/2) / len(rtk_error) * 100
    ax2.text(0.02, 0.95, f"✅ 작물 밟은 구간: {rtk_crush_pct:.0f}%",
            transform=ax2.transAxes, fontsize=11, color='green',
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax2.legend(loc='upper right', fontsize=8)
    
    # ═════════════ 하단: Cross-track Error 시계열 ═════════════
    ax3 = axes[1, 0]
    ax3.plot(target_x, gnss_y, 'r-', linewidth=1.2, alpha=0.7, label='GNSS 이탈')
    ax3.fill_between(target_x, -row_width/2, row_width/2, color='green', alpha=0.15, label='안전 영역')
    ax3.axhline(0, color='gray', linestyle=':', linewidth=0.5)
    ax3.set_xlabel("주행 거리 (m)")
    ax3.set_ylabel("Cross-track Error (m)")
    ax3.set_title("GNSS 횡방향 이탈 오차 시계열", fontsize=10)
    ax3.legend(fontsize=8)
    ax3.set_ylim(-6, 6)
    
    ax4 = axes[1, 1]
    ax4.plot(target_x, rtk_y * 100, 'b-', linewidth=1.2, alpha=0.7, label='RTK 이탈')  # cm 단위
    ax4.fill_between(target_x, -row_width/2*100, row_width/2*100, color='green', alpha=0.15, label='안전 영역')
    ax4.axhline(0, color='gray', linestyle=':', linewidth=0.5)
    ax4.set_xlabel("주행 거리 (m)")
    ax4.set_ylabel("Cross-track Error (cm)")
    ax4.set_title("RTK 횡방향 이탈 오차 시계열 (cm 단위)", fontsize=10)
    ax4.legend(fontsize=8)
    ax4.set_ylim(-10, 10)
    
    plt.tight_layout()
    
    # 통계 출력
    print("\n" + "=" * 55)
    print("📊 주행 정밀도 비교 분석 결과")
    print("=" * 55)
    print(f"{'항목':<25} {'일반 GNSS':>12} {'RTK':>12}")
    print("-" * 55)
    print(f"{'평균 이탈 오차':<25} {np.mean(gnss_error):>10.2f} m {np.mean(rtk_error)*100:>9.1f} cm")
    print(f"{'최대 이탈 오차':<25} {np.max(gnss_error):>10.2f} m {np.max(rtk_error)*100:>9.1f} cm")
    print(f"{'작물 피해 구간 비율':<25} {crush_pct:>10.0f} % {rtk_crush_pct:>10.0f} %")
    print(f"{'평행 주행 적합성':<25} {'❌ 부적합':>12} {'✅ 완벽':>12}")
    print("=" * 55)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step2_result.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    print(f"\n✅ RTK 비교 결과 저장: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    rtk_comparison_simulation()
