import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def forward_kinematics(l1, l2, theta1, theta2):
    """
    2-DOF 평면 로봇 팔의 정기구학 연산
    :param l1: 첫 번째 링크 길이
    :param l2: 두 번째 링크 길이
    :param theta1: 첫 번째 관절 각도 (radian)
    :param theta2: 두 번째 관절 각도 (radian)
    :return: (x1, y1), (x2, y2) 좌표
    """
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    
    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)
    
    return (x1, y1), (x2, y2)

def inverse_kinematics(l1, l2, x, y):
    """
    2-DOF 평면 로봇 팔의 역기구학 연산 (Geometric Approach)
    :param l1: 첫 번째 링크 길이
    :param l2: 두 번째 링크 길이
    :param x: 목표 x 좌표
    :param y: 목표 y 좌표
    :return: theta1, theta2 (radian)
    """
    # 코사인 법칙을 이용한 theta2 계산
    cos_theta2 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    
    # 도달 불가능한 위치 체크
    if abs(cos_theta2) > 1:
        return None, None
    
    # Elbow down solution
    theta2 = np.arccos(cos_theta2)
    
    # theta1 계산
    theta1 = np.arctan2(y, x) - np.arctan2(l2 * np.sin(theta2), l1 + l2 * np.cos(theta2))
    
    return theta1, theta2

# --- 시뮬레이션 설정 ---
L1_init = 1.0
L2_init = 0.8

fig, ax = plt.subplots(figsize=(8, 9))
plt.subplots_adjust(bottom=0.3) # 슬라이더 공간 확보를 위해 여백 조정

(p1, p2) = forward_kinematics(L1_init, L2_init, np.deg2rad(45), np.deg2rad(45))

line, = ax.plot([0, p1[0], p2[0]], [0, p1[1], p2[1]], 'o-', lw=4, markersize=10, color='#2c3e50', label='Robot Arm')
target_dot, = ax.plot(p2[0], p2[1], 'ro', markersize=8, label='End-Effector')

# 작업 영역 가이드 라인 (최대 도달 거리)
max_dist = L1_init + L2_init
workspace_circle = plt.Circle((0, 0), max_dist, color='gray', fill=False, linestyle='--', alpha=0.3, label='Workspace Boundary')
ax.add_artist(workspace_circle)

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.grid(True, linestyle='--')
ax.set_title("2-DOF Agricultural Robot Arm Kinematics", fontsize=15, pad=20)
ax.set_aspect('equal')

# 슬라이더 위치 설정
ax_t1 = plt.axes([0.2, 0.20, 0.65, 0.03])
ax_t2 = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_l1 = plt.axes([0.2, 0.10, 0.65, 0.03])
ax_l2 = plt.axes([0.2, 0.05, 0.65, 0.03])

s_t1 = Slider(ax_t1, 'Theta 1 (deg)', -180, 180, valinit=45)
s_t2 = Slider(ax_t2, 'Theta 2 (deg)', -180, 180, valinit=45)
s_l1 = Slider(ax_l1, 'Link 1 Length', 0.1, 1.5, valinit=L1_init)
s_l2 = Slider(ax_l2, 'Link 2 Length', 0.1, 1.5, valinit=L2_init)

def update(val):
    t1 = np.deg2rad(s_t1.val)
    t2 = np.deg2rad(s_t2.val)
    l1 = s_l1.val
    l2 = s_l2.val
    
    (p1, p2) = forward_kinematics(l1, l2, t1, t2)
    line.set_data([0, p1[0], p2[0]], [0, p1[1], p2[1]])
    target_dot.set_data([p2[0]], [p2[1]])
    
    # 작업 영역 가이드 업데이트
    workspace_circle.set_radius(l1 + l2)
    
    fig.canvas.draw_idle()

s_t1.on_changed(update)
s_t2.on_changed(update)
s_l1.on_changed(update)
s_l2.on_changed(update)

ax.legend(loc='upper right')
plt.show()
