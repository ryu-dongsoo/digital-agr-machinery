# Week 10 Lab: Agricultural Drone Virtual Waypoint Generation

## 📺 Reference Video
- **Recommended Watch**: [Mission Planner & Drone Flight Simulation](https://youtu.be/5pyWz4NmPGY?si=wI-YaqQJFgz6pNit)
- Highly recommended to watch before the lab to understand the overall workflow of auto-flight path generation.

## 🎯 Lab Overview
- **Objective**: Understand the algorithm for defining target polygon areas and generating a zigzag (Grid) waypoint path for drone spraying.
- **Format**: Python-based path planning and flight parameter (altitude, swath width, speed) calculation.
- **Learning Algorithm**: Field area (Bounding Box) setup → Trajectory generation based on Swath Width → Calculation of estimated flight time and distance.

---

## 🛠 [Step 0] Environment Setup

### Required Libraries 
- `numpy`: Array operations and distance calculations between coordinates.
- `matplotlib`: Visualization of the generated spraying path and waypoints.

### Installation Command
```bash
pip install numpy matplotlib
```

---

## 💻 [Step 1] [Basic] Zigzag Path Generation based on Parameters (`step0_basic_waypoint.py`)

### Purpose
- Understand the Survey Grid generation logic that occurs automatically within a GCS (like Mission Planner).
- Observe changes in the number of waypoints and total flight distance by adjusting the Swath Width.

### Mechanism
- Define a virtual rectangular field coordinate (e.g., 100m x 80m).
- Generate a reciprocating coordinate array moving along the X-axis while shifting the Y-axis by the set **Swath Width**.
- Extract and list the coordinates of each point (Node).

---

## 💻 [Step 2] Flight Data Validation and Calculation Logic

### Mechanism
- Calculate the **Total Flight Distance** by summing the Euclidean distance between each generated waypoint.
- Calculate the **Estimated Flight Time** by applying the set **Flight Speed (m/s)**.
- Verify through simulation if the mission can be completed with a single battery pack.

### Lab Parameters (Example)
| Parameter | Value | Remarks |
|---|---|---|
| **Field Size** | W: 100m, H: 80m | Approx. 8,000㎡ |
| **Swath Width** | 4.0 m | Based on drone spraying width |
| **Flight Speed** | 5.0 m/s | Optimal speed for downwash |
| **Altitude** | 2.5 m | (Omitted in 2D coordinate plane for this lab) |

---

## 💻 [Step 3] [Advanced] Path Visualization and Verification (`step1_flight_simulation.py`)

### Mechanism
- Draw waypoint markers and movement trajectories on a 2D map using `matplotlib`.
- Visualize the entire flow starting from the Home point, covering the spraying area, and Returning To Launch (RTL).
- Compare visualizations by modifying parameters (e.g., Swath Width 2m vs 4m).

### Output
- `waypoint_path.png`: Output image visualizing the final generated spraying trajectory.

### Field Application Considerations
- **Wind Direction**: In practice, paths are generated at an angle to minimize crosswinds based on wind direction.
- **Obstacle Avoidance**: Designating no-fly zones for utility poles or trees and calculating bypass routes.
