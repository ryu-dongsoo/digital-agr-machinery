"""
Step 3: A-B Line 경로 계획 & 경제성 분석 시뮬레이션
=====================================================
가상 농지(사다리꼴)에 A-B Line 기준 평행 패스를 자동 생성하고,
오버랩 수준(초보 운전자 vs RTK)에 따른 연료비·작업시간 경제성을 비교

학습 목표:
  - A-B Line 평행 주행의 원리와 Swath(작업폭) 개념 이해
  - 오버랩(겹침)이 연료비와 작업 시간에 미치는 정량적 영향 체감
  - RTK 투자 비용 회수 기간(ROI) 계산 능력 습득
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.collections import PatchCollection
import os

# Windows 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def ab_line_simulation():
    print("🗺️ A-B Line 경로 계획 & 경제성 분석 시뮬레이션 시작...")
    
    # ============================================================
    # 1. 가상 농지 정의 (사다리꼴, 약 1.2ha)
    # ============================================================
    # 사다리꼴 꼭짓점 (미터 단위)
    field_vertices = np.array([
        [0, 0],       # 좌하
        [120, 0],     # 우하
        [110, 100],   # 우상
        [10, 100],    # 좌상
        [0, 0]        # 닫기
    ])
    
    # 면적 계산 (신발끈 공식)
    x = field_vertices[:-1, 0]
    y = field_vertices[:-1, 1]
    area = 0.5 * abs(np.sum(x[:-1]*y[1:] - x[1:]*y[:-1]) + x[-1]*y[0] - x[0]*y[-1])
    area_ha = area / 10000
    
    # 작업기 제원
    implement_width = 2.5  # 로터리 작업기 폭 (m)
    tractor_speed = 6.0    # km/h
    turn_time = 20         # Headland 턴 시간 (초)
    fuel_rate = 15         # 연료 소비율 (L/h)
    fuel_price = 1800      # 경유 가격 (원/L)
    labor_hourly = 12000   # 인건비 (원/시간)
    rtk_cost = 10_000_000  # RTK 장비 비용 (원)
    
    # 헤드랜드 영역 (밭머리, 양쪽 5m씩)
    headland = 5.0
    
    # ============================================================
    # 2. 세 가지 시나리오별 패스 계산
    # ============================================================
    scenarios = {
        '초보 운전자\n(50cm 겹침)': {'overlap': 0.50, 'color': '#FF6B6B'},
        '숙련 운전자\n(20cm 겹침)': {'overlap': 0.20, 'color': '#FFD700'},
        'RTK 자동조향\n(2cm 겹침)':  {'overlap': 0.02, 'color': '#4ECDC4'},
    }
    
    field_width = 100 - 2 * headland  # 헤드랜드 제외 작업 가능 폭 (90m)
    field_length = 120 - 2 * headland  # 헤드랜드 제외 작업 가능 길이 (110m)
    
    results = {}
    for name, sc in scenarios.items():
        effective_width = implement_width - sc['overlap']
        n_passes = int(np.ceil(field_width / effective_width))
        total_distance = n_passes * field_length  # 총 주행 거리 (m)
        total_distance_km = total_distance / 1000
        
        work_time_h = total_distance_km / tractor_speed  # 이동 시간
        turn_time_h = (n_passes - 1) * turn_time / 3600  # 턴 시간
        total_time_h = work_time_h + turn_time_h
        
        fuel_used = total_time_h * fuel_rate  # 연료 (L)
        fuel_cost = fuel_used * fuel_price    # 연료비 (원)
        labor_cost = total_time_h * labor_hourly  # 인건비 (원)
        total_cost = fuel_cost + labor_cost
        
        wasted_area = n_passes * sc['overlap'] * field_length  # 낭비 면적 (m²)
        
        results[name] = {
            'n_passes': n_passes,
            'effective_width': effective_width,
            'total_distance': total_distance,
            'total_time_h': total_time_h,
            'fuel_used': fuel_used,
            'fuel_cost': fuel_cost,
            'labor_cost': labor_cost,
            'total_cost': total_cost,
            'wasted_area': wasted_area,
            'overlap': sc['overlap'],
            'color': sc['color'],
        }
    
    # ============================================================
    # 3. 시각화
    # ============================================================
    fig = plt.figure(figsize=(18, 10))
    
    # 3개 시나리오 농지 시각화 (상단)
    for i, (name, r) in enumerate(results.items()):
        ax = fig.add_subplot(2, 3, i + 1)
        
        # 농지 폴리곤
        field_poly = MplPolygon(field_vertices[:-1], fill=True, 
                               facecolor='#f5f0e1', edgecolor='#8B4513', linewidth=2)
        ax.add_patch(field_poly)
        
        # 헤드랜드 표시
        ax.fill_between([0, 120], 0, headland, color='#D2B48C', alpha=0.4)
        ax.fill_between([0, 120], 100 - headland, 100, color='#D2B48C', alpha=0.4)
        
        # A-B Line 패스 생성
        for p in range(r['n_passes']):
            y_pos = headland + p * r['effective_width']
            if y_pos > 100 - headland:
                break
            # 사다리꼴이므로 x 범위 계산
            frac = y_pos / 100
            x_left = headland + 10 * frac
            x_right = 120 - headland - 10 * frac
            
            ax.fill_between([x_left, x_right], 
                          y_pos - implement_width/2, y_pos + implement_width/2,
                          color=r['color'], alpha=0.15, edgecolor=r['color'], linewidth=0.5)
            ax.plot([x_left, x_right], [y_pos, y_pos], 
                   color=r['color'], linewidth=0.8, alpha=0.6)
        
        ax.set_xlim(-5, 125)
        ax.set_ylim(-5, 105)
        ax.set_aspect('equal')
        ax.set_title(f"{name}\n({r['n_passes']}패스)", fontsize=11, fontweight='bold')
        ax.set_xlabel("X (m)")
        if i == 0:
            ax.set_ylabel("Y (m)")
        
        # A, B 마커
        ax.plot(headland, headland, 'ro', markersize=12, zorder=10)
        ax.annotate('A', (headland, headland), fontsize=12, fontweight='bold',
                   color='red', ha='center', va='bottom', xytext=(0, 8), textcoords='offset points')
        ax.plot(120 - headland, headland, 'bs', markersize=12, zorder=10)
        ax.annotate('B', (120 - headland, headland), fontsize=12, fontweight='bold',
                   color='blue', ha='center', va='bottom', xytext=(0, 8), textcoords='offset points')
    
    # ── 하단 좌측: 비용 비교 막대그래프 ──
    ax_bar = fig.add_subplot(2, 3, 4)
    names = list(results.keys())
    fuel_costs = [r['fuel_cost'] / 10000 for r in results.values()]
    labor_costs = [r['labor_cost'] / 10000 for r in results.values()]
    colors = [r['color'] for r in results.values()]
    
    x_pos = np.arange(len(names))
    bars1 = ax_bar.bar(x_pos, fuel_costs, 0.35, label='연료비', color=colors, alpha=0.7, edgecolor='white')
    bars2 = ax_bar.bar(x_pos, labor_costs, 0.35, bottom=fuel_costs, label='인건비', 
                       color=colors, alpha=0.4, edgecolor='white', hatch='///')
    
    for i, (fc, lc) in enumerate(zip(fuel_costs, labor_costs)):
        ax_bar.text(i, fc + lc + 0.1, f'{(fc+lc):.1f}만원', ha='center', fontsize=9, fontweight='bold')
    
    ax_bar.set_xticks(x_pos)
    ax_bar.set_xticklabels([n.replace('\n', ' ') for n in names], fontsize=8)
    ax_bar.set_ylabel("비용 (만원)")
    ax_bar.set_title("1회 작업 비용 비교", fontsize=12, fontweight='bold')
    ax_bar.legend(fontsize=8)
    
    # ── 하단 중앙: 작업 시간 비교 ──
    ax_time = fig.add_subplot(2, 3, 5)
    times = [r['total_time_h'] * 60 for r in results.values()]  # 분 단위
    ax_time.barh(x_pos, times, color=colors, edgecolor='white', height=0.5)
    for i, t in enumerate(times):
        ax_time.text(t + 0.5, i, f'{t:.0f}분', va='center', fontsize=10, fontweight='bold')
    ax_time.set_yticks(x_pos)
    ax_time.set_yticklabels([n.replace('\n', ' ') for n in names], fontsize=8)
    ax_time.set_xlabel("작업 시간 (분)")
    ax_time.set_title("1회 작업 시간 비교", fontsize=12, fontweight='bold')
    
    # ── 하단 우측: RTK 투자 회수 분석 ──
    ax_roi = fig.add_subplot(2, 3, 6)
    
    novice_cost = list(results.values())[0]['total_cost']
    rtk_running = list(results.values())[2]['total_cost']
    savings_per_work = novice_cost - rtk_running  # 1회 절감액
    
    works = np.arange(0, 201)
    cumulative_savings = works * savings_per_work
    
    ax_roi.plot(works, cumulative_savings / 10000, 'g-', linewidth=2, label='누적 절감액')
    ax_roi.axhline(rtk_cost / 10000, color='red', linestyle='--', linewidth=1.5, label=f'RTK 장비 비용 ({rtk_cost//10000}만원)')
    
    # 손익 분기점
    if savings_per_work > 0:
        breakeven = int(np.ceil(rtk_cost / savings_per_work))
        ax_roi.axvline(breakeven, color='orange', linestyle=':', linewidth=1.5)
        ax_roi.text(breakeven + 3, rtk_cost / 10000 * 0.5, 
                   f'손익분기: {breakeven}회\n(연 20회 → {breakeven//20}년)',
                   fontsize=9, color='orange',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    ax_roi.set_xlabel("누적 작업 횟수")
    ax_roi.set_ylabel("금액 (만원)")
    ax_roi.set_title("RTK 투자 회수 분석 (ROI)", fontsize=12, fontweight='bold')
    ax_roi.legend(fontsize=8)
    ax_roi.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # 콘솔 출력
    print("\n" + "=" * 70)
    print(f"🗺️ A-B Line 경로 계획 분석 결과 (농지 면적: {area_ha:.2f} ha)")
    print("=" * 70)
    print(f"{'항목':<20} {'초보(50cm)':>12} {'숙련(20cm)':>12} {'RTK(2cm)':>12}")
    print("-" * 70)
    for key, label in [('n_passes', '패스 수'),
                        ('total_time_h', '작업 시간(h)'),
                        ('fuel_used', '연료(L)'),
                        ('total_cost', '총 비용(원)')]:
        vals = [results[n][key] for n in names]
        if key == 'total_cost':
            print(f"  {label:<18} {vals[0]:>10,.0f} {vals[1]:>10,.0f} {vals[2]:>10,.0f}")
        elif key == 'total_time_h':
            print(f"  {label:<18} {vals[0]:>10.1f} {vals[1]:>10.1f} {vals[2]:>10.1f}")
        else:
            print(f"  {label:<18} {vals[0]:>10.1f} {vals[1]:>10.1f} {vals[2]:>10.1f}")
    print("-" * 70)
    if savings_per_work > 0:
        print(f"  {'RTK 투자 회수':<18} {breakeven}회 (연 20회 작업 시 약 {breakeven//20}년)")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step3_result.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    print(f"\n✅ A-B Line 경제성 분석 결과 저장: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    ab_line_simulation()
