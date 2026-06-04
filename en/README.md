# 🚜 Digital Agricultural Machinery Lab Portfolio (English)

> **Author / Rights Holder:** 전북대학교 생물산업기계공학과 유동수 (ryudongsoo@jbnu.ac.kr)

> **Instructor:** Dongsoo Ryu (Jeonbuk National University)  
> **[Korean Version Link](../ko/README.md)**

This directory contains the weekly lab materials for the **Introduction to Digital Agricultural Machinery** course. Each week's folder includes Python practical code and a detailed lab manual.

---

## 🗓️ Weekly Lab List

| Week | Topic | Key Content | Source Code |
|:---:|---|---|:---:|
| **02** | **Power Systems & TCO Analysis** | 10-year Total Cost of Ownership (TCO) simulation: Diesel vs Electric | [Link](week2/) |
| **03** | **Communication (CAN & ISOBUS)** | J1939 CAN ID analysis and PGN/SPN data decoding practice | [Link](week3/) |
| **04** | **GNSS & Path Planning** | RTK correction principles and A-B Line based path planning | [Link](week4/) |
| **05** | **Optical Sensing & NDVI** | Vegetation Index (NDVI) calculation and mapping | [Link](week5/) |
| **06** | **3D Perception (LiDAR)** | Point Cloud data processing and structural phenotyping | [Link](week6/) |
| **07** | **Smart Farm Control Systems** | Environmental monitoring and PID-based irrigation control | [Link](week7/) |
| **09** | **VRT Prescription Map** | Variable Rate Technology (VRT) prescription map generation and application simulation | [Link](week9/) |
| **10** | **Drone Flight Control** | Automated spraying path (Waypoint) generation and flight simulation | [Link](week10/) |
| **11** | **Autonomous Driving Path Tracking** | Pure Pursuit steering performance analysis based on Ld tuning | [Link](week11/) |
| **12** | **Field Robots & End-Effectors** | 2-DOF kinematics and soft gripper compliance simulation | [Link](week12/) |
| **13** | **Agricultural AI & Data Analysis** | No-Code AI (Teachable Machine) based crop/weed classification model | [Link](week13/) |
| **14** | **System Integration & Industry Analysis** | Global commercialization technology analysis and next-gen digital agriculture | [Link](week14/) |

---

## 🚀 Getting Started

> 📌 **First-time students: See the [Lab Environment Setup Guide](Lab_Environment_Setup_Guide.md) first**

### Step 1: Install Basic Environment

- **Python 3.11+**, **VS Code**, **Git** required
- Detailed instructions → [Lab Environment Setup Guide](Lab_Environment_Setup_Guide.md)

### Step 2: Download Lab Materials

```bash
git clone https://github.com/ryu-dongsoo/digital-agr-machinery.git
```

### Step 3: Install Python Packages

#### Required Packages (Common for All Weeks)

```bash
pip install numpy matplotlib
```

#### Week-Specific Additional Packages

| Week | Additional Packages | Install Command | Notes |
|:---:|-----------|----------|------|
| **03** | *(None)* | — | Standard library only |
| **05** | `rasterio` | `pip install rasterio` | GeoTIFF image processing |
| **09** | `geopandas`, `shapely` | `pip install geopandas shapely` | GeoJSON prescription map |
| **13** | `opencv-python`, `tensorflow` | `pip install opencv-python tensorflow` | AI model loading |
| **13** | `ultralytics` | `pip install ultralytics` | YOLO detection (optional) |

> ⚠️ **Bulk install** (all packages at once):
> ```bash
> pip install numpy matplotlib rasterio geopandas shapely opencv-python tensorflow ultralytics
> ```

### Step 4: Run Labs

1. Read the **lab manual (`*.md`)** for the relevant week first
2. Run scripts in order: `step0_xxx.py` → `step1_xxx.py` → ...
3. Modify parameters as instructed and observe results
4. Capture screenshots (`Win+Shift+S`) → Attach to report

### Step 5: Submit Reports

- Submit via **GitHub Issues** → [Submission Guide](Lab_Environment_Setup_Guide.md#8-lab-report-submission-github-issue)
- Title format: `[WeekXX] StudentID_Name_LabReport`

### Step 6: Quizzes & Discussion

- Review key concepts in the **[Discussion Topics & Quiz Bank](QUIZ_BANK.md)**

---

## 📞 Contact & Support
- **Professor**: Dongsoo Ryu (ryudongsoo@jbnu.ac.kr)
- **Lab**: Agricultural Smart Robot Lab (ASRL), JBNU

---
*© 2026 Jeonbuk National University. All rights reserved.*

## 📝 변경 이력 (Changelog)
- **2026-05-07 15:19:18** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Update video title to explicitly mention Daedong vs John Deere comparison
- **2026-05-07 15:18:35** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add second Daedong AI Tractor video to lab manuals
- **2026-05-07 15:15:47** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Daedong AI Tractor YouTube video link to lab manuals
- **2026-05-07 15:11:58** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Merge tracking algorithms into path_tracking_compare.py with 3x animation speed
- **2026-05-07 15:03:14** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Stanley method simulator and animation explanations
