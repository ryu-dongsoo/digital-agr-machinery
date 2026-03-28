# Week 04 Lab: GNSS Precision Positioning & A-B Line Path Planning

## 🎯 Lab Overview
- **Objective**: Visually experience GNSS trilateration principles, compare RTK correction effectiveness, and quantitatively analyze A-B Line path planning economics
- **Format**: Step-by-step Python simulation (numpy + matplotlib)
- **Prerequisites**: Python 3.x

---

## 💻 [Step 1] `step1_gnss_trilateration.py`
- **Purpose**: Visualize how 4 satellite distance circles intersect to determine receiver position
- **3 panels**:
  - ① Ideal trilateration (zero error) — circles intersect at exactly one point
  - ② Real GNSS — atmospheric errors cause circles to misalign, producing a scatter cloud
  - ③ Multi-Constellation benefit — error reduction with increasing satellite count
- **Output**: `step1_result.png`

## 💻 [Step 2] `step2_rtk_vs_gnss.py`
- **Purpose**: Compare tractor path tracking with standard GNSS (2-5m error) vs RTK (2cm error)
- **Key concept**: Cross-track Error, quantified crop damage ratio
- **4 panels**:
  - Top: GNSS trajectory vs RTK trajectory (driving along crop rows)
  - Bottom: Cross-track error time series comparison
- **Output**: `step2_result.png`

## 💻 [Step 3] `step3_abline_path_planning.py`
- **Purpose**: Generate parallel passes on a virtual field (~1.2ha trapezoid) using A-B Line and analyze economics
- **3 scenarios**: Novice driver (50cm overlap) vs Expert (20cm overlap) vs RTK (2cm overlap)
- **6 panels**:
  - Top: 3 field + pass visualizations per scenario
  - Bottom: Cost comparison, work time comparison, RTK ROI analysis
- **Output**: `step3_result.png`
