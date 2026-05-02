"""
10주차 실습 Step 0: 농업용 드론 방제 웨이포인트(Waypoint) 생성 기초
- 가상의 농지 크기 및 방제 간격(Swath Width)을 기반으로 지그재그 궤적 생성
- 총 비행 거리 및 예상 소요 시간 계산
"""

import numpy as np

# 1. 방제 파라미터 설정
field_width = 100.0   # 농지 가로 길이 (m)
field_height = 80.0   # 농지 세로 길이 (m)
swath_width = 4.0     # 방제 간격 (m)
flight_speed = 5.0    # 비행 속도 (m/s)

print(f"--- 🚁 방제 파라미터 ---")
print(f"농지 면적: {field_width * field_height} ㎡")
print(f"방제 간격: {swath_width} m")
print(f"비행 속도: {flight_speed} m/s\n")

# 2. 지그재그(Grid) 웨이포인트 좌표 생성
waypoints = []
# (0, 0)에서 시작하여 Y축으로 이동하며 X축 왕복
y_coords = np.arange(0, field_height + swath_width, swath_width)

direction = 1 # 1: 정방향(0 -> width), -1: 역방향(width -> 0)
for y in y_coords:
    if direction == 1:
        waypoints.append((0, y))
        waypoints.append((field_width, y))
    else:
        waypoints.append((field_width, y))
        waypoints.append((0, y))
    direction *= -1 # 방향 전환

# 3. 비행 거리 및 소요 시간 계산
total_distance = 0.0
for i in range(1, len(waypoints)):
    p1 = waypoints[i-1]
    p2 = waypoints[i]
    # 유클리디안 거리 합산
    distance = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    total_distance += distance

# 이륙 지점 복귀(RTL) 거리 추가 (마지막 좌표에서 처음 좌표로)
rtl_distance = np.sqrt((waypoints[-1][0] - waypoints[0][0])**2 + (waypoints[-1][1] - waypoints[0][1])**2)
total_distance += rtl_distance

estimated_time = total_distance / flight_speed

print(f"--- 📊 예상 비행 데이터 ---")
print(f"생성된 웨이포인트 개수: {len(waypoints)} 개")
print(f"총 비행 거리(RTL 포함): {total_distance:.2f} m")
print(f"예상 소요 시간: {estimated_time:.2f} 초 ({estimated_time/60:.2f} 분)")
