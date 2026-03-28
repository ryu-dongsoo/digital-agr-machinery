# Week 07 Lab: Smart Pot — PID Irrigation Control

## 🎯 Lab Overview
- **Objective**: Build a soil moisture-based automatic irrigation system with progressive control strategies (On/Off → P → PI)
- **Format**: Arduino sketches for Tinkercad simulation
- **Prerequisites**: Tinkercad account (https://www.tinkercad.com)

---

## 🛠 [Step 1] `step1_onoff_control.ino`
- **Purpose**: Simplest control — pump ON when dry (sensor > 500), OFF when wet (sensor < 350)
- **Key concept**: Hysteresis dead band to prevent chattering
- **Components**: Soil moisture sensor (A0), relay (pin 7), green/red LEDs (pins 3, 4)

## 🛠 [Step 2] `step2_p_control.ino`
- **Purpose**: Proportional control — pump speed varies proportionally to the error
- **Key concept**: `Output = Kp × Error`, PWM output (0-255)
- **Observation**: Steady-state offset — the system never fully reaches the setpoint

## 🛠 [Step 3] `step3_pi_control.ino`
- **Purpose**: PI control — adds integral term to eliminate steady-state error
- **Key concept**: `Output = Kp × Error + Ki × ∫Error·dt`
- **Anti-windup**: Integral sum resets when error becomes negative (soil sufficiently wet)
- **Observation**: System eventually reaches the exact setpoint with zero offset
