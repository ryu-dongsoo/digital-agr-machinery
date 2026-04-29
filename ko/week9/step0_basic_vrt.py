"""
09주차 실습 Step 0: VRT(변량 제어) 기초 로직 이해
- 직관적인 4x4 소형 가상 밭 데이터를 직접 생성
- 각 칸(셀)의 NDVI 값을 바탕으로 비료 처방량 할당
- 전체 필요한 비료량 합산 계산
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# 1. 4x4 소형 가상 NDVI 밭 데이터 (직접 입력)
# 직관적으로 왼쪽 위는 생육 우수(0.9), 오른쪽 아래는 불량(0.2)
ndvi_data = np.array([
    [0.9, 0.8, 0.4, 0.3],
    [0.8, 0.7, 0.3, 0.2],
    [0.5, 0.4, 0.6, 0.5],
    [0.3, 0.2, 0.7, 0.8]
])

# 2. 구역(Zone)별 처방량(Rate) 할당 로직
rate_data = np.zeros_like(ndvi_data)

for i in range(4):
    for j in range(4):
        val = ndvi_data[i, j]
        if val < 0.4:
            rate_data[i, j] = 150  # Zone 1: 생육 불량 (보충 시비)
        elif val < 0.7:
            rate_data[i, j] = 100  # Zone 2: 생육 보통 (표준 시비)
        else:
            rate_data[i, j] = 50   # Zone 3: 생육 우수 (시비 절감)

# 3. 비료 소모량 총합 계산
total_fertilizer = np.sum(rate_data)
print(f"✅ 해당 구역(4x4)에 필요한 총 비료량: {total_fertilizer} kg")

# 4. 결과 시각화 (값 표시 포함)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.imshow(ndvi_data, cmap='RdYlGn', vmin=0, vmax=1)
ax1.set_title("Input: NDVI Data")
# 각 칸에 실제 수치 표시
for (j, i), label in np.ndenumerate(ndvi_data):
    ax1.text(i, j, f"{label:.1f}", ha='center', va='center', color='black')

ax2.imshow(rate_data, cmap='YlOrRd')
ax2.set_title("Output: Fertilizer Rate (kg/ha)")
# 각 칸에 실제 수치 표시
for (j, i), label in np.ndenumerate(rate_data):
    ax2.text(i, j, int(label), ha='center', va='center', color='black')

plt.tight_layout()
output_dir = os.path.dirname(os.path.abspath(__file__))
output_img = os.path.join(output_dir, "step0_basic_vrt_result.png")
plt.savefig(output_img, dpi=300)
print(f"✅ 시각화 이미지 저장 완료: {output_img}")
# plt.show() # 서버/자동화 환경을 위해 주석 처리
