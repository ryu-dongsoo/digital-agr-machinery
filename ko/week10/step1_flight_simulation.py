"""
10주차 실습 Step 1: 드론 방제 궤적 시각화
- step0에서 생성한 웨이포인트를 2D 평면 위에 렌더링
- 이륙 지점(Home) 및 복귀 경로(RTL) 시각적 표시
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# 1. 방제 파라미터 설정 및 경로 생성 (step0 재사용)
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

# x, y 좌표 분리
x_coords = [p[0] for p in waypoints]
y_coords = [p[1] for p in waypoints]

# 2. Matplotlib을 이용한 경로 시각화
plt.figure(figsize=(10, 8))

# 농지 경계선(Bounding Box) 그리기
plt.plot([-5, field_width+5, field_width+5, -5, -5], 
         [-5, -5, field_height+5, field_height+5, -5], 
         'k--', label='Field Boundary Margin')

# 지그재그 방제 경로 그리기
plt.plot(x_coords, y_coords, 'b-', label='Flight Path (Survey Grid)', linewidth=1.5)
plt.scatter(x_coords, y_coords, c='red', s=20, label='Waypoints')

# 시작 지점 (Home/Takeoff)
plt.scatter(x_coords[0], y_coords[0], c='green', marker='^', s=150, label='Home / Takeoff')

# 복귀 경로 (RTL: Return To Launch) 점선 표시
plt.plot([x_coords[-1], x_coords[0]], [y_coords[-1], y_coords[0]], 'g--', label='RTL Path')

# 시각화 설정
plt.title(f"Agricultural Drone Auto Flight Path (Swath: {swath_width}m)")
plt.xlabel("X Coordinate (m)")
plt.ylabel("Y Coordinate (m)")
plt.legend(loc='upper right')
plt.grid(True)
plt.axis('equal') # X, Y 축 비율 동일하게 설정

plt.tight_layout()
output_dir = os.path.dirname(os.path.abspath(__file__))
output_img = os.path.join(output_dir, "waypoint_path.png")
plt.savefig(output_img, dpi=300)
print(f"[SUCCESS] 시각화 이미지 저장 완료: {output_img}")
# plt.show() # 서버/자동화 환경을 위해 주석 처리
