"""
Step 1: Tractor LiDAR Scanning Simulation
==========================================
Animated visualization of a tractor-mounted LiDAR scanning an orchard,
building a 3D Point Cloud in real time.

Learning Objectives:
  - Intuitively experience the LiDAR Time-of-Flight (ToF) principle
  - Visually understand that each point in a Point Cloud is one laser reflection
  - Grasp the SLAM concept: 3D map progressively built as the tractor moves
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import os

# ============================================================
# 1. Virtual Orchard Environment Generation
# ============================================================
def create_orchard_environment():
    """
    Generates a regularly planted orchard (5 cols x 4 rows = 20 trees)
    with flat ground data. Each tree is modeled as a cone-shaped canopy
    with a cylindrical trunk.
    """
    all_pts = []
    tree_centers = []
    
    for row in range(4):
        for col in range(5):
            cx = col * 4.0 + 2.0
            cy = row * 5.0 + 2.5
            
            # Random variation per tree (realistic)
            tree_h = np.random.uniform(3.5, 5.5)
            canopy_r = np.random.uniform(1.2, 2.0)
            
            tree_centers.append((cx, cy, tree_h, canopy_r))
            
            # Trunk (cylinder, height 0-1.5m)
            n_trunk = 200
            trunk_h = np.random.uniform(0, 1.5, n_trunk)
            trunk_angle = np.random.uniform(0, 2*np.pi, n_trunk)
            trunk_r = 0.15
            trunk_x = cx + trunk_r * np.cos(trunk_angle)
            trunk_y = cy + trunk_r * np.sin(trunk_angle)
            all_pts.append(np.column_stack((trunk_x, trunk_y, trunk_h)))
            
            # Canopy (cone, height 1.5m to tree_h)
            n_canopy = 800
            canopy_z = np.random.uniform(1.5, tree_h, n_canopy)
            frac = (canopy_z - 1.5) / (tree_h - 1.5)
            local_r = canopy_r * (1.0 - frac * 0.8)
            canopy_angle = np.random.uniform(0, 2*np.pi, n_canopy)
            canopy_x = cx + local_r * np.cos(canopy_angle) + np.random.normal(0, 0.05, n_canopy)
            canopy_y = cy + local_r * np.sin(canopy_angle) + np.random.normal(0, 0.05, n_canopy)
            all_pts.append(np.column_stack((canopy_x, canopy_y, canopy_z)))
    
    # Ground plane (Z ≈ 0)
    n_ground = 3000
    gx = np.random.uniform(-1, 22, n_ground)
    gy = np.random.uniform(-1, 22, n_ground)
    gz = np.random.normal(0, 0.05, n_ground)
    all_pts.append(np.column_stack((gx, gy, gz)))
    
    world_pts = np.vstack(all_pts)
    return world_pts, tree_centers


# ============================================================
# 2. LiDAR Scanning Simulation (Tractor Movement + Beam Emission)
# ============================================================
def simulate_lidar_scan(world_pts, tractor_pos, scan_range=8.0):
    """
    Returns points within the LiDAR scan range from the tractor's current position.
    Real LiDAR measures distance via ToF; this simulation uses Euclidean distance.
    """
    tx, ty = tractor_pos
    dx = world_pts[:, 0] - tx
    dy = world_pts[:, 1] - ty
    dist = np.sqrt(dx**2 + dy**2)
    
    mask = dist < scan_range
    scanned = world_pts[mask]
    
    return scanned


# ============================================================
# 3. Animation Execution
# ============================================================
def run_animation():
    print("🚜 Starting Tractor LiDAR Scanning Simulation...")
    print("   Watch as the 3D Point Cloud is built in real time while the tractor drives through the orchard.")
    
    world_pts, tree_centers = create_orchard_environment()
    
    # Tractor path: drive along orchard rows
    path_y_fwd = np.linspace(-1, 22, 30)
    path_y_rev = np.linspace(22, -1, 30)
    
    path1_x = np.full_like(path_y_fwd, 10.0)
    path1 = np.column_stack((path1_x, path_y_fwd))
    
    path2_x = np.full_like(path_y_rev, 6.0)
    path2 = np.column_stack((path2_x, path_y_rev))
    
    tractor_path = np.vstack((path1, path2))
    n_frames = len(tractor_path)
    
    accumulated_pts = np.empty((0, 3))
    
    fig = plt.figure(figsize=(14, 6))
    
    # Left: 2D Top View
    ax1 = fig.add_subplot(121)
    ax1.set_xlim(-2, 24)
    ax1.set_ylim(-2, 24)
    ax1.set_aspect('equal')
    ax1.set_title("Top View: Tractor Path & LiDAR Scan")
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Y (m)")
    ax1.set_facecolor('#2a2a2a')
    
    for cx, cy, th, cr in tree_centers:
        tree_circle = plt.Circle((cx, cy), cr, color='green', alpha=0.3)
        ax1.add_patch(tree_circle)
        ax1.plot(cx, cy, 'g^', markersize=4)
    
    ax1.plot(tractor_path[:, 0], tractor_path[:, 1], '--', color='gray', alpha=0.3, linewidth=1)
    
    tractor_dot, = ax1.plot([], [], 'rs', markersize=10, label='Tractor')
    scan_circle = plt.Circle((0, 0), 8.0, color='yellow', fill=False, linewidth=1.5, linestyle='--', alpha=0.6)
    ax1.add_patch(scan_circle)
    scan_pts_2d, = ax1.plot([], [], '.', color='cyan', markersize=0.5, alpha=0.3)
    ax1.legend(loc='upper right', fontsize=8)
    
    # Right: 3D Accumulated Point Cloud
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_xlim(-2, 24)
    ax2.set_ylim(-2, 24)
    ax2.set_zlim(-1, 7)
    ax2.set_title("Accumulated 3D Point Cloud")
    ax2.set_xlabel("X (m)")
    ax2.set_ylabel("Y (m)")
    ax2.set_zlabel("Z (Height, m)")
    ax2.view_init(elev=25, azim=-60)
    
    info_text = ax1.text(0.02, 0.98, '', transform=ax1.transAxes, 
                         fontsize=9, verticalalignment='top', color='white',
                         bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
    
    def update(frame):
        nonlocal accumulated_pts
        
        tx, ty = tractor_path[frame]
        scanned = simulate_lidar_scan(world_pts, (tx, ty), scan_range=8.0)
        
        if len(scanned) > 500:
            idx = np.random.choice(len(scanned), 500, replace=False)
            scanned = scanned[idx]
        accumulated_pts = np.vstack((accumulated_pts, scanned))
        
        tractor_dot.set_data([tx], [ty])
        scan_circle.center = (tx, ty)
        scan_pts_2d.set_data(accumulated_pts[:, 0], accumulated_pts[:, 1])
        
        ax2.cla()
        ax2.set_xlim(-2, 24)
        ax2.set_ylim(-2, 24)
        ax2.set_zlim(-1, 7)
        ax2.set_xlabel("X (m)")
        ax2.set_ylabel("Y (m)")
        ax2.set_zlabel("Z (m)")
        
        z = accumulated_pts[:, 2]
        z_norm = (z - z.min()) / (z.max() - z.min() + 1e-6)
        
        show_step = max(1, len(accumulated_pts) // 15000)
        ax2.scatter(accumulated_pts[::show_step, 0], 
                    accumulated_pts[::show_step, 1], 
                    accumulated_pts[::show_step, 2], 
                    c=z_norm[::show_step], cmap='jet', s=0.5, alpha=0.6)
        
        ax2.scatter([tx], [ty], [0], c='red', s=80, marker='s', edgecolors='white', zorder=10)
        
        ax2.set_title(f"Accumulated 3D Point Cloud ({len(accumulated_pts):,} pts)")
        ax2.view_init(elev=25, azim=-60 + frame * 0.5)
        
        info_text.set_text(
            f"Frame: {frame+1}/{n_frames}\n"
            f"Tractor: ({tx:.1f}, {ty:.1f})m\n"
            f"Total Points: {len(accumulated_pts):,}"
        )
        
        return tractor_dot, scan_circle, scan_pts_2d, info_text
    
    ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=120, blit=False, repeat=False)
    
    plt.tight_layout()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step1_result.png")
    
    def on_finish(event=None):
        fig.savefig(save_path, dpi=200, bbox_inches='tight')
        print(f"✅ LiDAR scanning simulation result saved: {save_path}")
    
    fig.canvas.mpl_connect('close_event', on_finish)
    
    print("   (Close the window to auto-save the final result image)")
    plt.show()
    
    npy_path = os.path.join(base_dir, "scanned_orchard.npy")
    np.save(npy_path, accumulated_pts)
    print(f"✅ Accumulated Point Cloud saved: {npy_path} ({len(accumulated_pts):,} points)")
    
    return accumulated_pts

if __name__ == "__main__":
    run_animation()
