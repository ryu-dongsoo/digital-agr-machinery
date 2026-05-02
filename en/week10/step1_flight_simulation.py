"""
Week 10 Lab Step 1: Drone Trajectory Visualization
- Render the waypoints generated in step 0 on a 2D plane
- Visually indicate Home point and RTL path
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Parameter Setup & Path Generation (Reused from step0)
field_width = 100.0   
field_height = 80.0   
swath_width = 4.0     

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

# 2. Trajectory Visualization using Matplotlib
plt.figure(figsize=(10, 8))

# Draw Field Boundary
plt.plot([-5, field_width+5, field_width+5, -5, -5], 
         [-5, -5, field_height+5, field_height+5, -5], 
         'k--', label='Field Boundary Margin')

# Draw Survey Grid Flight Path
plt.plot(x_coords, y_coords, 'b-', label='Flight Path (Survey Grid)', linewidth=1.5)
plt.scatter(x_coords, y_coords, c='red', s=20, label='Waypoints')

# Home Point
plt.scatter(x_coords[0], y_coords[0], c='green', marker='^', s=150, label='Home / Takeoff')

# RTL Path (Return To Launch)
plt.plot([x_coords[-1], x_coords[0]], [y_coords[-1], y_coords[0]], 'g--', label='RTL Path')

# Visualization Setup
plt.title(f"Agricultural Drone Auto Flight Path (Swath: {swath_width}m)")
plt.xlabel("X Coordinate (m)")
plt.ylabel("Y Coordinate (m)")
plt.legend(loc='upper right')
plt.grid(True)
plt.axis('equal') # Set aspect ratio to equal

plt.tight_layout()
output_dir = os.path.dirname(os.path.abspath(__file__))
output_img = os.path.join(output_dir, "waypoint_path.png")
plt.savefig(output_img, dpi=300)
print(f"✅ Visualization Image Saved: {output_img}")
# plt.show() # Commented out for server/automated environments
