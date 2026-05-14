import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def simulate_soft_finger(pressure):
    """
    공압식 소프트 그리퍼(Pneu-Net)의 굽힘 변형 단순화 모델
    :param pressure: 입력 공압 (0.0 ~ 1.0)
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
    
    x = [0]
    y = [0]
    angle = 0
    
    for i in range(num_segments):
        angle += k * segment_len
        x.append(x[-1] + segment_len * np.cos(angle))
        y.append(y[-1] + segment_len * np.sin(angle))
        
    return np.array(x), np.array(y)

# --- 시뮬레이션 설정 ---
fig, ax = plt.subplots(figsize=(8, 7))
plt.subplots_adjust(bottom=0.25)

# 초기 압력 설정
initial_p = 0.2
x_coords, y_coords = simulate_soft_finger(initial_p)

# 손가락 라인 렌더링 (부드러운 실리콘 느낌을 위해 굵게 설정)
finger_line, = ax.plot(x_coords, y_coords, '-', lw=20, color='#e74c3c', solid_capstyle='round', alpha=0.8)
# 내부 공기 챔버 느낌의 라인
chamber_line, = ax.plot(x_coords, y_coords, '--', lw=2, color='white', alpha=0.5)

# 현재 굽힘 정도 표시 텍스트
info_text = ax.text(0.05, 0.95, f"Bending Degree: {initial_p*270:.1f}°", transform=ax.transAxes, 
                    fontsize=12, fontweight='bold', verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

# 가상의 과일 (Target)
fruit = plt.Circle((0.5, 0.5), 0.15, color='#f1c40f', label='Fruit (Target)')
ax.add_artist(fruit)

ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.0)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_title("Pneumatic Soft Gripper Bending Simulation", fontsize=15, pad=20)

# 슬라이더 추가
ax_p = plt.axes([0.2, 0.1, 0.65, 0.03])
s_p = Slider(ax_p, 'Air Pressure (0-1)', 0.0, 1.0, valinit=initial_p)

def update(val):
    p = s_p.val
    new_x, new_y = simulate_soft_finger(p)
    finger_line.set_data(new_x, new_y)
    chamber_line.set_data(new_x, new_y)
    
    # 정보 텍스트 업데이트
    info_text.set_text(f"Bending Degree: {p*270:.1f}°")
    
    # 압력에 따라 색상 변경 (진해짐)
    finger_line.set_alpha(0.5 + 0.5 * p)
    
    fig.canvas.draw_idle()

s_p.on_changed(update)

plt.legend(handles=[fruit], loc='upper right')
plt.show()
