"""
Week 10 Lab Step 4: Drone Flight Trajectory Animation
- Generate an animation (GIF) of the drone moving along the planned spraying path.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# 1. Parameter Setup & Path Generation
field_width = 100.0   
field_height = 80.0   
swath_width = 10.0     # Wide swath width (e.g., 10m) for faster animation

waypoints = []
y_coords = np.arange(0, field_height + swath_width, swath_width)
direction = 1 
for y in y_coords:
    if direction == 1:
        waypoints.append((0, y))
        waypoints.append((field_width, y))
    else:
        waypoints.append((field_width, y))
        waypoints.append((0, y))
    direction *= -1

# Separate x, y coordinates
x_coords = [p[0] for p in waypoints]
y_coords = [p[1] for p in waypoints]

# 2. Generate smooth trajectory via interpolation (for fluid animation)
num_frames_per_segment = 10
smooth_x = []
smooth_y = []
for i in range(len(x_coords)-1):
    x_segment = np.linspace(x_coords[i], x_coords[i+1], num_frames_per_segment)
    y_segment = np.linspace(y_coords[i], y_coords[i+1], num_frames_per_segment)
    smooth_x.extend(x_segment)
    smooth_y.extend(y_segment)

# Add RTL (Return To Launch) path
rtl_x = np.linspace(x_coords[-1], x_coords[0], 20)
rtl_y = np.linspace(y_coords[-1], y_coords[0], 20)
smooth_x.extend(rtl_x)
smooth_y.extend(rtl_y)

# 3. Matplotlib Animation Configuration
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-5, field_width+5)
ax.set_ylim(-5, field_height+5)

# Draw background (Field boundary and planned path)
ax.plot([-5, field_width+5, field_width+5, -5, -5], 
         [-5, -5, field_height+5, field_height+5, -5], 
         'k--', label='Field Boundary Margin')
ax.plot(x_coords, y_coords, 'gray', alpha=0.3, label='Planned Path')
ax.scatter(x_coords[0], y_coords[0], c='green', marker='^', s=150, label='Home / Takeoff')

# Objects to update during animation
line, = ax.plot([], [], 'b-', linewidth=2, label='Drone Trajectory')
drone_marker, = ax.plot([], [], 'ro', markersize=10, label='Drone Position')

ax.set_title(f"Drone Flight Animation (Swath: {swath_width}m)")
ax.set_xlabel("X Coordinate (m)")
ax.set_ylabel("Y Coordinate (m)")
ax.legend(loc='upper right')
ax.grid(True)
ax.set_aspect('equal')

def init():
    line.set_data([], [])
    drone_marker.set_data([], [])
    return line, drone_marker

def update(frame):
    x_data = smooth_x[:frame+1]
    y_data = smooth_y[:frame+1]
    line.set_data(x_data, y_data)
    
    if frame < len(smooth_x):
        drone_marker.set_data([smooth_x[frame]], [smooth_y[frame]])
        
    return line, drone_marker

# Create Animation
ani = animation.FuncAnimation(fig, update, frames=len(smooth_x),
                              init_func=init, blit=True, interval=50, repeat=False)

# Save result
output_dir = os.path.dirname(os.path.abspath(__file__))
output_gif = os.path.join(output_dir, "flight_animation.gif")
plt.tight_layout()

# Save as GIF using Pillow
ani.save(output_gif, writer='pillow', fps=20)
print(f"[SUCCESS] Animation GIF saved to: {output_gif}")

# Show animation window
plt.show()
