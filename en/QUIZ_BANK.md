# Introduction to Digital Agricultural Machinery — Weeks 5-7 Discussion & Quiz Bank

> **Course:** Introduction to Digital Agricultural Machinery (2026 Spring)  
> **Institution:** Dept. of Bio-Industrial Machinery Engineering, Jeonbuk National University  
> **Instructor:** Dongsoo Ryu  
> 📌 **[한국어 버전](../ko/QUIZ_BANK.md)**

---

## Week 5: Optical Sensors & Vegetation Indices (NDVI & NDRE)

### Discussion Topics (3 Problems)

**[Discussion 5-1] Limitations of NDVI & Next-Generation Vegetation Indices**
> NDVI has been the remote sensing standard for decades, but suffers from saturation in dense canopies during late growth stages. NDRE partially addresses this but has its own limitations. Investigate when **newer vegetation indices (e.g., EVI, SAVI, MTCI)** may be more useful, and propose an optimal index combination for major Korean crops (rice, apple, strawberry).

**[Discussion 5-2] Multispectral vs Hyperspectral — A Farmer's Practical Choice**
> Hyperspectral sensors enable highly precise analysis with 100+ continuous spectral bands, but face high cost (tens of thousands of dollars), massive data processing loads (hundreds of GB/flight), and specialist requirements. Multispectral sensors cover 5-10 bands for general use but lack chemical-level diagnostic resolution. For a **10-hectare apple orchard** adopting drone-based remote sensing, which sensor type would you recommend? Discuss with supporting evidence and assumptions.

**[Discussion 5-3] The Danger of Uncalibrated Data**
> DLS (Downwelling Light Sensor) and CRP (Calibrated Reflectance Panel) calibration is critical. However, field pressures (time constraints, lost panels, degraded CRP reflectance) frequently lead to skipped calibration. Identify at least **3 specific error scenarios** where uncalibrated NDVI data could lead to wrong agricultural decisions (e.g., false disease alerts, over-fertilization) and discuss mitigation strategies.

---

### Quiz (5 Questions)

**[Q5-1]** What is the physiological reason healthy plants strongly reflect near-infrared (NIR, 700-1300nm) light?
- (A) Chlorophyll actively uses NIR for photosynthesis
- (B) NIR wavelengths are blocked by Earth's atmosphere
- **(C) The spongy mesophyll tissue inside leaves would suffer heat damage from absorbing NIR, so the structure evolved to reflect it** ✅
- (D) Soil absorbs NIR and re-emits it toward plants

**[Q5-2]** In the NDVI formula $(NIR - RED) / (NIR + RED)$, what causes healthy vegetation to have high NDVI values?
- (A) Red reflectance increases and NIR reflectance decreases
- **(B) Chlorophyll strongly absorbs Red (low reflectance) while cell structure strongly reflects NIR (high reflectance)** ✅
- (C) Both Red and NIR are reflected equally
- (D) The denominator approaches zero

**[Q5-3]** When NDVI saturates, which wavelength band does NDRE use as a substitute?
- (A) Blue (~450nm)
- (B) Green (~550nm)
- **(C) Red Edge (~710-720nm)** ✅
- (D) SWIR (~1500nm)

**[Q5-4]** Why is a gray panel placed on the ground and captured before multispectral drone flights?
- (A) To focus the camera
- (B) To record GPS coordinates
- **(C) To calibrate the entire image's reflectance values using a known absolute reflectance reference** ✅
- (D) To measure drone flight altitude

**[Q5-5]** Which best describes the difference between Multispectral and Hyperspectral cameras?
- (A) Multispectral includes thermal, hyperspectral captures RGB only
- (B) Multispectral uses 100+ bands, hyperspectral uses 5 or fewer
- **(C) Multispectral uses 5-10 wide, discrete bands; hyperspectral uses 100+ narrow, continuous bands to create spectral fingerprints** ✅
- (D) Both use the same principle and only differ in resolution

---

## Week 6: 3D Spatial Perception (LiDAR, Depth Camera & SLAM)

### Discussion Topics (3 Problems)

**[Discussion 6-1] LiDAR Price Decline & Agricultural Adoption**
> Solid-state LiDAR prices have plummeted from tens of millions to 1-3 million KRW due to the autonomous vehicle industry. If this trend extends to agriculture, **can equipping small orchard robots or drones with LiDAR be economically justified?** Estimate the expected ROI (yield increase, pesticide savings, labor cost reduction). Also discuss the extent to which low-cost Depth Cameras (stereo cameras) could substitute for LiDAR.

**[Discussion 6-2] SLAM Challenges in Agricultural Environments**
> SLAM is essential for autonomous navigation in GPS-denied areas (under orchard canopies, inside greenhouses). However, agricultural environments feature **extreme dynamic variables**: seasonal canopy changes, unpaved road vibrations, and rain/fog sensor degradation. Research and present technical solutions for ensuring SLAM stability in these 'outdoor unstructured environments' (e.g., multi-sensor fusion, semantic SLAM, deep learning-based features).

**[Discussion 6-3] 3D Phenotyping & Breeding Innovation**
> LiDAR-based 3D Phenotyping can simultaneously measure thousands of plants' structural traits (height, canopy width, DBH) non-destructively, revolutionizing breeding research productivity. However, traditional **breeding researchers (plant science background)** often lack 3D data processing, programming, and GIS skills. Discuss what changes are needed in university curricula to **cultivate IT-agriculture convergence talent**.

---

### Quiz (5 Questions)

**[Q6-1]** What fundamental distance measurement principle is shared by LiDAR, ultrasonic sensors, and radar?
- (A) Triangulation
- **(B) Time-of-Flight (ToF)** ✅
- (C) Phased Array
- (D) Doppler Effect

**[Q6-2]** What structural difference allows 3D LiDAR to generate volumetric Point Clouds unlike 2D LiDAR?
- (A) Longer laser wavelength
- (B) Rotation speed is 2× faster
- **(C) Multiple vertical laser beams (16, 32, 64, 128 channels) rotate and scan simultaneously** ✅
- (D) GPS coordinates are recorded alongside

**[Q6-3]** Which best describes the core problem SLAM solves?
- (A) An algorithm for optimizing drone battery life
- (B) A technology for converting satellite photos into 3D models
- **(C) A technology for simultaneously building a map while navigating an unknown environment, and estimating one's position within that map** ✅
- (D) A control system for automatically adjusting pesticide spray volume

**[Q6-4]** What is the correct formula for computing CHM (Canopy Height Model) from LiDAR Point Cloud?
- (A) CHM = DTM + DSM
- **(B) CHM = DSM − DTM** ✅
- (C) CHM = DSM × DTM
- (D) CHM = DTM − DSM

**[Q6-5]** Which Depth Camera technology operates most reliably under outdoor direct sunlight?
- (A) Structured Light
- **(B) ToF Camera (active infrared phase shift)** ✅
- (C) RGB monocular camera
- (D) Thermal camera

---

## Week 7: Smart Farm Environmental Sensing & PID Control

### Discussion Topics (3 Problems)

**[Discussion 7-1] PID Control vs AI-Based Control for Agriculture**
> PID control is simple and stable, covering 90%+ of industrial control worldwide. However, in agriculture where environmental variables (weather, season, growth stage) change complexly, **fixed Kp, Ki, Kd values** can't optimally handle all situations. Reinforcement learning (RL) or deep learning-based adaptive control can auto-adjust but suffers from black-box properties and data scarcity. For a **1,000m² strawberry smart greenhouse**, debate which approach is more practically suitable from cost, maintenance, reliability, and performance perspectives.

**[Discussion 7-2] Soil Sensor Calibration Dilemma**
> FDR soil moisture sensors are inexpensive and easy to use but measurement accuracy varies significantly with soil type (sandy, loam, clay), temperature, and EC. When manufacturer-provided calibration curves don't match local soil characteristics, **VWC errors exceeding ±10%** can occur. Quantitatively analyze the impact on automated irrigation control quality (e.g., over-irrigation volume, moisture stress duration) and propose practical field calibration methodologies.

**[Discussion 7-3] Small Farm Smart Farm Entry Strategy**
> State-of-the-art smart farm systems (multi-sensor networks + cloud + AI control) cost tens of millions of KRW per 10a (300 pyeong), prohibitive for small-scale farmers. However, the **Arduino + FDR sensor + relay** DIY system from this lab costs only tens of thousands of KRW in parts. Design a **phased roadmap (Stage 0 → 1 → 2 → 3)** for small farms to incrementally adopt smart farming, specifying cost, technical difficulty, and expected benefits at each stage.

---

### Quiz (5 Questions)

**[Q7-1]** How does an FDR (Frequency Domain Reflectometry) soil moisture sensor measure soil water content?
- (A) Analyzes soil color changes via camera
- (B) Measures evaporated moisture weight
- **(C) Exploits the fact that water's dielectric constant (~80) is vastly higher than air (~1) or soil (~4), causing electrode capacitance (frequency) to change with moisture content** ✅
- (D) Irradiates infrared on the soil surface and measures reflectance

**[Q7-2]** When soil EC (Electrical Conductivity) exceeds 3.0 dS/m, what is the most appropriate problem and response?
- (A) Soil becomes too acidic; apply lime
- **(B) Excessive salt accumulation inhibits root osmotic absorption; perform leaching irrigation** ✅
- (C) Soil moisture is insufficient; irrigate immediately with large volumes
- (D) pH becomes too high; apply sulfuric acid

**[Q7-3]** What is the phenomenon called when a pump rapidly alternates ON/OFF near the setpoint in On/Off control?
- (A) Overshoot
- (B) Steady-State Error
- **(C) Chattering** ✅
- (D) Integral Windup

**[Q7-4]** What is the most important role of the **Integral term (I)** in PID control?
- (A) Dampens rapid error changes to suppress overshoot
- (B) Adjusts output proportionally to error magnitude
- **(C) Reflects accumulated error over time to drive steady-state error to zero** ✅
- (D) Filters sensor noise

**[Q7-5]** What is the core characteristic of a 'feedback loop (Closed-Loop)' in a smart farm control system?
- (A) Operates actuators on a predetermined schedule without sensors
- (B) Maintains identical output permanently once configured
- **(C) The sensor re-measures the result of actuator action, and the control output is continuously corrected based on that feedback** ✅
- (D) Stops operating when internet connection is lost

---

> **※ This document can be used for midterm preparation and course review.**
