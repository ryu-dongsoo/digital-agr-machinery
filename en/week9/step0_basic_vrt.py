"""
Week 09 Lab Step 0: Understanding Basic VRT Logic
- Create an intuitive 4x4 small virtual field data directly
- Assign fertilizer application rate based on the NDVI value of each cell
- Calculate the sum of total required fertilizer
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# 1. 4x4 Small Virtual NDVI Field Data (Hardcoded)
# Top-left represents excellent growth (0.9), bottom-right is poor (0.2)
ndvi_data = np.array([
    [0.9, 0.8, 0.4, 0.3],
    [0.8, 0.7, 0.3, 0.2],
    [0.5, 0.4, 0.6, 0.5],
    [0.3, 0.2, 0.7, 0.8]
])

# 2. Zone-based Rate Assignment Logic
rate_data = np.zeros_like(ndvi_data)

for i in range(4):
    for j in range(4):
        val = ndvi_data[i, j]
        if val < 0.4:
            rate_data[i, j] = 150  # Zone 1: Poor growth (Supplemental)
        elif val < 0.7:
            rate_data[i, j] = 100  # Zone 2: Normal growth (Standard)
        else:
            rate_data[i, j] = 50   # Zone 3: Excellent growth (Reduced)

# 3. Calculate Total Fertilizer Required
total_fertilizer = np.sum(rate_data)
print(f"✅ Total fertilizer required for this 4x4 area: {total_fertilizer} kg")

# 4. Result Visualization (including text values)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.imshow(ndvi_data, cmap='RdYlGn', vmin=0, vmax=1)
ax1.set_title("Input: NDVI Data")
# Display actual values in each cell
for (j, i), label in np.ndenumerate(ndvi_data):
    ax1.text(i, j, f"{label:.1f}", ha='center', va='center', color='black')

ax2.imshow(rate_data, cmap='YlOrRd')
ax2.set_title("Output: Fertilizer Rate (kg/ha)")
# Display actual values in each cell
for (j, i), label in np.ndenumerate(rate_data):
    ax2.text(i, j, int(label), ha='center', va='center', color='black')

plt.tight_layout()
output_dir = os.path.dirname(os.path.abspath(__file__))
output_img = os.path.join(output_dir, "step0_basic_vrt_result.png")
plt.savefig(output_img, dpi=300)
print(f"✅ Visualization image saved: {output_img}")
# plt.show() # Commented out for automated environments
