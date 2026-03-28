"""
Step 3: A-B Line Path Planning & Economic Analysis
====================================================
Generates parallel passes on a virtual trapezoidal field (~1.2ha) using
A-B Line guidance, comparing 3 overlap scenarios and calculating ROI.

Learning Objectives:
  - Understand A-B Line parallel driving and Swath (implement width) concepts
  - Quantify how overlap affects fuel cost and work time
  - Calculate RTK investment payback period (ROI)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
import os

def ab_line_simulation():
    print("Starting A-B Line Path Planning & Economic Analysis...")
    
    # Virtual field (trapezoid, ~1.2ha)
    field_vertices = np.array([
        [0, 0], [120, 0], [110, 100], [10, 100], [0, 0]
    ])
    
    x = field_vertices[:-1, 0]; y = field_vertices[:-1, 1]
    area = 0.5 * abs(np.sum(x[:-1]*y[1:] - x[1:]*y[:-1]) + x[-1]*y[0] - x[0]*y[-1])
    area_ha = area / 10000
    
    implement_width = 2.5   # m
    tractor_speed = 6.0     # km/h
    turn_time = 20          # seconds
    fuel_rate = 15          # L/h
    fuel_price = 1800       # KRW/L
    labor_hourly = 12000    # KRW/h
    rtk_cost = 10_000_000   # KRW
    headland = 5.0          # m
    
    scenarios = {
        'Novice\n(50cm overlap)': {'overlap': 0.50, 'color': '#FF6B6B'},
        'Expert\n(20cm overlap)':  {'overlap': 0.20, 'color': '#FFD700'},
        'RTK Auto-steer\n(2cm overlap)': {'overlap': 0.02, 'color': '#4ECDC4'},
    }
    
    field_width = 100 - 2 * headland
    field_length = 120 - 2 * headland
    
    results = {}
    for name, sc in scenarios.items():
        ew = implement_width - sc['overlap']
        n_passes = int(np.ceil(field_width / ew))
        total_dist = n_passes * field_length
        work_h = (total_dist / 1000) / tractor_speed
        turn_h = (n_passes - 1) * turn_time / 3600
        total_h = work_h + turn_h
        fuel = total_h * fuel_rate
        fc = fuel * fuel_price
        lc = total_h * labor_hourly
        
        results[name] = {
            'n_passes': n_passes, 'effective_width': ew,
            'total_distance': total_dist, 'total_time_h': total_h,
            'fuel_used': fuel, 'fuel_cost': fc, 'labor_cost': lc,
            'total_cost': fc + lc, 'overlap': sc['overlap'], 'color': sc['color'],
        }
    
    fig = plt.figure(figsize=(18, 10))
    
    for i, (name, r) in enumerate(results.items()):
        ax = fig.add_subplot(2, 3, i + 1)
        field_poly = MplPolygon(field_vertices[:-1], fill=True,
                               facecolor='#f5f0e1', edgecolor='#8B4513', linewidth=2)
        ax.add_patch(field_poly)
        ax.fill_between([0, 120], 0, headland, color='#D2B48C', alpha=0.4)
        ax.fill_between([0, 120], 100 - headland, 100, color='#D2B48C', alpha=0.4)
        
        for p in range(r['n_passes']):
            y_pos = headland + p * r['effective_width']
            if y_pos > 100 - headland: break
            frac = y_pos / 100
            x_left = headland + 10 * frac
            x_right = 120 - headland - 10 * frac
            ax.fill_between([x_left, x_right],
                          y_pos - implement_width/2, y_pos + implement_width/2,
                          color=r['color'], alpha=0.15, edgecolor=r['color'], linewidth=0.5)
            ax.plot([x_left, x_right], [y_pos, y_pos], color=r['color'], linewidth=0.8, alpha=0.6)
        
        ax.set_xlim(-5, 125); ax.set_ylim(-5, 105); ax.set_aspect('equal')
        ax.set_title(f"{name}\n({r['n_passes']} passes)", fontsize=11, fontweight='bold')
        ax.set_xlabel("X (m)")
        if i == 0: ax.set_ylabel("Y (m)")
        
        ax.plot(headland, headland, 'ro', markersize=12, zorder=10)
        ax.annotate('A', (headland, headland), fontsize=12, fontweight='bold',
                   color='red', ha='center', va='bottom', xytext=(0, 8), textcoords='offset points')
        ax.plot(120 - headland, headland, 'bs', markersize=12, zorder=10)
        ax.annotate('B', (120 - headland, headland), fontsize=12, fontweight='bold',
                   color='blue', ha='center', va='bottom', xytext=(0, 8), textcoords='offset points')
    
    # Cost comparison
    ax_bar = fig.add_subplot(2, 3, 4)
    names = list(results.keys())
    fuel_costs = [r['fuel_cost'] / 10000 for r in results.values()]
    labor_costs = [r['labor_cost'] / 10000 for r in results.values()]
    colors = [r['color'] for r in results.values()]
    x_pos = np.arange(len(names))
    
    ax_bar.bar(x_pos, fuel_costs, 0.35, label='Fuel', color=colors, alpha=0.7, edgecolor='white')
    ax_bar.bar(x_pos, labor_costs, 0.35, bottom=fuel_costs, label='Labor',
               color=colors, alpha=0.4, edgecolor='white', hatch='///')
    for i, (fc, lc) in enumerate(zip(fuel_costs, labor_costs)):
        ax_bar.text(i, fc + lc + 0.1, f'{(fc+lc):.1f}', ha='center', fontsize=9, fontweight='bold')
    ax_bar.set_xticks(x_pos)
    ax_bar.set_xticklabels([n.replace('\n', ' ') for n in names], fontsize=8)
    ax_bar.set_ylabel("Cost (x10,000 KRW)"); ax_bar.set_title("Cost per Operation", fontsize=12, fontweight='bold')
    ax_bar.legend(fontsize=8)
    
    # Time comparison
    ax_time = fig.add_subplot(2, 3, 5)
    times = [r['total_time_h'] * 60 for r in results.values()]
    ax_time.barh(x_pos, times, color=colors, edgecolor='white', height=0.5)
    for i, t in enumerate(times):
        ax_time.text(t + 0.5, i, f'{t:.0f} min', va='center', fontsize=10, fontweight='bold')
    ax_time.set_yticks(x_pos)
    ax_time.set_yticklabels([n.replace('\n', ' ') for n in names], fontsize=8)
    ax_time.set_xlabel("Work Time (min)"); ax_time.set_title("Time per Operation", fontsize=12, fontweight='bold')
    
    # ROI analysis
    ax_roi = fig.add_subplot(2, 3, 6)
    novice_cost = list(results.values())[0]['total_cost']
    rtk_running = list(results.values())[2]['total_cost']
    savings = novice_cost - rtk_running
    
    works = np.arange(0, 201)
    ax_roi.plot(works, works * savings / 10000, 'g-', linewidth=2, label='Cumulative Savings')
    ax_roi.axhline(rtk_cost / 10000, color='red', linestyle='--', linewidth=1.5,
                   label=f'RTK Cost ({rtk_cost//10000}x10k KRW)')
    if savings > 0:
        be = int(np.ceil(rtk_cost / savings))
        ax_roi.axvline(be, color='orange', linestyle=':', linewidth=1.5)
        ax_roi.text(be + 3, rtk_cost / 10000 * 0.5,
                   f'Break-even: {be} ops\n(20/yr = {be//20} yrs)',
                   fontsize=9, color='orange',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax_roi.set_xlabel("Cumulative Operations"); ax_roi.set_ylabel("Amount (x10,000 KRW)")
    ax_roi.set_title("RTK Investment ROI", fontsize=12, fontweight='bold')
    ax_roi.legend(fontsize=8); ax_roi.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    print(f"\nA-B Line Analysis (Field: {area_ha:.2f} ha)")
    print("=" * 60)
    print(f"{'Metric':<20} {'Novice':>12} {'Expert':>12} {'RTK':>12}")
    print("-" * 60)
    for key, label in [('n_passes', 'Passes'), ('total_time_h', 'Time (h)'),
                        ('fuel_used', 'Fuel (L)'), ('total_cost', 'Cost (KRW)')]:
        vals = [results[n][key] for n in names]
        if key == 'total_cost':
            print(f"  {label:<18} {vals[0]:>10,.0f} {vals[1]:>10,.0f} {vals[2]:>10,.0f}")
        else:
            print(f"  {label:<18} {vals[0]:>10.1f} {vals[1]:>10.1f} {vals[2]:>10.1f}")
    print("=" * 60)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step3_result.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    print(f"\n✅ A-B Line analysis result saved: {save_path}")
    plt.show()

if __name__ == "__main__":
    ab_line_simulation()
