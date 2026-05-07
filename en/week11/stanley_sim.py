"""
Week 11 Lab: Autonomous Driving Path Tracking Simulation (Stanley Method)
- Proportional control using Cross-Track Error (CTE) and Heading Error based on the Front Axle
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# --- 1. Simulation Parameters ---
dt = 0.1         # Simulation time step [s]
WB = 2.5         # Tractor Wheel Base [m]
v = 2.0          # Tractor speed [m/s]
k = 0.5          # Steering Gain <-- Tuning point!
MAX_STEER = math.radians(30.0)  # Maximum steering angle [rad]

# --- 2. Tractor State Class ---
class State:
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v

def update_state(state, delta):
    """ Bicycle Kinematic Model Update """
    delta = np.clip(delta, -MAX_STEER, MAX_STEER)
    state.x += state.v * math.cos(state.yaw) * dt
    state.y += state.v * math.sin(state.yaw) * dt
    state.yaw += state.v / WB * math.tan(delta) * dt
    # Normalize yaw angle (-pi to pi)
    state.yaw = (state.yaw + math.pi) % (2 * math.pi) - math.pi
    return state

def normalize_angle(angle):
    return (angle + math.pi) % (2 * math.pi) - math.pi

# --- 3. Stanley Control Algorithm ---
def stanley_control(state, cx, cy, cyaw, pind):
    """
    Calculate steering angle (delta) using Stanley method based on current state and reference path
    """
    # 3.1. Calculate Front Axle coordinates
    fx = state.x + WB * math.cos(state.yaw)
    fy = state.y + WB * math.sin(state.yaw)
    
    # 3.2. Find nearest path point from the front axle
    dx = [fx - icx for icx in cx]
    dy = [fy - icy for icy in cy]
    d = np.hypot(dx, dy)
    target_ind = np.argmin(d)
    
    # 3.3. Calculate Cross-Track Error (CTE)
    front_axle_vec = [-math.cos(state.yaw + math.pi/2), -math.sin(state.yaw + math.pi/2)]
    error_front_axle = np.dot([dx[target_ind], dy[target_ind]], front_axle_vec)
    
    # 3.4. Calculate Heading Error
    theta_e = normalize_angle(cyaw[target_ind] - state.yaw)
    
    # 3.5. Calculate steering angle from CTE
    theta_d = math.atan2(k * error_front_axle, state.v)
    
    # 3.6. Total steering angle
    delta = theta_e + theta_d
    
    return delta, target_ind

# --- 4. Main Simulation Loop (with Animation) ---
def main():
    # Generate virtual S-curve reference path
    cx = np.arange(0, 50, 0.5)
    cy = [math.sin(ix / 5.0) * (ix / 2.0) for ix in cx]
    
    # Calculate yaw angles for the reference path
    cyaw = []
    for i in range(len(cx) - 1):
        cyaw.append(math.atan2(cy[i+1] - cy[i], cx[i+1] - cx[i]))
    cyaw.append(cyaw[-1])
    
    # Initialize tractor state
    state = State(x=0.0, y=-3.0, yaw=0.0, v=v)
    
    x_hist, y_hist = [], []
    target_ind = 0
    
    plt.figure(figsize=(10, 6))
    
    while target_ind < len(cx) - 1:
        delta, target_ind = stanley_control(state, cx, cy, cyaw, target_ind)
        state = update_state(state, delta)
        
        x_hist.append(state.x)
        y_hist.append(state.y)
        
        # --- Real-time Animation Plot ---
        plt.cla()
        plt.plot(cx, cy, ".r", label="Target Path (Reference)")
        plt.plot(x_hist, y_hist, "-b", label="Tractor Trajectory")
        
        # Visualize front axle center
        fx = state.x + WB * math.cos(state.yaw)
        fy = state.y + WB * math.sin(state.yaw)
        plt.plot(fx, fy, "xg", label="Front Axle Center")
        
        # Draw tractor outline
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
        plt.plot(outline[:, 0], outline[:, 1], "-k")
        
        plt.title(f"Stanley Method Control (k = {k}, v = {v}m/s)")
        plt.xlabel("X [m]")
        plt.ylabel("Y [m]")
        plt.legend(loc="upper left")
        plt.grid(True)
        plt.axis("equal")
        plt.pause(0.01) # Animation update interval
        
    plt.show()

if __name__ == '__main__':
    main()
