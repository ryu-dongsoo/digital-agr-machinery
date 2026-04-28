"""
09주차 실습: 변량 제어(VRT) 처방 지도 생성 파이썬 실습
- 가상의 NDVI 밭 데이터를 생성하고 구역(Zone)을 나눔
- 구역별 처방량(Rate)을 할당하여 GeoJSON 벡터 데이터로 저장
"""

import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os

# 1. 가상 NDVI 데이터 생성 (10x10 그리드 밭)
np.random.seed(42)
# 중심부는 생육이 좋고(0.8), 가장자리는 불량한(0.3) 가상의 데이터 시뮬레이션
x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
ndvi_base = 0.8 - 0.4 * (x**2 + y**2)
# 노이즈 추가
ndvi_data = ndvi_base + np.random.normal(0, 0.05, (10, 10))
ndvi_data = np.clip(ndvi_data, 0.0, 1.0) # 0~1 사이로 클리핑

# 2. Zoning (등급화) 및 처방량 할당
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

# 3. 벡터화 (Polygon 생성 및 GeoDataFrame 구성)
polygons = []
rates = []
zones = []

# 좌표 스케일 설정 (가상 좌표: 한 픽셀당 10m x 10m)
pixel_size = 10 

for i in range(ndvi_data.shape[0]):
    for j in range(ndvi_data.shape[1]):
        x_coord = j * pixel_size
        y_coord = -i * pixel_size # y좌표는 위에서 아래로
        
        # 사각형 폴리곤 꼭짓점 구성
        poly = Polygon([
            (x_coord, y_coord),
            (x_coord + pixel_size, y_coord),
            (x_coord + pixel_size, y_coord - pixel_size),
            (x_coord, y_coord - pixel_size)
        ])
        polygons.append(poly)
        rates.append(rate_data[i, j])
        zones.append(zone_data[i, j])

# GeoDataFrame 생성
gdf = gpd.GeoDataFrame({
    'Zone': zones,
    'Rate_kg_ha': rates
}, geometry=polygons)

# 현재 스크립트 실행 경로를 기준으로 저장 폴더 지정
output_dir = os.path.dirname(os.path.abspath(__file__))

# 4. 파일 내보내기 (GeoJSON)
# GeoJSON은 Shapefile보다 단일 파일로 다루기 편함
output_filename = os.path.join(output_dir, "vrt_rx_map.geojson")
gdf.to_file(output_filename, driver="GeoJSON")
print(f"✅ 처방 지도 생성 완료: {output_filename}")

# 5. 시각화 (Matplotlib)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 원본 NDVI 플롯
im1 = ax1.imshow(ndvi_data, cmap='RdYlGn', vmin=0, vmax=1)
ax1.set_title("Original NDVI Map (Virtual Data)")
fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)

# 처방량(Rate) 지도 플롯 (GeoPandas 내장 기능 활용)
gdf.plot(column='Rate_kg_ha', cmap='YlOrRd', legend=True, ax=ax2, edgecolor='black')
ax2.set_title("VRT Prescription Map (Rate: kg/ha)")
ax2.axis('off')

plt.tight_layout()
output_img = os.path.join(output_dir, "vrt_rx_map.png")
plt.savefig(output_img, dpi=300)
print(f"✅ 시각화 이미지 저장 완료: {output_img}")
# plt.show() # 서버 환경이나 비대화형 환경에서 멈춤 방지를 위해 주석 처리
