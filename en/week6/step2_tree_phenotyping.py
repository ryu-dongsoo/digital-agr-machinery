"""
Step 2: 3D Crop Phenotyping — Automated Measurement
=====================================================
Analyzes the orchard Point Cloud collected in Step 1 to automatically
extract tree height and canopy spread for each individual tree,
overlaying red bounding boxes.

Learning Objectives:
  - Understand segmentation principles for isolating objects from Point Cloud data
  - Experience automated crop dimension extraction via Axis-Aligned Bounding Box (AABB)
  - Appreciate the efficiency of digital agriculture vs manual measurement
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os

# ============================================================
# 1. Automatic Tree Detection (Grid-based Segmentation)
# ============================================================
def detect_trees(pts, grid_size=3.0, min_height=1.5, min_pts=50):
    """
    Divides the Point Cloud into a grid and identifies cells
    containing high-Z points (above min_height) as tree locations.
    In practice, advanced algorithms like DBSCAN or PointNet are used.
    """
    trees = []
    
    x_min, x_max = pts[:, 0].min(), pts[:, 0].max()
    y_min, y_max = pts[:, 1].min(), pts[:, 1].max()
    
    x_bins = np.arange(x_min, x_max, grid_size)
    y_bins = np.arange(y_min, y_max, grid_size)
    
    for x_start in x_bins:
        for y_start in y_bins:
            mask = (
                (pts[:, 0] >= x_start) & (pts[:, 0] < x_start + grid_size) &
                (pts[:, 1] >= y_start) & (pts[:, 1] < y_start + grid_size) &
                (pts[:, 2] > min_height)
            )
            cell_pts = pts[mask]
            
            if len(cell_pts) >= min_pts:
                bb_min = np.min(cell_pts, axis=0)
                bb_max = np.max(cell_pts, axis=0)
                
                all_mask = (
                    (pts[:, 0] >= x_start) & (pts[:, 0] < x_start + grid_size) &
                    (pts[:, 1] >= y_start) & (pts[:, 1] < y_start + grid_size)
                )
                ground_z = np.percentile(pts[all_mask][:, 2], 5)
                
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
# 2. 3D Bounding Box Drawing Utility
# ============================================================
def draw_bbox_3d(ax, bb_min, bb_max, color='red', alpha=0.15):
    """Draws a wireframe bounding box on a 3D axis."""
    x0, y0, z0 = bb_min
    x1, y1, z1 = bb_max
    
    corners = np.array([
        [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
        [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]
    ])
    
    edges = [
        [0,1], [1,2], [2,3], [3,0],
        [4,5], [5,6], [6,7], [7,4],
        [0,4], [1,5], [2,6], [3,7]
    ]
    for e in edges:
        ax.plot3D(*zip(corners[e[0]], corners[e[1]]), color=color, linewidth=1.5, alpha=0.8)
    
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
# 3. Main Visualization and Measurement
# ============================================================
def run_measurement():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    npy_path = os.path.join(base_dir, "scanned_orchard.npy")
    save_path = os.path.join(base_dir, "step2_result.png")
    
    if not os.path.exists(npy_path):
        print("⚠️ No scan data from Step 1 found. Generating orchard data internally.")
        print("   (For better results, run step1_lidar_scanning_simulation.py first!)")
        from step1_lidar_scanning_simulation import create_orchard_environment
        pts, _ = create_orchard_environment()
    else:
        pts = np.load(npy_path)
    
    print(f"📊 Loaded. Total points: {len(pts):,}")
    
    print("🌳 Running automatic tree detection (Grid Segmentation)...")
    trees = detect_trees(pts)
    print(f"   → {len(trees)} trees detected!")
    
    # Measurement results
    print("\n" + "=" * 60)
    print(f"🌳 3D Phenotyping Results ({len(trees)} trees)")
    print("=" * 60)
    print(f"{'No.':<5} {'Center (X,Y)':<18} {'Height(m)':<10} {'Spread(m)':<10}")
    print("-" * 50)
    for t in trees:
        cx, cy = t['center']
        print(f"  {t['id']:<3}  ({cx:5.1f}, {cy:5.1f})     {t['height']:5.2f}     {t['spread']:5.2f}")
    
    if len(trees) > 0:
        heights = [t['height'] for t in trees]
        spreads = [t['spread'] for t in trees]
        print("-" * 50)
        print(f"  Mean Height: {np.mean(heights):.2f}m  (Std: {np.std(heights):.2f}m)")
        print(f"  Mean Spread: {np.mean(spreads):.2f}m  (Std: {np.std(spreads):.2f}m)")
    print("=" * 60 + "\n")
    
    # Visualization
    fig = plt.figure(figsize=(16, 6))
    
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
    
    ax2 = fig.add_subplot(122, projection='3d')
    
    show_step = max(1, len(pts) // 15000)
    z = pts[::show_step, 2]
    z_norm = (z - z.min()) / (z.max() - z.min() + 1e-6)
    ax2.scatter(pts[::show_step, 0], pts[::show_step, 1], pts[::show_step, 2],
                c=z_norm, cmap='jet', s=0.3, alpha=0.4)
    
    for t in trees:
        draw_bbox_3d(ax2, t['bb_min'], t['bb_max'])
    
    ax2.set_title(f"3D Phenotyping ({len(trees)} trees detected)")
    ax2.set_xlabel("X (m)")
    ax2.set_ylabel("Y (m)")
    ax2.set_zlabel("Z (Height, m)")
    ax2.view_init(elev=30, azim=-55)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    print(f"✅ 3D Phenotyping result image saved: {save_path}")
    plt.show()

if __name__ == "__main__":
    run_measurement()
