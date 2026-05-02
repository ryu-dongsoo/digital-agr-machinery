"""
Week 10 Lab Step 0: Agricultural Drone Waypoint Generation Basic
- Generate zigzag trajectory based on virtual field size and swath width
- Calculate total flight distance and estimated flight time
"""

import numpy as np

# 1. Parameter Setup
field_width = 100.0   # Field width (m)
field_height = 80.0   # Field height (m)
swath_width = 4.0     # Swath width (m)
flight_speed = 5.0    # Flight speed (m/s)

print(f"--- 🚁 Flight Parameters ---")
print(f"Field Area: {field_width * field_height} sq.m")
print(f"Swath Width: {swath_width} m")
print(f"Flight Speed: {flight_speed} m/s\n")

# 2. Survey Grid Waypoint Generation
waypoints = []
# Start at (0,0) and move along Y-axis, reciprocating along X-axis
y_coords = np.arange(0, field_height + swath_width, swath_width)

direction = 1 # 1: Forward (0 -> width), -1: Backward (width -> 0)
for y in y_coords:
    if direction == 1:
        waypoints.append((0, y))
        waypoints.append((field_width, y))
    else:
        waypoints.append((field_width, y))
        waypoints.append((0, y))
    direction *= -1 # Change direction

# 3. Calculate Distance and Time
total_distance = 0.0
for i in range(1, len(waypoints)):
    p1 = waypoints[i-1]
    p2 = waypoints[i]
    # Sum Euclidean distances
    distance = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    total_distance += distance

# Add RTL (Return To Launch) distance (from last point back to first)
rtl_distance = np.sqrt((waypoints[-1][0] - waypoints[0][0])**2 + (waypoints[-1][1] - waypoints[0][1])**2)
total_distance += rtl_distance

estimated_time = total_distance / flight_speed

print(f"--- 📊 Estimated Flight Data ---")
print(f"Number of Waypoints: {len(waypoints)}")
print(f"Total Flight Distance (incl. RTL): {total_distance:.2f} m")
print(f"Estimated Flight Time: {estimated_time:.2f} s ({estimated_time/60:.2f} min)")
