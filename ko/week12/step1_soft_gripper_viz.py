import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def simulate_soft_finger(pressure, start_pos=(0, 0)):
    """
    공압식 소프트 그리퍼(Pneu-Net)의 굽힘 변형 단순화 모델
    :param pressure: 입력 공압 (0.0 ~ 1.0)
    :param start_pos: 손가락 시작 좌표 (x, y)
    :return: 손가락 마디 좌표 (x, y)
    """
    # 손가락의 기본 길이 및 마디 수
    length = 1.0
    num_segments = 20
    segment_len = length / num_segments
    
    # 압력에 따른 곡률(Curvature) 계산 (단순 선형 모델)
    # 압력이 높을수록 곡률 반경이 작아짐 (더 많이 굽힘)
    max_curvature = np.pi / length * 1.5  # 최대 270도 정도 굽힘
    k = pressure * max_curvature
    
    x = [start_pos[0]]
    y = [start_pos[1]]
    angle = 0
    
    for i in range(num_segments):
        angle += k * segment_len
        x.append(x[-1] + segment_len * np.cos(angle))
        y.append(y[-1] + segment_len * np.sin(angle))
        
    return np.array(x), np.array(y)

# --- 시뮬레이션 설정 ---
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.35, left=0.15)

# 초기 설정값
initial_p = 0.2
initial_fruit_pos = (0.5, 0.5)
initial_gripper_pos = (0.0, 0.0)

x_coords, y_coords = simulate_soft_finger(initial_p, initial_gripper_pos)

# 손가락 라인 렌더링 (부드러운 실리콘 느낌을 위해 굵게 설정)
finger_line, = ax.plot(x_coords, y_coords, '-', lw=20, color='#e74c3c', solid_capstyle='round', alpha=0.8)
# 내부 공기 챔버 느낌의 라인
chamber_line, = ax.plot(x_coords, y_coords, '--', lw=2, color='white', alpha=0.5)

# 현재 상태 표시 텍스트
info_text = ax.text(0.05, 0.95, f"Bending: {initial_p*270:.1f}°", transform=ax.transAxes, 
                    fontsize=11, fontweight='bold', verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

# 가상의 과일 (Target)
fruit = plt.Circle(initial_fruit_pos, 0.15, color='#f1c40f', label='Fruit (Target)')
ax.add_artist(fruit)

# 접촉 지점 표시용 아티스트 (파란색 점)
contact_pts, = ax.plot([], [], 'o', color='#3498db', markersize=10, label='Contact Point', zorder=5)

ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_title("Pneumatic Soft Gripper Simulation (Adjustable Position)", fontsize=15, pad=20)

# 슬라이더 영역 정의 [left, bottom, width, height]
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
    
    # 그리퍼 업데이트
    new_x, new_y = simulate_soft_finger(p, (gx, gy))
    finger_line.set_data(new_x, new_y)
    chamber_line.set_data(new_x, new_y)
    
    # 과일 위치 업데이트
    fruit.set_center((fx, fy))
    
    # 접촉 지점 계산 (과일 원 안에 들어온 마디 확인)
    # 과일 반지름 0.15 + 손가락 두께 고려 (약간의 마진 추가 가능)
    distances = np.sqrt((new_x - fx)**2 + (new_y - fy)**2)
    contact_mask = distances <= 0.15
    contact_x = new_x[contact_mask]
    contact_y = new_y[contact_mask]
    contact_pts.set_data(contact_x, contact_y)
    
    is_contact = "Yes" if np.any(contact_mask) else "No"
    
    # 정보 텍스트 업데이트
    info_text.set_text(f"Bending: {p*270:.1f}°\nFruit: ({fx:.1f}, {fy:.1f})\nGripper: ({gx:.1f}, {gy:.1f})\nContact: {is_contact}")
    
    # 압력에 따라 색상 변경
    finger_line.set_alpha(0.5 + 0.5 * p)
    
    fig.canvas.draw_idle()

s_p.on_changed(update)
s_fx.on_changed(update)
s_fy.on_changed(update)
s_gx.on_changed(update)
s_gy.on_changed(update)

plt.legend(handles=[fruit, contact_pts], loc='upper right')
plt.show()
