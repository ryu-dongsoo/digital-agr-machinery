# 🚜 Introduction to Digital Agricultural Machinery Final Exam Questions (Weeks 9–14)

> **Course:** Introduction to Digital Agricultural Machinery (2026 Spring)  
> **Institution:** Dept. of Bio-Industrial Machinery Engineering, Jeonbuk National University  
> **Exam Range:** Weeks 9 to 14  
> 📌 **[Back to README](../README.md)**

---

## 1. Quiz (10 Questions)

**[Q1]** Greatest advantage of PWM (Pulse Width Modulation) nozzle control compared to conventional pressure-based nozzles (Origin: Q9-2)
- (A) Direct operation without a pump
- (B) Wider coverage via rotating nozzles
- **(C) Independent flow rate adjustment keeping spray pressure (droplet size) constant** ✅
- (D) Automatic mixture of chemicals and water at nozzle tip

**[Q2]** Core ISOBUS module linking tractor GPS position with prescription map for implement ECU commands (Origin: Q9-4)
- (A) TECU (Tractor Electronic Control Unit)
- **(B) TC-GEO (Task Controller Geo-referenced)** ✅
- (C) UT (Universal Terminal)
- (D) TIM (Tractor Implement Management)

**[Q3]** Most critical parameter for generating zigzag (grid) waypoint paths for drone spraying (Origin: Q10-1)
- (A) Flight Altitude
- (B) Home Point Coordinates
- **(C) Swath Width** ✅
- (D) Camera Field of View (FOV)

**[Q4]** Phenomenon in Pure Pursuit algorithm during curves when look-ahead distance ($L_d$) is set excessively long (Origin: Q11-2)
- (A) Immediate convergence of CTE to zero
- (B) Severe left/right steering oscillation
- **(C) Loss of outer trajectory and cutting deeply into curve inside (Corner Cutting)** ✅
- (D) Automatic decrease of tractor speed

**[Q5]** Shortest perpendicular distance between reference line and current vehicle position (Origin: Q11-4)
- **(A) Cross-Track Error (CTE)** ✅
- (B) Yaw Rate
- (C) Slip Angle
- (D) Longitudinal Error

**[Q6]** Computational process used to calculate required joint angles of robot arm for given target coordinates ($X, Y, Z$) (Origin: Q12-2)
- (A) Forward Kinematics
- **(B) Inverse Kinematics** ✅
- (C) Path Planning
- (D) Autonomous Control

**[Q7]** Property of soft robotics-based grippers allowing self-adaptation and wrapping around object shapes without sensors (Origin: Q12-4)
- (A) Hardware Acceleration
- **(B) Morphological Computation / Morphological Adaptation** ✅
- (C) Mechanical Friction
- (D) Inverse Kinematic Solution

**[Q8]** AI task outputting bounding box coordinates to indicate object location within an image for harvesting (Origin: Q13-2)
- (A) Image Classification
- **(B) Object Detection** ✅
- (C) Style Transfer
- (D) Speech-to-Text

**[Q9]** Deep learning architecture specialized for extracting features while maintaining spatial patterns between image pixels as core of agricultural vision AI (Origin: Q13-3)
- (A) RNN (Recurrent Neural Network)
- (B) GAN (Generative Adversarial Network)
- **(C) CNN (Convolutional Neural Network)** ✅
- (D) Transformer

**[Q10]** Design philosophy where a machine automatically stops safely or limits output to prevent larger accidents in case of system failure (Origin: Q14-4)
- (A) Overclocking
- **(B) Fail-Safe** ✅
- (C) Fast-Forward
- (D) Multi-Tasking

---

## 2. In-Depth Discussion Questions (5 Questions)

**[Discussion 1] Map-based vs. Sensor-based VRT for Small-scale Farming**
- Compare Map-based (prescription maps) and Sensor-based (real-time scanning) methods
- Evaluate suitability and economic/practical limits in small-scale, multi-cropping field environments in Korea
- Propose hybrid VRT operation strategies to overcome individual method limitations

**[Discussion 2] Pure Pursuit vs. Stanley Algorithm Comparison and Implement Matching**
- Compare Pure Pursuit (curve smoothness, corner-cutting) and Stanley (front-axle control, straight-line precision) characteristics
- Develop algorithm matching strategy and justification for precision seeders vs. multi-purpose rotary tractors

**[Discussion 3] Durability and Practicality of Soft Grippers in Outdoor Environments**
- Analyze soft gripper feasibility for delicate fruit harvesting
- Assess durability degradation causes (rough branches, UV exposure) and material limitations
- Propose engineering alternatives (protective skins, replaceable tips) for commercialization

**[Discussion 4] Edge AI (On-device) vs. Cloud Processing for Autonomous Field Equipment**
- Identify limitations of cloud-based transmission for real-time object detection (YOLO) in tractors/drones
- Evaluate safety risks caused by communication latency and signal dead zones in fields
- Analyze necessity of Edge AI platforms (e.g., NVIDIA Jetson) for stable local computation

**[Discussion 5] "Right to Repair" Dilemma and Data Sovereignty in Advanced Machinery**
- Analyze conflicts between manufacturer's safety/DRM locks and farmer's repair/property rights
- Investigate ownership issues of big data collected by global agricultural companies
- Suggest technical and policy compromises for fair profit/data sharing
