import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def simulate_soft_finger(pressure, start_pos=(0, 0)):
    """
    Simplified model of bending deformation for a pneumatic soft gripper (Pneu-Net)
    :param pressure: Input air pressure (0.0 ~ 1.0)
    :param start_pos: Finger start coordinates (x, y)
    :return: Finger segment coordinates (x, y)
    """
    # Base finger length and number of segments
    length = 1.0
    num_segments = 20
    segment_len = length / num_segments
    
    # Calculate curvature based on pressure (simple linear model)
    # Higher pressure leads to a smaller curvature radius (more bending)
    max_curvature = np.pi / length * 1.5  # Max bending of about 270 degrees
    k = pressure * max_curvature
    
    x = [start_pos[0]]
    y = [start_pos[1]]
    angle = 0
    
    for _ in range(num_segments):
        angle += k * segment_len
        x.append(x[-1] + segment_len * np.cos(angle))
        y.append(y[-1] + segment_len * np.sin(angle))
        
    return np.array(x), np.array(y)

# --- Simulation Settings ---
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.35, left=0.15)

# Initial setting values
initial_p = 0.2
initial_fruit_pos = (0.5, 0.5)
initial_gripper_pos = (0.0, 0.0)

x_coords, y_coords = simulate_soft_finger(initial_p, initial_gripper_pos)

# Render finger line (set thick for a soft silicone feel)
finger_line, = ax.plot(x_coords, y_coords, '-', lw=20, color='#e74c3c', solid_capstyle='round', alpha=0.8)
# Line representing the internal air chambers
chamber_line, = ax.plot(x_coords, y_coords, '--', lw=2, color='white', alpha=0.5)

# Current state display text
info_text = ax.text(0.05, 0.95, f"Bending: {initial_p*270:.1f}°", transform=ax.transAxes, 
                    fontsize=11, fontweight='bold', verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

# Virtual Fruit (Target)
fruit = plt.Circle(initial_fruit_pos, 0.15, color='#f1c40f', label='Fruit (Target)')
ax.add_artist(fruit)

# Contact point display artist (blue dots)
contact_pts, = ax.plot([], [], 'o', color='#3498db', markersize=10, label='Contact Point', zorder=5)

ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_title("Pneumatic Soft Gripper Simulation (Adjustable Position)", fontsize=15, pad=20)

# Define slider areas [left, bottom, width, height]
ax_p = plt.axes([0.2, 0.22, 0.6, 0.02])
ax_fx = plt.axes([0.2, 0.17, 0.6, 0.02])
ax_fy = plt.axes([0.2, 0.12, 0.6, 0.02])
ax_gx = plt.axes([0.2, 0.07, 0.6, 0.02])
ax_gy = plt.axes([0.2, 0.02, 0.6, 0.02])

s_p = Slider(ax_p, 'Pressure', 0.0, 1.0, valinit=initial_p)
s_fx = Slider(ax_fx, 'Fruit X', -0.5, 1.5, valinit=initial_fruit_pos[0])
s_fy = Slider(ax_fy, 'Fruit Y', -0.5, 1.5, valinit=initial_fruit_pos[1])
s_gx = Slider(ax_gx, 'Gripper X', -0.5, 0.5, valinit=initial_gripper_pos[0])
s_gy = Slider(ax_gy, 'Gripper Y', -0.5, 0.5, valinit=initial_gripper_pos[1])

def update(val):
    p = s_p.val
    fx = s_fx.val
    fy = s_fy.val
    gx = s_gx.val
    gy = s_gy.val
    
    # Update gripper
    new_x, new_y = simulate_soft_finger(p, (gx, gy))
    finger_line.set_data(new_x, new_y)
    chamber_line.set_data(new_x, new_y)
    
    # Update fruit position
    fruit.set_center((fx, fy))
    
    # Calculate contact points (segments inside the fruit circle)
    # Fruit radius 0.15 + finger thickness consideration
    distances = np.sqrt((new_x - fx)**2 + (new_y - fy)**2)
    contact_mask = distances <= 0.15
    contact_x = new_x[contact_mask]
    contact_y = new_y[contact_mask]
    contact_pts.set_data(contact_x, contact_y)
    
    is_contact = "Yes" if np.any(contact_mask) else "No"
    
    # Update info text
    info_text.set_text(f"Bending: {p*270:.1f}°\nFruit: ({fx:.1f}, {fy:.1f})\nGripper: ({gx:.1f}, {gy:.1f})\nContact: {is_contact}")
    
    # Change alpha based on pressure
    finger_line.set_alpha(0.5 + 0.5 * p)
    
    fig.canvas.draw_idle()

s_p.on_changed(update)
s_fx.on_changed(update)
s_fy.on_changed(update)
s_gx.on_changed(update)
s_gy.on_changed(update)

plt.legend(handles=[fruit, contact_pts], loc='upper right')
plt.show()
