# Introduction to Digital Agricultural Machinery — Weekly Discussion & Quiz Bank

> **Course:** Introduction to Digital Agricultural Machinery (2026 Spring)  
> **Institution:** Dept. of Bio-Industrial Machinery Engineering, Jeonbuk National University  
> **Instructor:** Dongsoo Ryu  
> 📌 **[한국어 버전](../ko/QUIZ_BANK.md)**

---

## Week 1: Paradigm Shift in Digital Agriculture & 2026 Trends

### In-Depth Discussion Questions (3)

**[Discussion 1-1] Light and Shadow of Digital Transformation**
> The transition from Agriculture 4.0 (data/connectivity) to Agriculture 5.0 (AI/robot collaboration) is accelerating. In South Korea's aging rural environment, identify at least **three positive effects** and **three negative side-effects** (digital exclusion, cost burden, etc.) of this rapid digital transformation, and discuss policy measures to minimize the drawbacks.

**[Discussion 1-2] Limits of Generative AI in Agriculture**
> In the lecture, we practiced using generative AI tools (Gemini, ChatGPT, Claude) as research assistants. Discuss the risks of **hallucination (misinformation)** when such AI tools are used directly for agricultural **decision-making** (crop selection, pest control timing, etc.), and propose countermeasures with concrete examples.

**[Discussion 1-3] Feasibility of Carbon-Neutral Agricultural Machinery**
> The "5th Agricultural Mechanization Master Plan" emphasizes carbon-neutral farm machinery (electric/hydrogen tractors). When do you think mass adoption will realistically be possible? Present arguments from both **optimistic and pessimistic** perspectives, considering current battery technology, charging infrastructure, and the demanding workloads of agricultural operations.

---

### Quiz (5 Questions)

**[Q1-1]** Which stage of agricultural evolution is based on 'data and connectivity'?
- (A) Agriculture 1.0
- (B) Agriculture 2.0
- (C) Agriculture 3.0
- **(D) Agriculture 4.0** ✅

**[Q1-2]** What is the primary risk phenomenon that prevents us from blindly trusting information provided by generative AI?
- (A) Overfitting
- **(B) Hallucination** ✅
- (C) Underfitting
- (D) Bias

**[Q1-3]** Which of the following is **NOT** a key technology keyword emphasized in the 5th Agricultural Mechanization Master Plan for 2026?
- (A) Data Sovereignty
- (B) Carbon-Neutral Farm Machinery
- (C) Field-Ready AI
- **(D) Gene-Edited Crops** ✅

**[Q1-4]** Which of the following is **NOT** among the three major challenges of South Korean agriculture that drive the need for digital transformation?
- (A) Aging rural population
- (B) Climate change
- **(C) Expansion of trade surplus** ✅
- (D) Agricultural labor shortage

**[Q1-5]** In the lecture, tools such as Antigravity, Cursor, and VS Code were introduced for what purpose?
- (A) Drone flight simulators
- (B) Remote control tools for agricultural machinery
- **(C) AI-powered development tools (app development, data analysis, etc.)** ✅
- (D) Agricultural ERP systems

---

## Week 2: Agricultural Power Systems (Internal Combustion vs. Electrification)

### In-Depth Discussion Questions (3)

**[Discussion 2-1] Economic Comparison: Electric vs. Diesel Tractor**
> Estimate and compare the 10-year Total Cost of Ownership (TCO) — including purchase price, fuel/electricity costs, and maintenance — of a 100-hp electric tractor versus a diesel tractor. Discuss which power source is more economically viable for different Korean agricultural environments (paddy fields, dry fields, orchards), using specific figures.

**[Discussion 2-2] The Dilemma of Emission Regulations (Tier 5)**
> The SCR (urea system) and DPF (particulate filter) aftertreatment devices required to meet Tier 5 / Stage V emission regulations significantly increase the structural complexity and maintenance costs of agricultural machinery. Discuss where the appropriate balance lies between stricter environmental regulations and the economic realities of farming, incorporating government subsidy policies.

**[Discussion 2-3] The Future of Hydrogen Fuel Cell Tractors**
> Hydrogen fuel cell tractors are attracting attention as an alternative that covers the weaknesses of battery-electric tractors (charging time, range). However, realistic challenges such as hydrogen refueling infrastructure, hydrogen production costs, and rural accessibility remain significant. Present a forecast with supporting evidence on whether hydrogen tractors can be commercialized by 2030.

---

### Quiz (5 Questions)

**[Q2-1]** What term describes a diesel engine's ability to increase torque in response to a sudden load increase?
- (A) Thermal Efficiency
- **(B) Torque Rise / Lugability** ✅
- (C) Compression Ratio
- (D) Air-Fuel Ratio

**[Q2-2]** Which aftertreatment device reduces nitrogen oxides (NOx) by injecting urea solution, as required by Tier 5 / Stage V regulations?
- (A) DPF (Diesel Particulate Filter)
- (B) EGR (Exhaust Gas Recirculation)
- **(C) SCR (Selective Catalytic Reduction)** ✅
- (D) DOC (Diesel Oxidation Catalyst)

**[Q2-3]** One of the greatest advantages of electric tractors is a characteristic available at 0 RPM as soon as the motor starts. What is it?
- (A) High compression ratio
- (B) Low noise
- **(C) Instant maximum torque output** ✅
- (D) Fuel efficiency

**[Q2-4]** What is the mode of PTO (Power Take-Off) operation that functions independently of the transmission?
- (A) Ground Speed PTO
- **(B) Independent PTO** ✅
- (C) Transmission PTO
- (D) Live PTO

**[Q2-5]** In e-CVT (Electric Continuously Variable Transmission), what is the core function that 'CVT' refers to?
- (A) Engine restart after shutdown
- **(B) Continuously varying the gear ratio without discrete gear steps** ✅
- (C) Automatic 4WD switching
- (D) Hydraulic cylinder speed control

---

## Week 3: Agricultural Machinery Communication Networks (CAN & ISOBUS)

### In-Depth Discussion Questions (3)

**[Discussion 3-1] CAN Bus Bandwidth Limitations and Next-Generation Communication**
> The existing ISOBUS (CAN 2.0B, 250 kbps) lacks sufficient bandwidth for transmitting large-volume data such as camera footage or LiDAR point clouds. The next-generation High Speed ISOBUS (ISO 23870, up to 1 Gbps) attempts to solve this with Ethernet. Discuss the **backward compatibility strategy** with existing CAN infrastructure and the **technical and economic challenges** expected when adopting Ethernet in the agricultural machinery industry.

**[Discussion 3-2] The Ideal vs. Reality of ISOBUS Plug & Play**
> The ISOBUS standard aims for Plug & Play — "connect any brand of implement to any brand of tractor and it works automatically." In reality, however, issues such as varying AEF certification levels, proprietary function extensions, and firmware version mismatches persist. Propose the conditions necessary to achieve true interoperability from **technical, institutional, and industrial** perspectives.

**[Discussion 3-3] TIM (Bidirectional Communication) and Autonomous Farming**
> TIM (Tractor Implement Management) enables implements to directly control the tractor's speed, PTO, and hitch. Explain why this bidirectional communication technology could become a **core infrastructure for fully autonomous agricultural machinery systems**, and discuss what additional **safety mechanisms** are needed when TIM is applied to autonomous operations.

---

### Quiz (5 Questions)

**[Q3-1]** When two CAN Bus nodes transmit messages simultaneously, what determines the priority?
- (A) The node that started transmitting first
- **(B) The message with the lower Identifier (ID) value wins** ✅
- (C) The message with the longer data length (DLC)
- (D) Random back-off and retransmission

**[Q3-2]** What component must be installed at both ends of a CAN bus, and what is its correct resistance value?
- (A) Fuse / 10Ω
- (B) Capacitor / 100μF
- **(C) Termination Resistor / 120Ω** ✅
- (D) Inductor / 1mH

**[Q3-3]** What is the most accurate description of the core function of the ISOBUS Virtual Terminal (VT)?
- (A) A mechanical device that directly controls the implement's hydraulic valves
- **(B) A universal display that renders and controls any brand of implement UI on a single tractor monitor** ✅
- (C) An ECU that automatically adjusts the tractor engine's fuel injection rate
- (D) A GNSS antenna module that receives satellite signals

**[Q3-4]** In the J1939 protocol, what parameter does PGN 61444 (EEC1), SPN 190 represent?
- (A) Coolant Temperature
- (B) Vehicle Speed
- **(C) Engine Speed (RPM)** ✅
- (D) Fuel Level

**[Q3-5]** What is the most revolutionary change in TIM (Tractor Implement Management) compared to conventional one-way communication?
- (A) Communication speed increases to 1 Gbps
- (B) The tractor screen changes to a touchscreen
- **(C) The implement can send control commands for the tractor's speed and PTO (bidirectional)** ✅
- (D) Remote control via satellite becomes possible

---

## Week 4: GNSS and Precision Positioning Systems (RTK & Auto-Steering)

### In-Depth Discussion Questions (3)

**[Discussion 4-1] Accessibility Gap in RTK Infrastructure**
> RTK GNSS requires either a Base Station or an NTRIP (Network RTK) service. Farms near urban areas can easily access LTE/5G-based NTRIP services, while farms in mountainous or island regions face connectivity dead zones. Propose realistic solutions — both **technological and policy-based** — to bridge this **precision agriculture infrastructure accessibility gap**.

**[Discussion 4-2] ROI of Auto-Steering System Investment**
> The cost of installing an RTK-based auto-steering system ranges from approximately $6,000 to $15,000. For small-scale farms (1–3 ha), estimate how many years it would take to recoup this investment, considering fuel savings, input material savings, night operation capability, and labor cost reduction. Compare with large-scale farms (50+ ha) and discuss the **economic justification** for small farms.

**[Discussion 4-3] Addressing Multipath Errors in the Field**
> Among GNSS error sources, multipath is one of the most troublesome problems that cannot be corrected even by RTK. It is especially severe in orchards, near greenhouse structures, and in forested areas. Discuss possible approaches to minimize multipath errors from the perspectives of **antenna design, receiver algorithms, and operational environment arrangement**.

---

### Quiz (5 Questions)

**[Q4-1]** What is the fundamental reason why GNSS requires signals from a minimum of 4 satellites?
- (A) Four satellites are the farthest apart
- (B) International agreement mandates a minimum of four
- **(C) Four unknowns must be solved simultaneously: latitude, longitude, altitude, and receiver clock error** ✅
- (D) Satellites operate in groups of four

**[Q4-2]** Which atmospheric layer is identified as the largest source of GNSS error?
- (A) Troposphere
- **(B) Ionosphere** ✅
- (C) Stratosphere
- (D) Thermosphere

**[Q4-3]** What is the key reason RTK (Real-Time Kinematic) achieves dramatically higher precision than conventional DGPS?
- (A) It uses more satellites
- (B) It has a larger antenna
- **(C) It analyzes the carrier wave 'phase,' enabling much more precise distance measurement than code-based methods** ✅
- (D) It receives data via the internet

**[Q4-4]** What is the core role of the IMU (Inertial Measurement Unit) in a tractor auto-steering system?
- (A) Amplifying satellite signals
- (B) Monitoring engine RPM
- **(C) Compensating for antenna position errors caused by tractor tilt (roll, pitch) — terrain compensation** ✅
- (D) Measuring soil moisture

**[Q4-5]** In auto-steering, what is the reference line called that is created by marking a start point (A) and an end point (B) during the tractor's first pass?
- (A) Swath Line
- (B) Grid Map
- **(C) A-B Line** ✅
- (D) Headland Boundary

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

## Week 9: Variable Rate Technology (VRT) & Precision Implements

### In-Depth Discussion Questions (3)

**[Discussion 9-1] Field Application: Map-based vs Sensor-based VRT**
> Variable Rate Technology (VRT) is divided into Map-based (requiring pre-made prescription maps) and Sensor-based (real-time scanning and control) methods. Discuss which method is more economical and practical for small-scale, multi-cropping field farming environments in Korea, and propose a hybrid strategy to overcome the limitations of each method.

**[Discussion 9-2] Economic Analysis of Section Control**
> Installing an 8-section control valve on a 24m boom sprayer can save about 15% of pesticides by preventing overlapping at headlands or in irregularly shaped fields. Quantitatively estimate the Return on Investment (ROI) for a farm adopting this technology, and discuss the law of diminishing marginal utility when dividing sections even further (e.g., individual nozzle control).

**[Discussion 9-3] Combining Drone Spraying with VRT**
> VRT technology is recently being introduced to agricultural spraying drones (multicopters). However, due to the drone's fast flight speed, downwash, and payload limitations, it is difficult to achieve the same precision as tractor-based VRT. Propose technical improvement measures (concerning pumps, nozzles, and flight algorithms) to increase the precision of VRT in drone spraying.

---

### Quiz (5 Questions)

**[Q9-1]** Which of the following best describes Map-based VRT?
- (A) Adjusts valves instantly as sensors scan the crops
- (B) Operates completely independently of the tractor's driving speed
- **(C) Requires a pre-made prescription map (Rx Map) based on prior analysis of drone/satellite imagery** ✅
- (D) Has no preprocessing step, making it best for responding to real-time sudden changes

**[Q9-2]** What is the greatest advantage of PWM (Pulse Width Modulation) nozzle control over conventional pressure-based nozzles?
- (A) It operates entirely without a pump
- (B) The nozzle rotates to cover a wider area
- **(C) It can independently adjust the flow rate while keeping the spray pressure (droplet size) constant** ✅
- (D) It automatically mixes chemicals and water at the nozzle tip

**[Q9-3]** What is the core advantage of an **Electric Drive** planter compared to a mechanical (wheel-driven) planter?
- **(A) It enables VRT and precise seed spacing regardless of wheel slip** ✅
- (B) It requires no battery, improving tractor fuel efficiency
- (C) The motor's heat dries the seeds, increasing the germination rate
- (D) It can adjust planting depth to more than 1 meter

**[Q9-4]** In an ISOBUS system, which core module links the tractor's GPS position with the prescription map to send application commands to the implement ECU?
- (A) TECU (Tractor Electronic Control Unit)
- **(B) TC-GEO (Task Controller Geo-referenced)** ✅
- (C) UT (Universal Terminal)
- (D) TIM (Tractor Implement Management)

**[Q9-5]** What is the process of simplifying NDVI raster data into 3 distinct zones in GIS software called?
- (A) Vectorization
- (B) Smoothing
- **(C) Reclassify (Zoning)** ✅
- (D) Interpolation

## Week 10: Agricultural Drone Spraying Path Generation & Simulation

### In-Depth Discussion Questions (3)

**[Discussion 10-1] The Dilemma of Swath Width: Economics vs. Efficiency**
> Compare and explain the effects of setting a narrow versus a wide swath width on the total drone flight distance and spraying efficiency (e.g., spray uniformity). Present the key variables that must be considered when determining the optimal swath width on an actual farm.

**[Discussion 10-2] Obstacle Avoidance and Path Optimization**
> Describe the logical process by which a waypoint generation algorithm reconfigures the path when a No-Fly Zone (obstacle) is designated in the Ground Control Station (GCS). What methods can be used to minimize the resulting increase in flight time during this process?

**[Discussion 10-3] Designing Spray Trajectories in Crosswind Environments**
> In an actual drone spraying field with strong crosswinds, how should the angle of the survey grid be set to minimize drift, and why? Explain in terms of chemical drift and flight safety.

---

### Quiz (5 Questions)

**[Q10-1]** What is the most critical parameter when generating a zigzag (grid) waypoint path for drone spraying?
- (A) Flight Altitude
- (B) Home Point Coordinates
- **(C) Swath Width** ✅
- (D) Camera Field of View (FOV)

**[Q10-2]** For a 100m x 80m field, how does the total flight distance roughly change if the swath width is reduced from 4m to 2m?
- (A) Decreases by half
- (B) Remains the same
- **(C) Increases by two times** ✅
- (D) Increases by four times

**[Q10-3]** If the total flight distance is 2000m and the drone flies at a speed of 5m/s, what is the estimated minimum flight time?
- (A) 100 seconds
- (B) 200 seconds
- (C) 300 seconds
- **(D) 400 seconds** ✅

**[Q10-4]** What is the term for the trajectory of the drone returning to its takeoff point after completing a flight mission?
- **(A) RTL (Return To Launch)** ✅
- (B) GCS (Ground Control Station)
- (C) IMU (Inertial Measurement Unit)
- (D) ROI (Region of Interest)

**[Q10-5]** Which Python library is most suitable for storing and calculating waypoint arrays in the virtual flight path visualization lab?
- (A) Pandas
- **(B) NumPy** ✅
- (C) TensorFlow
- (D) OpenCV

---

## Week 11: Autonomous Driving Architecture & Path Tracking Simulation

### In-Depth Discussion Questions (3)

**[Discussion 11-1] Pure Pursuit vs. Stanley Algorithm Comparison**
> Pure Pursuit smooths out curves but tends to corner-cut, whereas Stanley excels in straight-line precision via front-axle control. Which control algorithm is more advantageous to pair with a precision seeder (where straightness is critical) versus a multi-purpose rotary tractor (requiring flexible turns)?

**[Discussion 11-2] Dynamic Look-ahead Distance ($L_d$) Design**
> At high speeds, if $L_d$ is too short, severe oscillation (snaking) occurs. Discuss the stability improvements of introducing a function that adjusts $L_d$ in real-time ($L_d = k \cdot v$) proportional to the vehicle's current speed ($v$).

**[Discussion 11-3] Limits of Sensor Fusion and Mitigation**
> RTK-GNSS is precise but suffers from signal dead zones, while LiDAR and Vision are vulnerable to weather (rain, fog). Discuss how to configure sensor fusion to achieve perfect perception across various agricultural environments (open fields, orchards, greenhouses).

---

### Quiz (5 Questions)

**[Q11-1]** Which sensor is essential for acquiring ultra-precise absolute positioning coordinates ($x, y, z$) down to centimeter-level accuracy in agricultural environments?
- (A) Ultrasonic Sensor
- **(B) RTK-GNSS (Real-Time Kinematic GNSS)** ✅
- (C) Infrared Thermal Camera
- (D) IMU (Inertial Measurement Unit) alone

**[Q11-2]** In the Pure Pursuit algorithm, what is the typical phenomenon observed during curves when the look-ahead distance ($L_d$) is set excessively long?
- (A) CTE immediately converges to zero.
- (B) Severe left/right steering oscillation occurs.
- **(C) The vehicle loses the outer trajectory and cuts deeply into the inside of the curve (Corner Cutting).** ✅
- (D) The tractor's speed automatically decreases.

**[Q11-3]** In Coverage Path Planning (CPP), what is the greatest advantage of the zigzag (Boustrophedon) driving pattern?
- (A) It is perfect for handling irregular polygonal boundaries.
- **(B) It minimizes the number of turns when driving parallel to the longest edge, yielding high fuel efficiency.** ✅
- (C) It spirals outward from the center, which is advantageous for circular fields.
- (D) It requires 100% human steering intervention.

**[Q11-4]** What is the term for the shortest perpendicular distance between the reference line the tractor must follow and its current position?
- **(A) Cross-Track Error (CTE)** ✅
- (B) Yaw Rate
- (C) Slip Angle
- (D) Longitudinal Error

**[Q11-5]** In the 3-step autonomous driving architecture, which stage is responsible for global path planning and local obstacle avoidance calculations?
- (A) Perception
- **(B) Decision** ✅
- (C) Control
- (D) Communication

---

## Week 12: Field Robots and End-Effectors

### In-depth Discussion Questions (3 Items)

**[Discussion 12-1] Optimization of Degrees of Freedom (DOF) for Agricultural Robots**
> When designing an apple harvesting robot, compare the suitability of a 5-DOF versus a 7-DOF (redundant) manipulator for complex orchard environments. Discuss this in terms of obstacle avoidance capability, control algorithm complexity, and manufacturing cost.

**[Discussion 12-2] Durability and Practicality of Soft Robotics**
> While soft grippers are revolutionary for harvesting delicate fruits (strawberries, peaches, etc.), they face durability issues due to silicone's vulnerability to harsh outdoor branches or UV exposure. Propose design alternatives (e.g., protective skins, replaceable tips) to overcome these material limitations for commercialization.

**[Discussion 12-3] Robot Vision Placement Strategy: Eye-to-Hand vs. Eye-in-Hand**
> Compare the pros and cons of mounting a camera outside the robot arm (Eye-to-Hand) versus on the wrist (Eye-in-Hand) in terms of 'occlusion (view blockage)' and 'precision approach.' Explain why a system that fuses both methods might be necessary for harvesting robots.

---

### Quiz (5 Items)

**[Q12-1]** What is the minimum number of Degrees of Freedom (DOF) required to fully control the position ($X, Y, Z$) and orientation ($Roll, Pitch, Yaw$) of a robot's end-effector in 3D space?
- (A) 3-DOF
- (B) 4-DOF
- **(C) 6-DOF** ✅
- (D) 8-DOF

**[Q12-2]** What is the name of the computational process used to calculate the required **joint angles** of a robot arm when target coordinates ($X, Y, Z$) are given?
- (A) Forward Kinematics
- **(B) Inverse Kinematics** ✅
- (C) Path Planning
- (D) Autonomous Control

**[Q12-3]** Which term describes a specific posture of a robot arm where the joints align in a straight line, causing a momentary loss of control?
- (A) Dead Zone
- (B) Workspace
- **(C) Singularity** ✅
- (D) Base

**[Q12-4]** What is the term for the property of soft robotics-based grippers that allows them to adapt to the shape of an object and wrap around it without the need for precise sensors or complex algorithms?
- (A) Hardware Acceleration
- **(B) Morphological Computation / Morphological Adaptation** ✅
- (C) Mechanical Friction
- (D) Inverse Kinematic Solution

**[Q12-5]** In a pneumatic soft gripper (Pneu-Net), which layer is inserted to restrict expansion in a specific direction and induce a bending motion when air is injected?
- (A) Elastic Layer
- **(B) Strain Limiting Layer** ✅
- (C) Heating Layer
- (D) Lubricant Layer

---

### 📂 [Week 12 Lab Report Assignment]
#### **Topic: Integrated Design of Crop-Specific Robot Manipulator and End-Effector**

**1. Simulation Data Analysis**
- Using `step0_kinematics_sim.py`, capture and explain the changes in the reachable **Workspace** when the robot arm's link lengths ($L_1, L_2$) are modified.
- Derive the **Inverse Kinematic solutions (Joint Angles)** to harvest a fruit located at specific coordinates and analyze potential **Singularity** issues in that posture.

**2. Detailed End-Effector Design**
- **Target Crop**: (e.g., High-shelf strawberries for greenhouse)
- **Design Core**: Gripping mechanism (soft/mechanical/suction, etc.), stem cutting mechanism, and crop damage prevention strategy.
- **Drawings/Sketches**: Include a structural diagram of the end-effector and a layout of key components (motors, sensors, pneumatic tubes, etc.).

**3. Technical Feasibility Study**
- Identify two potential **Failure Modes** that could occur when your designed end-effector operates in actual agricultural fields (dust, vibration, humidity) and discuss mitigation strategies.
- Describe the appropriate manufacturing method (3D printing, CNC machining, silicone molding, etc.) for this robotic hand and state the reasons why.

---

## Week 13: Agricultural AI and Data Analysis

### In-depth Discussion Questions (3 Items)

**[Discussion 13-1] "Garbage In, Garbage Out" in Agricultural Data**
> Sensor data collected from outdoor agricultural fields often contains significant noise and missing values. Discuss the critical impact of such contaminated data on AI decision-making (e.g., incorrect pest diagnosis, excessive spraying) and strategies for data pre-processing (cleaning).

**[Discussion 13-2] Traditional Machine Learning vs. Deep Learning (CNN)**
> Compare the differences between traditional machine learning, where humans manually extract features, and deep learning, where the model discovers features on its own, using examples of agricultural image recognition. Discuss which approach would be more efficient in small-scale smart farm environments with limited computational resources.

**[Discussion 13-3] Real-time Object Detection (YOLO) and Edge AI**
> Explain why large-scale images collected by autonomous tractors or drones should be processed directly within the equipment (e.g., NVIDIA Jetson) rather than being sent to a cloud server, focusing on communication latency, network disconnections, and safety.

---

### Quiz (5 Items)

**[Q13-1]** What is the term for data that is clearly structured in columns and rows, such as in Excel (CSV) or databases, including variables like temperature, humidity, and rainfall?
- (A) Unstructured Data
- **(B) Structured Data** ✅
- (C) Multimedia Data
- (D) Metadata

**[Q13-2]** Which AI task outputs the bounding box coordinates to indicate 'where' an apple is located within an image for a harvesting robot?
- (A) Image Classification
- **(B) Object Detection** ✅
- (C) Style Transfer
- (D) Speech-to-Text

**[Q13-3]** Which deep learning architecture is specialized for extracting features while maintaining spatial patterns (lines, shapes, textures) between image pixels and serves as the core of agricultural vision AI?
- (A) RNN (Recurrent Neural Network)
- (B) GAN (Generative Adversarial Network)
- **(C) CNN (Convolutional Neural Network)** ✅
- (D) Transformer

**[Q13-4]** What is the technique used to artificially increase the size of a training dataset by flipping, rotating, or adjusting the brightness of original photos to improve model performance?
- (A) Data Compression
- **(B) Data Augmentation** ✅
- (C) Data Encryption
- (D) Data Pruning

**[Q13-5]** During the Teachable Machine practice, what is the fundamental cause of the phenomenon where the recognition rate drops sharply in environments different from the trained background?
- (A) Decreased internet speed
- (B) Low resolution of the webcam
- **(C) Data bias and lack of generalization performance** ✅
- (D) Aging of computer hardware

---

## Week 14: Global Industry Trends & System Integration Design

### In-depth Discussion Questions (3 Items)

**[Discussion 14-1] Autonomous Agricultural Machinery and the "Right to Repair"**
> Modern digital tractors are equipped with advanced software locks (DRM), making it impossible for farmers to perform repairs themselves. Analyze the conflict between the manufacturer's logic of safety and security and the farmer's logic of property/repair rights, and discuss potential compromises as an engineer.

**[Discussion 14-2] Reliability in System Integration (SI)**
> Discuss the importance of a 'Fail-Safe' architecture that prevents the entire system from going out of control or sudden acceleration even if one or two sensors malfunction due to dust or vibration. What are the primary safety redundancy elements to consider when designing agricultural robots?

**[Discussion 14-3] Data Sovereignty and Coexistence with Giant Platform Corporations**
> Who owns the agricultural big data collected by global agricultural machinery companies? Discuss ways to guarantee data sovereignty and profit distribution between farmers who generate the data and companies that process it into intelligent models.

---

### Quiz (5 Items)

**[Q14-1]** What is the legal and social movement to guarantee the repair rights of farmers against software locks (DRM) designed to prevent farmers from repairing tractors directly?
- (A) Data Sovereignty
- **(B) Right to Repair** ✅
- (C) Robot Tax
- (D) Net Zero

**[Q14-2]** Which middleware is used by roboticists worldwide and is a standard software framework for integrating sensor-decision-control modules in agricultural robots?
- (A) Windows
- (B) Android
- **(C) ROS (Robot Operating System)** ✅
- (D) TensorFlow

**[Q14-3]** Like John Deere's 'See & Spray' technology, what is the ultimate goal of technology that precisely sprays pesticides only on weeds to minimize environmental pollution?
- (A) Mass Production
- **(B) Precision Resource Management and Sustainability** ✅
- (C) Upsizing of Equipment
- (D) Full Humanization

**[Q14-4]** What is the design philosophy where a machine automatically stops safely or limits output to prevent larger accidents in case of system failure?
- (A) Overclocking
- **(B) Fail-Safe** ✅
- (C) Fast-Forward
- (D) Multi-Tasking

**[Q14-5]** What is the biggest advantage of 'Swarm Robotics' covered in the Week 14 lecture?
- (A) The price of one robot is very expensive.
- (B) The work speed is always slower than that of large tractors.
- **(C) Soil compaction prevention and ensuring work continuity in case of robot failure** ✅
- (D) It never works without an internet connection.

---

### 📂 [Week 14 Lab Report Assignment]
#### **Topic: Future Digital Agricultural System Integration Design and Technical Analysis Report**

**1. In-depth Analysis of Global Commercialization Cases**
- Select one of the commercialization cases from Week 14 (John Deere 8R, See & Spray, Monarch, etc.) and describe the core **Pain Point** of agriculture it aims to solve and its **technical differentiators**.

**2. Concept Design of a Virtual Agricultural Robot System Integration**
- Design a virtual robot system architecture to solve a specific agricultural problem (e.g., labor shortage in orchards for spraying due to aging).
- **Contents**: Sensors used (Perception), decision algorithms (Decision), actuation methods (Actuation), and a 'Sense-Think-Act' loop diagram.

**3. Technical Ethics and Engineer's Responsibility (Reflection)**
- Choose one of the social/ethical issues (job changes, right to repair, data ownership, etc.) that could occur when the robot you designed is actually introduced, and state your opinion.

---

### 📂 [Week 13 Lab Report Assignment]
#### **Topic: Development and Evaluation of a No-Code Crop/Weed Identification Model using Google Teachable Machine**

**1. Dataset Construction**
- Describe the characteristics of the image data collected for the Normal Crop (Class 1), Weed Proxy (Class 2), and Background (Class 3), including variations in angle and lighting.

**2. Model Training and Tuning**
- Record the hyperparameter settings, such as Epochs and Batch Size, and describe any notable issues encountered during the training process (e.g., training interruption, overfitting).

**3. Performance Testing and Limitation Analysis**
- Quantitatively describe the changes in recognition rate when testing the model in a new environment (different background, different light source) that was not part of the training set.
- Propose two technical or environmental factors that need to be improved for the current model to be applied to actual agricultural sites (e.g., See & Spray systems).

---

> **※ This document can be used for exam preparation and course review.**
