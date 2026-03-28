"""
Step 1: GNSS Trilateration Simulation
========================================
Visualize how 4 satellite distance circles intersect to determine
the receiver position, and the effect of atmospheric errors.

Learning Objectives:
  - Trilateration principle: distance from each satellite forms a circle; intersection = position
  - GNSS error sources: atmospheric delay, clock errors cause circles to misalign
  - Multi-constellation benefit: more satellites = higher precision
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import os

def trilateration_simulation():
    print("📡 Starting GNSS Trilateration Simulation...")
    print("   Observe how 4 satellite distance circles intersect to determine receiver position.")
    
    true_pos = np.array([5.0, 4.0])
    
    satellites = np.array([
        [1.0, 9.0],
        [9.0, 8.0],
        [8.0, 1.0],
        [2.0, 2.0],
    ])
    sat_names = ["GPS-1", "GPS-2", "GPS-3", "GPS-4"]
    sat_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    true_distances = np.sqrt(np.sum((satellites - true_pos)**2, axis=1))
    
    np.random.seed(42)
    noisy_distances = true_distances + np.random.normal(0, 0.4, len(true_distances))
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Panel 1: Ideal Trilateration
    ax1 = axes[0]
    ax1.set_xlim(-1, 11); ax1.set_ylim(-1, 11)
    ax1.set_aspect('equal')
    ax1.set_title("① Ideal Trilateration (Zero Error)", fontsize=12, fontweight='bold')
    ax1.set_xlabel("X (km)"); ax1.set_ylabel("Y (km)")
    ax1.set_facecolor('#1a1a2e')
    ax1.grid(True, alpha=0.2, color='white')
    
    for i, (sx, sy) in enumerate(satellites):
        circle = Circle((sx, sy), true_distances[i], fill=False,
                        color=sat_colors[i], linewidth=2, linestyle='--', alpha=0.7)
        ax1.add_patch(circle)
        ax1.plot(sx, sy, '*', color=sat_colors[i], markersize=15,
                markeredgecolor='white', markeredgewidth=0.5)
        ax1.annotate(f'{sat_names[i]}', (sx, sy), color=sat_colors[i],
                    fontsize=8, ha='center', va='bottom',
                    xytext=(0, 10), textcoords='offset points')
    
    ax1.plot(*true_pos, 'r^', markersize=15, markeredgecolor='white',
             markeredgewidth=1.5, zorder=10)
    ax1.annotate('Receiver\n(True Position)', true_pos, color='white', fontsize=9,
                ha='center', va='top', xytext=(0, -15), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='green', alpha=0.7))
    ax1.text(0.5, 0.95, "All 4 circles intersect at exactly one point",
            transform=ax1.transAxes, ha='center', va='top', color='lime',
            fontsize=9, bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
    
    # Panel 2: Real GNSS with errors
    ax2 = axes[1]
    ax2.set_xlim(-1, 11); ax2.set_ylim(-1, 11)
    ax2.set_aspect('equal')
    ax2.set_title("② Real GNSS (Atmospheric Errors)", fontsize=12, fontweight='bold')
    ax2.set_xlabel("X (km)")
    ax2.set_facecolor('#1a1a2e')
    ax2.grid(True, alpha=0.2, color='white')
    
    for i, (sx, sy) in enumerate(satellites):
        circle = Circle((sx, sy), noisy_distances[i], fill=False,
                        color=sat_colors[i], linewidth=2, linestyle='--', alpha=0.7)
        ax2.add_patch(circle)
        ax2.plot(sx, sy, '*', color=sat_colors[i], markersize=15,
                markeredgecolor='white', markeredgewidth=0.5)
        ax2.annotate(f'{sat_names[i]}', (sx, sy), color=sat_colors[i],
                    fontsize=8, ha='center', va='bottom',
                    xytext=(0, 10), textcoords='offset points')
    
    error_circle = Circle(true_pos, 0.8, fill=True, color='red', alpha=0.2)
    ax2.add_patch(error_circle)
    
    np.random.seed(123)
    scatter_pts = true_pos + np.random.normal(0, 0.5, (30, 2))
    ax2.scatter(scatter_pts[:, 0], scatter_pts[:, 1], c='yellow', s=10, alpha=0.6, zorder=5)
    
    ax2.plot(*true_pos, 'r^', markersize=15, markeredgecolor='white',
             markeredgewidth=1.5, zorder=10)
    estimated_pos = np.mean(scatter_pts, axis=0)
    ax2.plot(*estimated_pos, 'o', color='yellow', markersize=10,
             markeredgecolor='white', markeredgewidth=1.5, zorder=10)
    ax2.annotate(f'Estimated Position\n(Error: 2-5m)', estimated_pos, color='yellow', fontsize=8,
                ha='center', va='top', xytext=(0, -15), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='darkred', alpha=0.7))
    ax2.text(0.5, 0.95, "Circles don't meet at one point -> Position error",
            transform=ax2.transAxes, ha='center', va='top', color='orange',
            fontsize=9, bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
    
    # Panel 3: Multi-Constellation
    ax3 = axes[2]
    sat_counts = [4, 8, 12, 20, 30, 40]
    errors = [4.5, 2.8, 1.9, 1.2, 0.8, 0.5]
    
    bars = ax3.bar(range(len(sat_counts)), errors,
                   color=['#FF6B6B', '#FFA07A', '#FFD700', '#90EE90', '#4ECDC4', '#45B7D1'],
                   edgecolor='white', linewidth=0.5)
    ax3.set_xticks(range(len(sat_counts)))
    ax3.set_xticklabels([str(n) for n in sat_counts])
    ax3.set_xlabel("Number of Visible Satellites")
    ax3.set_ylabel("Average Position Error (m)")
    ax3.set_title("③ Multi-Constellation Effect", fontsize=12, fontweight='bold')
    ax3.set_facecolor('#1a1a2e')
    ax3.grid(True, alpha=0.2, axis='y', color='white')
    
    for bar, err in zip(bars, errors):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{err}m', ha='center', va='bottom', fontsize=9, fontweight='bold', color='white')
    
    ax3.axhline(y=2.0, color='red', linestyle=':', linewidth=1.5, alpha=0.7)
    ax3.text(5.5, 2.2, "Standard GNSS limit (2m)", color='red', fontsize=8, ha='right')
    
    ax3.axhline(y=0.02, color='lime', linestyle=':', linewidth=1.5, alpha=0.7)
    ax3.text(5.5, 0.15, "RTK target (2cm)", color='lime', fontsize=8, ha='right')
    
    plt.tight_layout()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step1_result.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight', facecolor='#0d1117')
    print(f"✅ Trilateration simulation result saved: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    trilateration_simulation()
