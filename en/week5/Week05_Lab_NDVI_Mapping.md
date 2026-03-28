# Week 05 Lab: NDVI Mapping & Vegetation Health Analysis

## 🎯 Lab Overview
- **Objective**: Simulate multispectral satellite imagery (RED/NIR bands) and compute NDVI with spatial visualization
- **Format**: Step-by-step Python scripting with auto-generated result images
- **Prerequisites**: Python 3.x (`rasterio`, `numpy`, `matplotlib`)

---

## 💻 [Step 1] `step1_ndvi_calculation.py`
- **Purpose**: Download a real satellite tile (California vineyard), simulate RED and NIR multispectral bands, and compute NDVI index
- **Output**: Side-by-side RGB vs NDVI map → `step1_result.png`

## 💻 [Step 2] `step2_colormap_visualization.py`
- **Purpose**: 3-panel visualization comparing RED band, NIR band, and NDVI map
- **Key concept**: Vegetation absorbs RED (dark) and reflects NIR (bright) → NDVI quantifies this contrast
- **Output**: `step2_result.png`

## 💻 [Step 3] `step3_polygon_extraction.py`
- **Purpose**: Extract treatment-required zones (NDVI < threshold) as binary mask
- **Key concept**: Precision agriculture — spray only where needed, not the entire field
- **Output**: `step3_result.png`

## 💻 [Step 4] `step4_interactive_ndvi_slider.py`
- **Purpose**: Interactive slider to adjust NDVI threshold in real time
- **Key concept**: Decision boundary sensitivity — how threshold selection affects treatment area
- **Output**: `step4_result.png`
