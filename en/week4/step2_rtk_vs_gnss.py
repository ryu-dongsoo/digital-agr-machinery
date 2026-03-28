"""
Step 2: RTK vs Standard GNSS — Tractor Path Comparison
=======================================================
Simulates tractor driving along crop rows with standard GNSS (2-5m error)
vs RTK (2cm error), visualizing cross-track error and crop damage.

Learning Objectives:
  - Experience how meter-level GNSS error is devastating for row crops
  - Understand RTK cm-level precision effect intuitively
  - Learn the Cross-track Error concept
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def rtk_comparison_simulation():
    print("🚜 Starting RTK vs GNSS Tractor Path Comparison...")
    print("   Standard GNSS (left) and RTK (right) tractors drive along the same crop row.")
    
    n_points = 200
    target_x = np.linspace(0, 100, n_points)
    target_y = np.zeros(n_points)
    row_width = 0.30
    
    # Standard GNSS trajectory (2-5m random walk error)
    np.random.seed(42)
    gnss_noise = np.cumsum(np.random.normal(0, 0.15, n_points))
    gnss_noise = gnss_noise - np.mean(gnss_noise)
    gnss_noise *= 2.5 / np.std(gnss_noise)
    gnss_y = target_y + gnss_noise
    
    # RTK trajectory (2cm Gaussian noise)
    np.random.seed(42)
    rtk_noise = np.random.normal(0, 0.02, n_points)
    rtk_y = target_y + rtk_noise
    
    crop_x = np.linspace(0, 100, 50)
    crop_y_upper = np.full_like(crop_x, 0.15)
    crop_y_lower = np.full_like(crop_x, -0.15)
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 10),
                              gridspec_kw={'height_ratios': [3, 1]})
    
    # Top Left: Standard GNSS
    ax1 = axes[0, 0]
    ax1.set_xlim(-5, 105); ax1.set_ylim(-5, 5)
    ax1.set_title("① Standard GNSS (Error: 2-5m)", fontsize=13, fontweight='bold', color='red')
    ax1.set_xlabel("Distance (m)"); ax1.set_ylabel("Lateral Deviation (m)")
    ax1.set_facecolor('#f5f0e1')
    ax1.fill_between([-5, 105], -row_width/2, row_width/2, color='#8B4513', alpha=0.3, label='Row Zone')
    ax1.axhline(0, color='#8B4513', linestyle='--', linewidth=1, alpha=0.5, label='Target Path')
    ax1.scatter(crop_x, crop_y_upper, c='green', marker='^', s=30, alpha=0.6, label='Crops')
    ax1.scatter(crop_x, crop_y_lower, c='green', marker='^', s=30, alpha=0.6)
    ax1.plot(target_x, gnss_y, 'r-', linewidth=1.5, alpha=0.8, label='GNSS Path')
    
    gnss_error = np.abs(gnss_y)
    crushed = gnss_error > row_width / 2
    ax1.scatter(target_x[crushed], gnss_y[crushed], c='red', s=5, alpha=0.5, zorder=5)
    crush_pct = np.sum(crushed) / len(crushed) * 100
    ax1.text(0.02, 0.95, f"Crop Damage: {crush_pct:.0f}%",
            transform=ax1.transAxes, fontsize=11, color='red',
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax1.legend(loc='upper right', fontsize=8)
    
    # Top Right: RTK
    ax2 = axes[0, 1]
    ax2.set_xlim(-5, 105); ax2.set_ylim(-5, 5)
    ax2.set_title("② RTK Correction (Error: 2cm)", fontsize=13, fontweight='bold', color='green')
    ax2.set_xlabel("Distance (m)"); ax2.set_ylabel("Lateral Deviation (m)")
    ax2.set_facecolor('#f5f0e1')
    ax2.fill_between([-5, 105], -row_width/2, row_width/2, color='#8B4513', alpha=0.3, label='Row Zone')
    ax2.axhline(0, color='#8B4513', linestyle='--', linewidth=1, alpha=0.5, label='Target Path')
    ax2.scatter(crop_x, crop_y_upper, c='green', marker='^', s=30, alpha=0.6, label='Crops')
    ax2.scatter(crop_x, crop_y_lower, c='green', marker='^', s=30, alpha=0.6)
    ax2.plot(target_x, rtk_y, 'b-', linewidth=1.5, alpha=0.8, label='RTK Path')
    
    rtk_error = np.abs(rtk_y)
    rtk_crush_pct = np.sum(rtk_error > row_width/2) / len(rtk_error) * 100
    ax2.text(0.02, 0.95, f"Crop Damage: {rtk_crush_pct:.0f}%",
            transform=ax2.transAxes, fontsize=11, color='green',
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax2.legend(loc='upper right', fontsize=8)
    
    # Bottom Left: GNSS error time series
    ax3 = axes[1, 0]
    ax3.plot(target_x, gnss_y, 'r-', linewidth=1.2, alpha=0.7, label='GNSS Deviation')
    ax3.fill_between(target_x, -row_width/2, row_width/2, color='green', alpha=0.15, label='Safe Zone')
    ax3.axhline(0, color='gray', linestyle=':', linewidth=0.5)
    ax3.set_xlabel("Distance (m)"); ax3.set_ylabel("Cross-track Error (m)")
    ax3.set_title("GNSS Cross-track Error", fontsize=10)
    ax3.legend(fontsize=8); ax3.set_ylim(-6, 6)
    
    # Bottom Right: RTK error time series (cm)
    ax4 = axes[1, 1]
    ax4.plot(target_x, rtk_y * 100, 'b-', linewidth=1.2, alpha=0.7, label='RTK Deviation')
    ax4.fill_between(target_x, -row_width/2*100, row_width/2*100, color='green', alpha=0.15, label='Safe Zone')
    ax4.axhline(0, color='gray', linestyle=':', linewidth=0.5)
    ax4.set_xlabel("Distance (m)"); ax4.set_ylabel("Cross-track Error (cm)")
    ax4.set_title("RTK Cross-track Error (cm scale)", fontsize=10)
    ax4.legend(fontsize=8); ax4.set_ylim(-10, 10)
    
    plt.tight_layout()
    
    print("\n" + "=" * 55)
    print("Driving Precision Comparison Results")
    print("=" * 55)
    print(f"{'Metric':<25} {'Std GNSS':>12} {'RTK':>12}")
    print("-" * 55)
    print(f"{'Mean Deviation':<25} {np.mean(gnss_error):>10.2f} m {np.mean(rtk_error)*100:>9.1f} cm")
    print(f"{'Max Deviation':<25} {np.max(gnss_error):>10.2f} m {np.max(rtk_error)*100:>9.1f} cm")
    print(f"{'Crop Damage Ratio':<25} {crush_pct:>10.0f} % {rtk_crush_pct:>10.0f} %")
    print("=" * 55)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step2_result.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    print(f"\n✅ RTK comparison result saved: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    rtk_comparison_simulation()
