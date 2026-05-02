"""
10주차 실습 Step 4: 드론 방제 궤적 애니메이션
- 생성된 방제 경로를 따라 드론이 이동하는 모습을 애니메이션(GIF)으로 생성
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# 1. 방제 파라미터 설정 및 경로 생성
field_width = 100.0   
field_height = 80.0   
swath_width = 10.0     # 애니메이션 속도를 위해 간격을 넓게 설정 (예: 10m)

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

# x, y 좌표 분리
x_coords = [p[0] for p in waypoints]
y_coords = [p[1] for p in waypoints]

# 2. 보간을 통한 세부 이동 경로 생성 (애니메이션을 부드럽게 만들기 위함)
num_frames_per_segment = 10
smooth_x = []
smooth_y = []
for i in range(len(x_coords)-1):
    x_segment = np.linspace(x_coords[i], x_coords[i+1], num_frames_per_segment)
    y_segment = np.linspace(y_coords[i], y_coords[i+1], num_frames_per_segment)
    smooth_x.extend(x_segment)
    smooth_y.extend(y_segment)

# RTL(Return To Launch) 경로 추가
rtl_x = np.linspace(x_coords[-1], x_coords[0], 20)
rtl_y = np.linspace(y_coords[-1], y_coords[0], 20)
smooth_x.extend(rtl_x)
smooth_y.extend(rtl_y)

# 3. Matplotlib 애니메이션 설정
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-5, field_width+5)
ax.set_ylim(-5, field_height+5)

# 배경 그리기 (농지 경계선 및 전체 경로 희미하게)
ax.plot([-5, field_width+5, field_width+5, -5, -5], 
         [-5, -5, field_height+5, field_height+5, -5], 
         'k--', label='Field Boundary Margin')
ax.plot(x_coords, y_coords, 'gray', alpha=0.3, label='Planned Path')
ax.scatter(x_coords[0], y_coords[0], c='green', marker='^', s=150, label='Home / Takeoff')

# 애니메이션 갱신용 객체
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

# 애니메이션 생성
ani = animation.FuncAnimation(fig, update, frames=len(smooth_x),
                              init_func=init, blit=True, interval=50, repeat=False)

# 결과 저장
output_dir = os.path.dirname(os.path.abspath(__file__))
output_gif = os.path.join(output_dir, "flight_animation.gif")
plt.tight_layout()

# Pillow를 이용해 GIF로 저장
ani.save(output_gif, writer='pillow', fps=20)
print(f"[SUCCESS] 애니메이션 GIF 저장 완료: {output_gif}")

# 화면에 애니메이션 띄우기
plt.show()
