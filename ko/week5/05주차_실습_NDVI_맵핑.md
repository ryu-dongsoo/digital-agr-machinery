# 05주차 실습: 다중분광 데이터 기반 NDVI 맵핑 및 가변처방 분할

## 🎯 실습 개요
- **목표**: 드론 다중분광 센서(NIR, RED 밴드) 데이터 기반 NDVI(정규화 식생 지수) 산출 및 시각화 구현
- **개발 환경**: Python 3.x (주요 라이브러리: `rasterio`, `numpy`, `matplotlib`, `scipy`)
- **실습 형태**: QGIS GUI 조작을 파이썬 코드로 자동화하는 예제 클론 코딩

---

## 🛠 실습 단계별 안내

### [Step 1] `step1_ndvi_calculation.py` (NDVI 수치 연산)
- **목적**: 2개의 단일 밴드 TIF 파일(RED, NIR)을 읽어 식생 지수 수식 적용
- **주요 문법**: 
  - `rasterio.open()`을 통한 공간 데이터 로드
  - Numpy 배열 연산 기반 식생 지수 도출: `(NIR - RED) / (NIR + RED)`
  - 영점 분모(ZeroDivision) 방장 안전 장치(`np.where` 활용)
- **출력물**: `-1.0` ~ `1.0` 사이의 실수 배열(Float32 array)

### [Step 2] `step2_colormap_visualization.py` (다중 밴드 3분할 시각화)
- **목적**: 원본 센서 이미지(RED, NIR)와 수학적 결과물(NDVI)을 동시에 비교하여 픽셀의 원리 직관적 체득
- **주요 문법**:
  - `matplotlib.pyplot.subplots(1, 3)`을 통한 3단 분할 뷰
  - RED 밴드(가시광 흡수)와 NIR 밴드(근적외선 강한 반사)의 흑백 특성 대조
  - 결과 NDVI에만 `RdYlGn`(Red-Yellow-Green) 컬러맵 적용하여 결과물 극대화

### [Step 3] `step3_polygon_extraction.py` (고정 임계값 마스킹 방제 구역 분할)
- **목적**: 맵 좌표 데이터를 트랙터가 인식할 수 있는 디지털 이진 마스크(0과 1)로 변환
- **주요 문법**:
  - 조건문(`0.2 < NDVI < threshold`) 복합 인스턴싱 추출
  - 추출된 Boolean 배열을 방제 분사(Spray) 명령용 정수형으로 형변환

### [Step 4] `step4_interactive_ndvi_slider.py` (동적 임계값 인터랙티브 실습)
- **목적**: 개발자가 설정한 고정값이 아닌, 사용자의 마우스 조작(Slider)에 따라 방제 마스크가 실시간으로 붉게 투영되는 원리 체험
- **주요 문법**:
  - `matplotlib.widgets.Slider` 모듈 활용
  - 슬라이더 조작 이벤트 콜백(Callback) 처리를 통한 화면 실시간 재연산(`val_update`)
  - 임계값의 높낮이에 따라 병반 오진율이나 방제 면적이 시각적으로 어떻게 증감하는지 토론 과제로 연계 가능

---

## ⚠️ 주의 사항
- **라이브러리 사전 설치 제한**: `pip install rasterio numpy matplotlib scipy` 완료 필수
- 경로 이슈 방지를 위해 스크립트와 동일 폴더에 테스트용 다중분광 이미지(예: `red.tif`, `nir.tif`) 위치 권장
