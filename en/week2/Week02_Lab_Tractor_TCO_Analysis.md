# [Week 2] Tractor Power Systems & TCO Analysis

## 1. Lab Overview
In this lab, we quantitatively compare the economic viability of the two primary tractor power sources: **Internal Combustion (Diesel)** and **Electrification (Battery)**. We will calculate the 10-year Total Cost of Ownership (TCO) based on initial purchase prices and variable costs (fuel/electricity and maintenance) and analyze the optimal investment point.

---

## 2. Main Objectives
- Implement a TCO calculation engine using various tractor specification datasets
- Perform sensitivity analysis based on annual working hours and energy price fluctuations
- Visualize the Break-even Point using Matplotlib

---

## 3. Core Algorithm: TCO Equation
$$TCO = P_{initial} + \sum_{t=1}^{n} (Cost_{energy, t} + Cost_{maint, t})$$
- $P_{initial}$: Initial purchase price
- $Cost_{energy}$: Annual energy cost (Consumption rate × hours × unit price)
- $Cost_{maint}$: Annual consumables and maintenance cost

---

## 4. Lab Instructions

### [Step 1] TCO Simulation using Python
Run the provided `step1_tco_analysis.py` file to view the cumulative cost curves for diesel and electric tractors.

```bash
# Install required libraries
pip install matplotlib numpy

# Run the code
python step1_tco_analysis.py
```

### [Step 2] Scenario Analysis (Self-Task)
Try modifying the parameters in the code to observe how the results change:
1. Decrease the annual operating hours to 500 hours and check the viability.
2. Shorten the break-even point by increasing the diesel price to 2,500 KRW/L.
3. Reflect on the impact of government subsidies (assuming an EV subsidy) on the initial price.

---

## 5. Result Interpretation Guide
- **Initial Cost**: Electric tractors are typically 40–50% more expensive due to battery prices.
- **Operating Cost**: Annual operation costs for electric tractors are only about 10–20% of diesel costs.
- **Conclusion**: Electrification becomes economically viable when a certain minimum threshold of annual operation hours is met.

---
📌 **[Return to Discussion & Quiz Bank](../../en/QUIZ_BANK.md)**
