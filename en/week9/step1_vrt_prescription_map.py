"""
Week 09 Lab: VRT Prescription Map Generation Python Practice
- Generation of virtual NDVI field data and zoning
- Allocation of application rates per zone and saving as GeoJSON vector data
"""

import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import os

# 1. Generate Virtual NDVI Data (10x10 Grid Field)
np.random.seed(42)
# Simulating virtual data with excellent growth in the center (0.8) and poor growth at the edges (0.3)
x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
ndvi_base = 0.8 - 0.4 * (x**2 + y**2)
# Add noise
ndvi_data = ndvi_base + np.random.normal(0, 0.05, (10, 10))
ndvi_data = np.clip(ndvi_data, 0.0, 1.0) # Clip between 0~1

# 2. Zoning and Rate Allocation
# Zone 1 (NDVI < 0.4): 150 kg/ha
# Zone 2 (0.4 <= NDVI < 0.7): 100 kg/ha
# Zone 3 (NDVI >= 0.7): 50 kg/ha
rate_data = np.zeros_like(ndvi_data)
zone_data = np.zeros_like(ndvi_data, dtype=int)

for i in range(ndvi_data.shape[0]):
    for j in range(ndvi_data.shape[1]):
        val = ndvi_data[i, j]
        if val < 0.4:
            zone_data[i, j] = 1
            rate_data[i, j] = 150
        elif val < 0.7:
            zone_data[i, j] = 2
            rate_data[i, j] = 100
        else:
            zone_data[i, j] = 3
            rate_data[i, j] = 50

# 3. Vectorization (Polygon Generation and GeoDataFrame Construction)
polygons = []
rates = []
zones = []

# Set coordinate scale (Virtual coordinate: 10m x 10m per pixel)
pixel_size = 10 

for i in range(ndvi_data.shape[0]):
    for j in range(ndvi_data.shape[1]):
        x_coord = j * pixel_size
        y_coord = -i * pixel_size # y-coordinate from top to bottom
        
        # Construct square polygon vertices
        poly = Polygon([
            (x_coord, y_coord),
            (x_coord + pixel_size, y_coord),
            (x_coord + pixel_size, y_coord - pixel_size),
            (x_coord, y_coord - pixel_size)
        ])
        polygons.append(poly)
        rates.append(rate_data[i, j])
        zones.append(zone_data[i, j])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame({
    'Zone': zones,
    'Rate_kg_ha': rates
}, geometry=polygons)

# Specify save folder based on current script execution path
output_dir = os.path.dirname(os.path.abspath(__file__))

# 4. Export File (GeoJSON)
# GeoJSON is easier to handle as a single file compared to Shapefile
output_filename = os.path.join(output_dir, "vrt_rx_map.geojson")
gdf.to_file(output_filename, driver="GeoJSON")
print(f"✅ Prescription map generation complete: {output_filename}")

# 5. Visualization (Matplotlib)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Original NDVI Plot
im1 = ax1.imshow(ndvi_data, cmap='RdYlGn', vmin=0, vmax=1)
ax1.set_title("Original NDVI Map (Virtual Data)")
fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)

# Prescription Rate Map Plot (using GeoPandas built-in function)
gdf.plot(column='Rate_kg_ha', cmap='YlOrRd', legend=True, ax=ax2, edgecolor='black')
ax2.set_title("VRT Prescription Map (Rate: kg/ha)")
ax2.axis('off')

plt.tight_layout()
output_img = os.path.join(output_dir, "vrt_rx_map.png")
plt.savefig(output_img, dpi=300)
print(f"✅ Visualization image save complete: {output_img}")
# plt.show() # Commented out to prevent blocking in server or non-interactive environments
