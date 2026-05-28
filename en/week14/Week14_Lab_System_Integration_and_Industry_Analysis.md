# Week 14 Lab: Digital Agriculture System Integration Design and Industry Analysis

## 🎯 Lab Overview
- **Objective**: Design an integrated architecture combining individual technologies (sensors, kinematics, autonomous driving, and AI) studied throughout the semester into a single agricultural robotic system, and compare it with real-world commercialized industrial cases.
- **Lab Format**: System design workshop and technical analysis report writing.
- **Core Learning Concepts**: System Integration (SI), Sense-Think-Act Loop, Fail-Safe Design, Technology Ethics.

---

## 🛠 [Step 1] Global Commercialized Technology Case Analysis
Select and analyze in detail one of the global corporate technologies covered in the lecture.

1. **Target Selection**: John Deere 8R (fully autonomous), See & Spray (precision spraying), Monarch (electrification), Fendt Xaver (swarm robotics), etc.
2. **Analysis Points**:
   - What agricultural challenges (Labor, Cost, Environment) does this technology solve?
   - What are the core sensors (Perception) and algorithms (AI/Control) utilized?
   - What is the key differentiator compared to traditional mechanical equipment?

---

## 🏗️ [Step 2] Virtual Agricultural Robot System Integration Design
Define an agricultural problem you wish to solve and design a robotic system to address it.

1. **Problem Definition**: Specify a target crop (e.g., Apple, Strawberry) and a concrete operation (e.g., harvesting, pruning, spraying).
2. **Perception**: Determine which combination of sensors (LiDAR, RGB-D camera, GNSS, etc.) will be used to perceive the surrounding environment and crops.
3. **Decision**: Design how the robot will process the perceived data to make decisions (path generation, object classification, grasping plans).
4. **Actuation**: Decide how the physical actions (driving, robot arm movements, nozzle spraying) will be executed.

---

## 🛡️ [Step 3] Reliability and Safety Design (Fail-Safe)
Establish strategies to ensure system reliability in harsh outdoor environments (mud, dust, network disconnects).

1. **Failure Assumptions**: Simulate scenarios where sensors are blocked or GNSS signals are lost.
2. **Safety Feature Design**: Devise a 'Fail-Safe' architecture including emergency stop mechanisms, sensor redundancy, and autonomous return-to-base in case of communication loss.

---

## 📝 [Step 4] Technology Ethics Reflection and Report Writing
Based on the lab outcomes, complete the [Week 14 Lab Report].

- **Data Sovereignty**: Who should own the field data collected by your designed robot — the farmer or the company?
- **Right to Repair**: Will you design the robot so that farmers can repair it themselves, or will the manufacturer maintain exclusive control for safety and security?
- **Social Responsibility**: Write your perspective as an engineer on how your technology will impact rural labor and employment.

---

### 💡 Tips
- Consider how to utilize the **ROS (Robot Operating System)** framework, introduced in the second half of the lecture, for your system integration design.
- Rather than abstract ideas, integrating concrete kinematics and AI knowledge practiced in the Week 12 and 13 labs will yield higher evaluations.
