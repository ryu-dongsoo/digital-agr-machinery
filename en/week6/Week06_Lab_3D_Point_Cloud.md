# Week 06 Lab: 3D Point Cloud — LiDAR Scanning & Phenotyping

## 🎯 Lab Overview
- **Objective**: Experience tractor-mounted LiDAR scanning via animation and perform automated 3D crop phenotyping
- **Format**: Python simulation (Step 1: animated LiDAR) → Data analysis (Step 2: 3D Phenotyping)
- **Prerequisites**: Python 3.x (`numpy`, `matplotlib`)
- **Note**: Runs fully on Matplotlib 3D — no Open3D dependency required

---

## 💻 [Step 1] `step1_lidar_scanning_simulation.py`

### Purpose
- Animate a **tractor driving through an orchard** while its mounted **LiDAR scans** surrounding trees, building a 3D Point Cloud in real time

### Learning Points
- Intuitive experience of the LiDAR Time-of-Flight (ToF) principle
- Each point in the cloud = one laser pulse reflection
- SLAM concept: 3D map progressively built as the tractor moves

### Panels
- **Left**: 2D top view — tractor position (red square), LiDAR scan range (yellow circle), tree layout (green)
- **Right**: 3D view — cumulative Point Cloud with Height Ramp colormap

### Output Files
- `scanned_orchard.npy`: Accumulated Point Cloud data (reused in Step 2)
- `step1_result.png`: Final scan result capture

---

## 💻 [Step 2] `step2_tree_phenotyping.py`

### Purpose
- Automatically analyze the scanned Point Cloud to extract **tree height** and **canopy spread** for each individual tree

### Learning Points
- Grid-based segmentation for detecting individual trees
- Axis-Aligned Bounding Box (AABB) for automated crop dimension extraction
- Efficiency of automation vs manual measurement

### Panels
- **Left**: 2D top view — detected trees with red bounding boxes + height labels
- **Right**: 3D view — Height Ramp colormap + semi-transparent red bounding boxes

### Console Output
- Full tree inventory table (center coordinates, height, canopy spread)
- Summary statistics (mean, standard deviation)

### Output Files
- `step2_result.png`: 3D Phenotyping measurement result capture
