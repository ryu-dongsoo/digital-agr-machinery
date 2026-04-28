# Week 09 Lab: Generating VRT (Variable Rate Technology) Prescription Maps

## 🎯 Lab Overview
- **Objective**: Allocation of zone-based application rates based on optical sensor NDVI data and automated generation of prescription maps
- **Lab Format**: Python data processing and vector spatial map (GeoJSON) extraction
- **Learning Algorithm**: Virtual data construction → Zoning → Rate assignment → Spatial data (Polygon) conversion and output

---

## 🛠 [Step 0] Lab Environment Setup

### Required Libraries
- `numpy`: Array calculations and virtual NDVI raster data generation
- `geopandas`: Vector spatial data processing and GeoJSON conversion
- `shapely`: Location-based Polygon geometry construction
- `matplotlib`: Result visualization

### Installation Command
```bash
pip install numpy geopandas shapely matplotlib
```

---

## 💻 [Step 1] NDVI Data Zoning Strategy

### Operating Principle
- Simplification of NDVI raster data (0.0 ~ 1.0 range) into 3 zones
- Application of inverse control strategy: increased fertilizer in poor growth zones, reduced fertilizer in excellent growth zones

### Zoning and Application Rate Criteria
| Grade | NDVI Range | Growth Status | Prescription Strategy | Rate (kg/ha) |
|---|---|---|---|---|
| **Zone 1** | 0.0 ~ 0.4 | Poor | Supplemental fertilization (High) | 150 kg/ha |
| **Zone 2** | 0.4 ~ 0.7 | Normal | Standard fertilization (Medium) | 100 kg/ha |
| **Zone 3** | 0.7 ~ 1.0 | Excellent | Reduced fertilization (Low) | 50 kg/ha |

---

## 💻 [Step 2] Python Implementation of Prescription Map Conversion (`step1_vrt_prescription_map.py`)

### Operating Principle
- Extraction of zoned 2D pixel data (Raster) and conversion to Polygon objects using the `shapely` module
- Integration of Zone and Rate attributes into the `GeoDataFrame` data structure
- Output of standard format (GeoJSON) data compatible with tractor terminals (ISOBUS TC-GEO)

### Outputs
- `vrt_rx_map.geojson`: Spatial data directly compatible with GIS software (QGIS) and tractors
- `vrt_rx_map.png`: Visualized result image for verification

### Further Study and Limitations
- **Data size issue**: Exponential increase in spatial data file size during pixel-by-pixel polygon conversion
- **Field application correction**: Necessity of grid optimization tailored to tractor implement width (e.g., 24m) through pixel merging (Dissolve) and smoothing
