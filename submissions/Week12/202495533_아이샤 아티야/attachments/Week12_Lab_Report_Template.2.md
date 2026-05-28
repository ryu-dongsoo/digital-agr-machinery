# [Digital Agricultural Machinery] Week 12 Lab Report

## 1. Personal Information
- **Student ID**: 202495533
- **Name**: Aisyah Athiya Nur Karima
- **Submission Date**: 26 May 2026

---

## 2. Lab 1: Robot Arm Kinematics Analysis (Simulation)
### 2.1 Workspace Analysis based on Link Lengths
- **Experimental Condition**: ($L_1$=1.0, $L_2$=0.5)
- **Analysis**: (Describe the changes in the reachable range when link lengths increase or decrease.)
- **Screenshot**: 
  > ![Robot Arm Kinematics Analysis](image.png)

### 2.2 Target Acquisition and Inverse Kinematics Solution
- **Target Fruit Coordinates**: ($X$=1.0, $Y$=0.8)
- **Calculated Joint Angles**: ($\theta_1$=-28.7°, $\theta_2$=99°)
- **Singularity Analysis**: (Analyze whether there are sections where control becomes difficult in the above posture.)

---

## 3. Lab 2: Soft Gripper Pneumatic Simulation
- **Input Pressure**: 0.5 (0.0 ~ 1.0)
- **Observation**: (Describe the degree of finger bending and fruit gripping stability according to pressure changes.)
- **Screenshot**:
  > ![soft gripper pneumatic simulation](image-1.png)

---

## 4. Lab 3: Crop-Specific End-Effector Design (Concept Design)
### 4.1 Target Crop and Harvesting Challenges
- **Crop**: corn
- **Challenges**: 
     -Corn ears are often at different heights orienttations making consistent grip difficult
     -The husk is tough and tighty wraped, must be removed or held firmly before detaching.
     -Stalks are thick and fibrous, cutting requires enough force without damaging the ear.
     -Field conditions(moisture, leaves, dust) can affect sensors and mechanism reliability.


### 4.2 Design Mechanism Explanation
- **Gripping/Cutting Method**: The end-effector uses a pair of adaptive rubberized gripper fingers to gently hold the corn ear. A rotating circular blade on one side cuts the stalk just below the ear. The ear is then pulled slightly downward to detach and place into a collection bin.
- **Material and Sensor Usage**: 
      Material: Aluminium frame for light weight and strenght, food grade rubber pads for gentle grip, stainless steel blade for corrosion resistance.
      Sensor: Force sensor in the gripper to avoid excessive pressure on the ear, proximity sensor to detect ear position, and rotary encoder to cocntrol blade position

### 4.3 Design Sketch (Idea Drawing)
> (Attach a hand-drawn or tablet sketch here and label the key components)

---

## 5. Discussion and Conclusion
- **Field Applicability**: (Potential problems and solutions when introduced to actual farmland)
    Problem 1 : dust, dirt, and moisture may effect sensors and moving parts
    Solution 1: Use protective covers sensors, IP-rated components, and regular cleaning.
    Problem  2: Variation in corn height and stalk thickness
    Solution 2: Use adjustable gripper opening and compliant rubber pads, add height sensing for adaption
    Problem  3: Power and control stability in uneven terrain
    Solution 3: Shock absorbing monts and stable power management system.

- **Lab Reflection**: 
    This lab helped me understand the importance of designing an end-effector that is not only effective but also gentle on the crop. Integrating sensors for feedback and using appropriate materials are key to real world performance
