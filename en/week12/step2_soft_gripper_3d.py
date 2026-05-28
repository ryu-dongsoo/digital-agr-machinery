"""
step2_soft_gripper_3d.py — Interactive 3D Soft Gripper Simulation

Three soft fingers placed at 120-degree intervals extend in 3D space 
toward a spherical fruit (target), bending inward according to 
the air pressure to wrap around the fruit. Adjustable via sliders.

Finger operation principle:
  - Fingers extend in the X+ direction (forward) from the gripper base.
  - Each finger is placed at 120-degree intervals in the YZ plane (gap radius).
  - Increasing pressure -> Fingers bend inward toward the central axis (fruit direction).

Sliders:
  - Pressure: Air pressure (bending degree)
  - Fruit X: Front/back position of the fruit
  - Gripper X: Front/back position of the gripper base
  - Finger Gap: Distance between the finger start point and the central axis

Dependencies: numpy, matplotlib (no additional packages required)
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider


# ──────────────────────────────────────────────
# 1. 3D Soft Finger Curve Generation
# ──────────────────────────────────────────────
def generate_finger_3d(pressure, gripper_x, gap, theta):
    """
    Generates coordinates for a 3D soft finger curve.

    Fingers extend in the X direction (forward) and bend inward 
    toward the central axis (X-axis) according to pressure.

    :param pressure:  Input air pressure (0.0 ~ 1.0)
    :param gripper_x: Gripper base X coordinate
    :param gap:       Radial distance of finger starting point from the central axis
    :param theta:     Placement angle in the YZ plane (radians)
    :return: (x, y, z) coordinate arrays
    """
    length = 0.7
    n_seg = 30
    seg_len = length / n_seg

    # Max curvature — about 150 degrees bending (inward) at pressure 1.0
    max_k = np.pi / length * 0.85
    k = pressure * max_k

    # 2D curve generation: forward vs radial plane
    # forward = X-axis direction, radial = distance from central axis
    fwd = [0.0]     # X-axis cumulative path
    rad = [gap]     # Radial path (starts at gap, decreases inward)
    angle = 0.0

    for _ in range(n_seg):
        angle += k * seg_len
        fwd.append(fwd[-1] + seg_len * np.cos(angle))
        rad.append(rad[-1] - seg_len * np.sin(angle))

    fwd = np.array(fwd)
    rad = np.array(rad)

    # 3D transformation: forward → X-axis, radial → YZ plane (along theta angle)
    x = gripper_x + fwd
    y = rad * np.cos(theta)
    z = rad * np.sin(theta)

    return x, y, z


# ──────────────────────────────────────────────
# 2. Fruit (Sphere) Surface Generation
# ──────────────────────────────────────────────
def make_sphere(cx, cy, cz, r=0.15, res=20):
    u = np.linspace(0, 2 * np.pi, res)
    v = np.linspace(0, np.pi, res)
    sx = cx + r * np.outer(np.cos(u), np.sin(v))
    sy = cy + r * np.outer(np.sin(u), np.sin(v))
    sz = cz + r * np.outer(np.ones_like(u), np.cos(v))
    return sx, sy, sz


# ──────────────────────────────────────────────
# 3. Contact Detection
# ──────────────────────────────────────────────
def detect_contact(fx, fy, fz, fc, r=0.15):
    d = np.sqrt((fx - fc[0])**2 + (fy - fc[1])**2 + (fz - fc[2])**2)
    return d <= r


# ──────────────────────────────────────────────
# 4. Finger Placement Setup (120-degree intervals)
# ──────────────────────────────────────────────
#   Finger 1:  90 degrees (Top)
#   Finger 2: 210 degrees (Bottom-Left)
#   Finger 3: 330 degrees (Bottom-Right)
FINGER_THETAS  = [np.radians(90), np.radians(210), np.radians(330)]
FINGER_COLORS  = ['#e74c3c', '#27ae60', '#2980b9']
FINGER_LABELS  = ['Finger 1 (Top)', 'Finger 2 (Bot-L)', 'Finger 3 (Bot-R)']
CONTACT_COLORS = ['#f39c12', '#1abc9c', '#8e44ad']


# ──────────────────────────────────────────────
# 5. Visualization Setup
# ──────────────────────────────────────────────
fig = plt.figure(figsize=(10, 9))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.30)

# Initial values
init_p   = 0.3
init_fx  = 0.55
init_gx  = 0.0
init_gap = 0.18
fruit_r  = 0.12

# Render Fruit (Centered along X-axis: Y=0, Z=0)
fruit_center = [init_fx, 0.0, 0.0]
sx, sy, sz = make_sphere(*fruit_center, fruit_r, res=25)
fruit_surf = [ax.plot_surface(sx, sy, sz, color='#f1c40f', alpha=0.4, shade=True)]

# Gripper central axis guide line (dashed line along X-axis)
ax.plot([init_gx - 0.1, init_fx + 0.3], [0, 0], [0, 0],
        '--', color='gray', alpha=0.3, lw=1)

# Initialize finger, chamber, and contact point artists
finger_lines = []
chamber_lines = []
contact_artists = []

for i in range(3):
    xi, yi, zi = generate_finger_3d(init_p, init_gx, init_gap, FINGER_THETAS[i])

    line, = ax.plot(xi, yi, zi, '-', lw=8, color=FINGER_COLORS[i],
                    solid_capstyle='round', alpha=0.85, label=FINGER_LABELS[i])
    finger_lines.append(line)

    ch, = ax.plot(xi, yi, zi, '--', lw=1.5, color='white', alpha=0.4)
    chamber_lines.append(ch)

    cp, = ax.plot([], [], [], 'o', color=CONTACT_COLORS[i], markersize=7)
    contact_artists.append(cp)

# Render Gripper Base Ring (connecting the finger start points)
base_theta = np.linspace(0, 2 * np.pi, 60)
base_y = init_gap * np.cos(base_theta)
base_z = init_gap * np.sin(base_theta)
base_ring, = ax.plot(np.full_like(base_theta, init_gx), base_y, base_z,
                     '-', color='#7f8c8d', lw=2, alpha=0.6, label='Gripper Base')

info_text = ax.text2D(0.02, 0.95, "", transform=ax.transAxes,
                      fontsize=10, fontweight='bold', verticalalignment='top',
                      bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.85))

ax.set_xlim(-0.2, 1.0)
ax.set_ylim(-0.4, 0.4)
ax.set_zlim(-0.4, 0.4)
ax.set_xlabel('X (Forward)', fontsize=11)
ax.set_ylabel('Y', fontsize=11)
ax.set_zlabel('Z', fontsize=11)
ax.set_title("3D Tri-Finger Soft Gripper Simulation", fontsize=14, pad=15)
ax.legend(loc='upper right', fontsize=8)
ax.view_init(elev=20, azim=-55)


# ──────────────────────────────────────────────
# 6. Sliders
# ──────────────────────────────────────────────
ax_p   = plt.axes([0.20, 0.20, 0.60, 0.02])
ax_fx  = plt.axes([0.20, 0.16, 0.60, 0.02])
ax_gx  = plt.axes([0.20, 0.12, 0.60, 0.02])
ax_gap = plt.axes([0.20, 0.08, 0.60, 0.02])

s_p   = Slider(ax_p,   'Pressure',   0.0,  1.0,  valinit=init_p)
s_fx  = Slider(ax_fx,  'Fruit X',    0.2,  0.9,  valinit=init_fx)
s_gx  = Slider(ax_gx,  'Gripper X', -0.2,  0.4,  valinit=init_gx)
s_gap = Slider(ax_gap, 'Finger Gap', 0.05,  0.35, valinit=init_gap)


# ──────────────────────────────────────────────
# 7. Update Callback
# ──────────────────────────────────────────────
def update(val):
    p   = s_p.val
    fx  = s_fx.val
    gx  = s_gx.val
    gap = s_gap.val
    fc  = [fx, 0.0, 0.0]

    total_contact = 0

    for i in range(3):
        xi, yi, zi = generate_finger_3d(p, gx, gap, FINGER_THETAS[i])

        finger_lines[i].set_data_3d(xi, yi, zi)
        chamber_lines[i].set_data_3d(xi, yi, zi)
        finger_lines[i].set_alpha(0.5 + 0.5 * p)

        # Detect contact
        mi = detect_contact(xi, yi, zi, fc, fruit_r)
        contact_artists[i].set_data_3d(xi[mi], yi[mi], zi[mi])
        total_contact += int(np.sum(mi))

    # Update base ring
    base_ring.set_data_3d(np.full(60, gx),
                          gap * np.cos(base_theta),
                          gap * np.sin(base_theta))

    # Redraw fruit surface
    fruit_surf[0].remove()
    nsx, nsy, nsz = make_sphere(*fc, fruit_r, res=25)
    fruit_surf[0] = ax.plot_surface(nsx, nsy, nsz, color='#f1c40f', alpha=0.4, shade=True)

    contact_str = f"Contact: {total_contact} pts" if total_contact > 0 else "Contact: No"

    info_text.set_text(
        f"Pressure: {p:.2f}\n"
        f"Bending: {p * 153:.0f}°\n"
        f"Fruit X: {fx:.2f}\n"
        f"Gripper X: {gx:.2f}\n"
        f"Gap: {gap:.2f}\n"
        f"{contact_str}"
    )

    fig.canvas.draw_idle()


s_p.on_changed(update)
s_fx.on_changed(update)
s_gx.on_changed(update)
s_gap.on_changed(update)

# Initial update call
update(None)

plt.show()
