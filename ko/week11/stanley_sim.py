"""
11주차 실습: 자율주행 경로 추종 시뮬레이션 (Stanley Method)
- 전륜 중심(Front Axle) 기준 횡방향 오차(CTE) 및 헤딩 오차 비례 제어
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# --- 1. 시뮬레이션 파라미터 설정 ---
dt = 0.1         # 시뮬레이션 시간 간격 [s]
WB = 2.5         # 트랙터 축간 거리 (Wheel Base) [m]
v = 2.0          # 트랙터 주행 속도 [m/s]
k = 0.5          # 조향 게인 (Steering Gain) <-- 튜닝 포인트!
MAX_STEER = math.radians(30.0)  # 최대 조향각 [rad]

# --- 2. 트랙터 상태(State) 클래스 ---
class State:
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v

def update_state(state, delta):
    """ Bicycle Kinematic Model 업데이트 """
    delta = np.clip(delta, -MAX_STEER, MAX_STEER)
    state.x += state.v * math.cos(state.yaw) * dt
    state.y += state.v * math.sin(state.yaw) * dt
    state.yaw += state.v / WB * math.tan(delta) * dt
    # yaw 각도 정규화 (-pi ~ pi)
    state.yaw = (state.yaw + math.pi) % (2 * math.pi) - math.pi
    return state

def normalize_angle(angle):
    return (angle + math.pi) % (2 * math.pi) - math.pi

# --- 3. Stanley 제어 알고리즘 ---
def stanley_control(state, cx, cy, cyaw, pind):
    """
    현재 상태와 목표 경로를 받아 Stanley 기반 조향각(delta) 반환
    """
    # 3.1. 트랙터 전륜(Front Axle) 중심 좌표 계산
    fx = state.x + WB * math.cos(state.yaw)
    fy = state.y + WB * math.sin(state.yaw)
    
    # 3.2. 가장 가까운 경로점 찾기 (전륜 기준)
    dx = [fx - icx for icx in cx]
    dy = [fy - icy for icy in cy]
    d = np.hypot(dx, dy)
    target_ind = np.argmin(d)
    
    # 3.3. 횡방향 오차 (Cross-Track Error, CTE) 계산
    # 경로 벡터와 차량-목표점 벡터의 외적을 통해 오차 방향 결정
    front_axle_vec = [-math.cos(state.yaw + math.pi/2), -math.sin(state.yaw + math.pi/2)]
    error_front_axle = np.dot([dx[target_ind], dy[target_ind]], front_axle_vec)
    
    # 3.4. 헤딩 오차 (Heading Error) 계산
    theta_e = normalize_angle(cyaw[target_ind] - state.yaw)
    
    # 3.5. 횡방향 오차에 의한 조향각 계산
    theta_d = math.atan2(k * error_front_axle, state.v)
    
    # 3.6. 총 조향각 (delta = theta_e + theta_d)
    delta = theta_e + theta_d
    
    return delta, target_ind

# --- 4. 메인 시뮬레이션 루프 (애니메이션 포함) ---
def main():
    # S자 형태의 가상 경로(Waypoint) 생성
    cx = np.arange(0, 50, 0.5)
    cy = [math.sin(ix / 5.0) * (ix / 2.0) for ix in cx]
    
    # 경로의 각 점에서의 각도(yaw) 계산
    cyaw = []
    for i in range(len(cx) - 1):
        cyaw.append(math.atan2(cy[i+1] - cy[i], cx[i+1] - cx[i]))
    cyaw.append(cyaw[-1])
    
    # 트랙터 초기 상태 설정
    state = State(x=0.0, y=-3.0, yaw=0.0, v=v)
    
    x_hist, y_hist = [], []
    target_ind = 0
    
    plt.figure(figsize=(10, 6))
    
    while target_ind < len(cx) - 1:
        delta, target_ind = stanley_control(state, cx, cy, cyaw, target_ind)
        state = update_state(state, delta)
        
        x_hist.append(state.x)
        y_hist.append(state.y)
        
        # --- 실시간 애니메이션 플롯 ---
        plt.cla()
        plt.plot(cx, cy, ".r", label="Target Path (Reference)")
        plt.plot(x_hist, y_hist, "-b", label="Tractor Trajectory")
        
        # 전륜 중심 시각화
        fx = state.x + WB * math.cos(state.yaw)
        fy = state.y + WB * math.sin(state.yaw)
        plt.plot(fx, fy, "xg", label="Front Axle Center")
        
        # 트랙터 외형 그리기 (후륜 중심 기준)
        length = 3.0
        width = 1.5
        outline = np.array([
            [-length/2, length/2, length/2, -length/2, -length/2],
            [width/2, width/2, -width/2, -width/2, width/2]
        ])
        Rot = np.array([
            [math.cos(state.yaw), -math.sin(state.yaw)],
            [math.sin(state.yaw),  math.cos(state.yaw)]
        ])
        # 직사각형 중심을 차량 중심점(후륜에서 WB/2 앞쪽)으로 이동
        outline = (Rot @ outline).T + [state.x + (WB/2)*math.cos(state.yaw), state.y + (WB/2)*math.sin(state.yaw)] 
        plt.plot(outline[:, 0], outline[:, 1], "-k")
        
        plt.title(f"Stanley Method Control (k = {k}, v = {v}m/s)")
        plt.xlabel("X [m]")
        plt.ylabel("Y [m]")
        plt.legend(loc="upper left")
        plt.grid(True)
        plt.axis("equal")
        plt.pause(0.01) # 애니메이션 업데이트 간격
        
    plt.show()

if __name__ == '__main__':
    main()
