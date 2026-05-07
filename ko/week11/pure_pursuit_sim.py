"""
11주차 실습: 자율주행 경로 추종 시뮬레이션 (Pure Pursuit)
- 전방 주시 거리(Ld) 튜닝에 따른 트랙터 조향 성능 분석
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# --- 1. 시뮬레이션 파라미터 설정 ---
dt = 0.1         # 시뮬레이션 시간 간격 [s]
WB = 2.5         # 트랙터 축간 거리 (Wheel Base) [m]
v = 2.0          # 트랙터 주행 속도 [m/s]
Ld = 2.0         # 전방 주시 거리 (Look-ahead distance) [m]  <-- 튜닝 포인트!
MAX_STEER = math.radians(30.0)  # 최대 조향각 [rad]

# --- 2. 트랙터 상태(State) 클래스 ---
class State:
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v

def update_state(state, delta):
    """ Bicycle Kinematic Model을 이용한 상태 업데이트 """
    # 조향각 제한
    delta = np.clip(delta, -MAX_STEER, MAX_STEER)
    
    state.x += state.v * math.cos(state.yaw) * dt
    state.y += state.v * math.sin(state.yaw) * dt
    state.yaw += state.v / WB * math.tan(delta) * dt
    return state

# --- 3. Pure Pursuit 제어 알고리즘 ---
def pure_pursuit_control(state, cx, cy, pind):
    """
    현재 상태와 목표 경로(cx, cy)를 받아 목표점 탐색 후 조향각(delta) 반환
    """
    # 3.1. 현재 위치에서 가장 가까운 경로점(ind) 찾기
    dx = [state.x - icx for icx in cx]
    dy = [state.y - icy for icy in cy]
    d = np.hypot(dx, dy)
    target_ind = np.argmin(d)
    
    # 3.2. 전방 주시 거리(Ld)를 만족하는 목표점 찾기
    L = 0.0
    while L < Ld and target_ind < len(cx) - 1:
        dx_val = cx[target_ind + 1] - cx[target_ind]
        dy_val = cy[target_ind + 1] - cy[target_ind]
        L += math.hypot(dx_val, dy_val)
        target_ind += 1
        
    # 3.3. 조향각(delta) 계산
    tx = cx[target_ind]
    ty = cy[target_ind]
    
    alpha = math.atan2(ty - state.y, tx - state.x) - state.yaw
    delta = math.atan2(2.0 * WB * math.sin(alpha), Ld)
    
    return delta, target_ind

# --- 4. 메인 시뮬레이션 루프 ---
def main():
    # S자 형태의 가상 경로(Waypoint) 생성
    cx = np.arange(0, 50, 0.5)
    cy = [math.sin(ix / 5.0) * (ix / 2.0) for ix in cx]
    
    # 트랙터 초기 상태 설정
    state = State(x=0.0, y=-3.0, yaw=0.0, v=v)
    
    x_hist, y_hist = [], []
    target_ind = 0
    
    plt.figure(figsize=(10, 6))
    
    while target_ind < len(cx) - 1:
        # 조향각 계산
        delta, target_ind = pure_pursuit_control(state, cx, cy, target_ind)
        
        # 트랙터 이동
        state = update_state(state, delta)
        
        x_hist.append(state.x)
        y_hist.append(state.y)
        
        # 실시간 시각화
        plt.cla()
        plt.plot(cx, cy, ".r", label="Target Path (Reference)")
        plt.plot(x_hist, y_hist, "-b", label="Tractor Trajectory")
        plt.plot(cx[target_ind], cy[target_ind], "xg", label="Look-ahead Target")
        
        # 트랙터 그리기 (단순화된 사각형)
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
        outline = (Rot @ outline).T + [state.x, state.y]
        plt.plot(outline[:, 0], outline[:, 1], "-k")
        
        plt.title(f"Pure Pursuit Control (Ld = {Ld}m, v = {v}m/s)")
        plt.xlabel("X [m]")
        plt.ylabel("Y [m]")
        plt.legend(loc="upper left")
        plt.grid(True)
        plt.axis("equal")
        plt.pause(0.01)
        
    plt.show()

if __name__ == '__main__':
    main()
