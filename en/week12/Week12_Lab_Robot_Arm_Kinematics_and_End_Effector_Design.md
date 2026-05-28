# Week 12 Lab: Agricultural Robot Kinematics Simulation and End-Effector Design

## 🎯 Lab Overview
- **Objective**: Understand the principles of kinematics for agricultural manipulators and perform conceptual design of an innovative end-effector for harvesting specific crops.
- **Lab Composition**:
    1. **[Step 1] Python-Based Robot Arm Kinematics Simulation**: Comprehend joint control of a 2-DOF planar robot arm and the principles of reaching a target coordinates.
    2. **[Step 2] Pneumatic Soft Gripper Actuation Simulation**: Understand the morphological computation/adaptation of silicon fingers in response to input pressure.
    3. **[Step 3] Customized End-Effector Conceptual Design**: Sketch and design mechanisms of a robotic hand optimized for a selected target crop (e.g., strawberry, tomato, apple).

---

## 🛠 [Step 0] Environment Setup

### Required Libraries
- `numpy`: Multi-dimensional array operations and trigonometric functions.
- `matplotlib`: Visualization of the robot arm structure and motion.

### Installation Command
```bash
pip install numpy matplotlib
```

---

## 💻 [Step 1] Robot Arm Kinematics Simulation (`step0_kinematics_sim.py`)

### Objectives
- Confirm how changes in joint angles ($\theta$) affect the final end-effector position ($X, Y$) (Forward Kinematics).
- Understand the diversity of joint combinations required to reach a specific target fruit coordinates.

### Core Concepts
- **Forward Kinematics**: Joint angles $\rightarrow$ End-effector coordinates.
- **Inverse Kinematics**: Target coordinates $\rightarrow$ Joint angles (intuitively experienced in this lab by manipulating sliders).

### Instructions
1. Run the provided `step0_kinematics_sim.py` file.
2. Manipulate the **Theta 1** and **Theta 2** sliders at the bottom to adjust the joint angles.
3. Try to find the optimal joint angles to harvest a virtual fruit at specific coordinates (e.g., $X=1.5, Y=0.5$).

---

## 💻 [Step 2] Soft Gripper Pneumatic Actuation Simulation (`step1_soft_gripper_viz.py` & `step2_soft_gripper_3d.py`)

### Objectives
- Visualize the basic principle of soft robotics, where flexible materials deform under air pressure.
- Understand how morphological computation/adaptation is advantageous for gripping delicate organic targets (fruits).

### Instructions
1. Run the `step1_soft_gripper_viz.py` (2D) or `step2_soft_gripper_3d.py` (3D) file.
2. Manipulate the **Pressure** slider to observe the degree of finger bending.
3. Determine how much pressure is needed to safely wrap and hold the virtual fruit.

---

## 📝 [Step 3] Harvesting End-Effector Conceptual Design

### Objectives
- Design a unique harvesting tool that balances mechanical rigidity and biological compliance.
- Apply the concepts learned in the Week 12 lecture (soft robotics, vacuum suction, cutting mechanisms) to a practical design.

### Lab Task: "Design Your Own Agricultural Robot Hand"
Complete a team-based (or individual) conceptual design sketch according to the template below.

#### 1. Target Crop Selection & Characteristic Analysis
- **Selected Crop**: (e.g., Strawberry, Grape, Melon, etc.)
- **Crop Characteristics**: (e.g., thin skin, tough stems, clustered growth, etc.)
- **Key Risk Factors in Harvesting**: (e.g., bruising, falling, stem damage, etc.)

#### 2. End-Effector Mechanism Design (Sketch)
> **[Mandatory Elements to Include in the Sketch]**
> - **Gripping Method**: (Mechanical claw / Vacuum suction / Soft gripper / Hybrid)
> - **Detaching Method**: (Twisting / Scissor cutting / Pulling)
> - **Material**: (Contact surface material - silicone, sponge, etc.)
> - **Sensor Placement**: (Camera, pressure sensors, etc.)

#### 3. Unique Selling Point (USP)
- What distinguishes your design from traditional harvesting methods or other robotic hands?
- e.g., "Our team's gripper precisely targets only the strawberry stem (pedicel), completely avoiding any direct contact with the delicate flesh."

---

## 🚀 Submission and Presentation
- **Python Simulation**: One screenshot of the robot arm successfully reaching a designated target coordinates.
- **Conceptual Sketch**: A PDF or image file containing the design drawings (hand-drawn or digital sketches) with detailed descriptions.
- **Presentation**: A 3-minute pitch on the core operating principles of your team's design.

---

### 💡 Tips and References
- **Applying Soft Robotics**: Instead of rigid grippers, consider silicone fingers that inflate under pneumatic pressure to conform to irregular shapes.
- **Combining Multi-Functions**: A hybrid structure (e.g., holding the fruit with vacuum suction and cutting the stem with a small blade) can be highly efficient.
- **Eye-in-Hand**: Placing a compact camera in the center of the robot palm enables more precise distance measurements to the target fruit.
