"""
Week 11 Lab: Autonomous Driving Path Tracking Simulation (Pure Pursuit)
- Analyzing tractor steering performance based on look-ahead distance (Ld) tuning
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# --- 1. Simulation Parameters ---
dt = 0.1         # Simulation time step [s]
WB = 2.5         # Tractor Wheel Base [m]
v = 2.0          # Tractor speed [m/s]
Ld = 2.0         # Look-ahead distance [m]  <-- Tuning point!
MAX_STEER = math.radians(30.0)  # Maximum steering angle [rad]

# --- 2. Tractor State Class ---
class State:
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v

def update_state(state, delta):
    """ Update state using Bicycle Kinematic Model """
    # Limit steering angle
    delta = np.clip(delta, -MAX_STEER, MAX_STEER)
    
    state.x += state.v * math.cos(state.yaw) * dt
    state.y += state.v * math.sin(state.yaw) * dt
    state.yaw += state.v / WB * math.tan(delta) * dt
    return state

# --- 3. Pure Pursuit Control Algorithm ---
def pure_pursuit_control(state, cx, cy, pind):
    """
    Search for target point using current state and reference path (cx, cy), then return steering angle (delta)
    """
    # 3.1. Find nearest path point index
    dx = [state.x - icx for icx in cx]
    dy = [state.y - icy for icy in cy]
    d = np.hypot(dx, dy)
    target_ind = np.argmin(d)
    
    # 3.2. Find target point satisfying Look-ahead distance (Ld)
    L = 0.0
    while L < Ld and target_ind < len(cx) - 1:
        dx_val = cx[target_ind + 1] - cx[target_ind]
        dy_val = cy[target_ind + 1] - cy[target_ind]
        L += math.hypot(dx_val, dy_val)
        target_ind += 1
        
    # 3.3. Calculate steering angle (delta)
    tx = cx[target_ind]
    ty = cy[target_ind]
    
    alpha = math.atan2(ty - state.y, tx - state.x) - state.yaw
    delta = math.atan2(2.0 * WB * math.sin(alpha), Ld)
    
    return delta, target_ind

# --- 4. Main Simulation Loop ---
def main():
    # Generate virtual S-curve reference path
    cx = np.arange(0, 50, 0.5)
    cy = [math.sin(ix / 5.0) * (ix / 2.0) for ix in cx]
    
    # Initialize tractor state
    state = State(x=0.0, y=-3.0, yaw=0.0, v=v)
    
    x_hist, y_hist = [], []
    target_ind = 0
    
    plt.figure(figsize=(10, 6))
    
    while target_ind < len(cx) - 1:
        # Calculate steering angle
        delta, target_ind = pure_pursuit_control(state, cx, cy, target_ind)
        
        # Move tractor
        state = update_state(state, delta)
        
        x_hist.append(state.x)
        y_hist.append(state.y)
        
        # Real-time visualization
        plt.cla()
        plt.plot(cx, cy, ".r", label="Target Path (Reference)")
        plt.plot(x_hist, y_hist, "-b", label="Tractor Trajectory")
        plt.plot(cx[target_ind], cy[target_ind], "xg", label="Look-ahead Target")
        
        # Draw simplified tractor rectangle
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
