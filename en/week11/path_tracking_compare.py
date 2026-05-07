"""
Week 11 Lab: Autonomous Driving Path Tracking Simulation (Pure Pursuit vs Stanley)
- Simultaneous comparison of two control algorithms
- Animation playback speed increased to 3x
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# --- 1. Simulation Parameters ---
dt = 0.1         # Simulation time step [s]
WB = 2.5         # Tractor Wheel Base [m]
v = 2.0          # Tractor speed [m/s]

# Pure Pursuit Parameter
Ld = 2.0         # Look-ahead distance [m]

# Stanley Parameter
k = 0.5          # Steering Gain

MAX_STEER = math.radians(30.0)  # Maximum steering angle [rad]

class State:
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v

def update_state(state, delta):
    delta = np.clip(delta, -MAX_STEER, MAX_STEER)
    state.x += state.v * math.cos(state.yaw) * dt
    state.y += state.v * math.sin(state.yaw) * dt
    state.yaw += state.v / WB * math.tan(delta) * dt
    state.yaw = (state.yaw + math.pi) % (2 * math.pi) - math.pi
    return state

def normalize_angle(angle):
    return (angle + math.pi) % (2 * math.pi) - math.pi

def pure_pursuit_control(state, cx, cy, pind):
    dx = [state.x - icx for icx in cx]
    dy = [state.y - icy for icy in cy]
    d = np.hypot(dx, dy)
    target_ind = np.argmin(d)
    
    L = 0.0
    while L < Ld and target_ind < len(cx) - 1:
        dx_val = cx[target_ind + 1] - cx[target_ind]
        dy_val = cy[target_ind + 1] - cy[target_ind]
        L += math.hypot(dx_val, dy_val)
        target_ind += 1
        
    tx = cx[target_ind]
    ty = cy[target_ind]
    
    alpha = math.atan2(ty - state.y, tx - state.x) - state.yaw
    delta = math.atan2(2.0 * WB * math.sin(alpha), Ld)
    
    return delta, target_ind

def stanley_control(state, cx, cy, cyaw, pind):
    fx = state.x + WB * math.cos(state.yaw)
    fy = state.y + WB * math.sin(state.yaw)
    
    dx = [fx - icx for icx in cx]
    dy = [fy - icy for icy in cy]
    d = np.hypot(dx, dy)
    target_ind = np.argmin(d)
    
    front_axle_vec = [-math.cos(state.yaw + math.pi/2), -math.sin(state.yaw + math.pi/2)]
    error_front_axle = np.dot([dx[target_ind], dy[target_ind]], front_axle_vec)
    
    theta_e = normalize_angle(cyaw[target_ind] - state.yaw)
    theta_d = math.atan2(k * error_front_axle, state.v)
    
    delta = theta_e + theta_d
    return delta, target_ind

def draw_tractor(state, color, label):
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
    outline = (Rot @ outline).T + [state.x + (WB/2)*math.cos(state.yaw), state.y + (WB/2)*math.sin(state.yaw)]
    plt.plot(outline[:, 0], outline[:, 1], color, label=label, linewidth=2)

def main():
    # S-curve path with slightly more curvature to make differences obvious
    cx = np.arange(0, 50, 0.5)
    cy = [math.sin(ix / 4.0) * (ix / 2.0) for ix in cx]
    
    cyaw = []
    for i in range(len(cx) - 1):
        cyaw.append(math.atan2(cy[i+1] - cy[i], cx[i+1] - cx[i]))
    cyaw.append(cyaw[-1])
    
    # Initial state for both tractors
    state_pp = State(x=0.0, y=-3.0, yaw=0.0, v=v)
    state_st = State(x=0.0, y=-3.0, yaw=0.0, v=v)
    
    x_hist_pp, y_hist_pp = [], []
    x_hist_st, y_hist_st = [], []
    
    target_ind_pp = 0
    target_ind_st = 0
    
    plt.figure(figsize=(12, 7))
    
    step = 0
    while target_ind_pp < len(cx) - 1 or target_ind_st < len(cx) - 1:
        
        # Pure Pursuit control
        if target_ind_pp < len(cx) - 1:
            delta_pp, target_ind_pp = pure_pursuit_control(state_pp, cx, cy, target_ind_pp)
            state_pp = update_state(state_pp, delta_pp)
            x_hist_pp.append(state_pp.x)
            y_hist_pp.append(state_pp.y)
            
        # Stanley control
        if target_ind_st < len(cx) - 1:
            delta_st, target_ind_st = stanley_control(state_st, cx, cy, cyaw, target_ind_st)
            state_st = update_state(state_st, delta_st)
            x_hist_st.append(state_st.x)
            y_hist_st.append(state_st.y)
            
        # 3x Animation Speed: Render every 3 steps
        if step % 3 == 0:
            plt.cla()
            plt.plot(cx, cy, ".r", label="Target Path (Reference)")
            
            plt.plot(x_hist_pp, y_hist_pp, "-b", label="Pure Pursuit Trajectory", alpha=0.5)
            plt.plot(x_hist_st, y_hist_st, "-g", label="Stanley Trajectory", alpha=0.5)
            
            draw_tractor(state_pp, "-b", "Tractor (Pure Pursuit)")
            draw_tractor(state_st, "-g", "Tractor (Stanley)")
            
            plt.title(f"Path Tracking Comparison (3x Speed)\nPure Pursuit ($L_d$={Ld}) vs Stanley ($k$={k})")
            plt.xlabel("X [m]")
            plt.ylabel("Y [m]")
            plt.legend(loc="upper left")
            plt.grid(True)
            plt.axis("equal")
            plt.pause(0.001)
            
        step += 1
        
    plt.show()

if __name__ == '__main__':
    main()
