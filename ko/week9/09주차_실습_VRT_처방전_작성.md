# 09주차 실습: 변량 제어(VRT) 처방 지도(Prescription Map) 생성

## 🎯 실습 개요
- **목표**: 광학 센서 식생 지수(NDVI) 데이터 기반 구역별 처방량 할당 및 처방 지도 자동 생성
- **실습 형태**: Python 데이터 처리 기반 벡터 공간 지도(GeoJSON) 추출 실습
- **학습 알고리즘**: 가상 데이터 구성 → 구역화(Zoning) → 처방량(Rate) 부여 → 공간 데이터(Polygon) 변환 및 출력

---

## 🛠 [Step 0] 실습 환경 세팅

### 필요 라이브러리 
- `numpy`: 배열 연산 및 가상 NDVI 래스터 데이터 생성
- `geopandas`: 벡터 공간 데이터 처리 및 GeoJSON 변환
- `shapely`: 위치 정보 기반 폴리곤(Polygon) 형상 구성
- `matplotlib`: 결과물 시각화 

### 설치 명령어
```bash
pip install numpy geopandas shapely matplotlib
```

---

## 💻 [Step 1] [기초] 2D 배열 기반 처방량 계산 실습 (`step0_basic_vrt.py`)

### 실습 목적
- 복잡한 공간 데이터(GeoJSON, Polygon) 변환 전, 배열 연산을 통한 VRT 핵심 로직 파악
- 직관적인 4x4 소형 밭 데이터를 직접 입력하여 NDVI와 처방량의 상관관계 이해

### 동작 원리
- 4x4 크기의 2D 배열(`numpy.array`) 하드코딩을 통한 가상 NDVI 데이터 생성
- 배열 순회(loop) 및 조건문을 활용한 구역별 처방량(Rate) 할당
- 전체 구역의 총 필요 비료량 합산 및 데이터 시각화(수치 표기) 적용

---

## 💻 [Step 2] NDVI 데이터 구역화 (Zoning) 전략

### 동작 원리
- 0.0 ~ 1.0 범위 NDVI 래스터 데이터를 3단계 구역(Zone) 단순화
- 생육 불량 구역에 비료 투입량 증가, 생육 우수 구역에 비료 절감 적용 (역상관 제어 전략)

### Zoning 및 처방량 기준
| 등급 | NDVI 범위 | 생육 상태 | 처방 전략 | 처방량 (Rate) |
|---|---|---|---|---|
| **Zone 1** | 0.0 ~ 0.4 | 불량 | 보충 시비 (강) | 150 kg/ha |
| **Zone 2** | 0.4 ~ 0.7 | 보통 | 표준 시비 (중) | 100 kg/ha |
| **Zone 3** | 0.7 ~ 1.0 | 우수 | 시비 절감 (약) | 50 kg/ha |

---

## 💻 [Step 3] [심화] 처방 지도 벡터(GeoJSON) 변환 파이썬 구현 (`step1_vrt_prescription_map.py`)

### 동작 원리
- 구역화된 2D 픽셀 데이터(Raster) 추출 후 `shapely` 모듈 활용 폴리곤(Polygon) 객체 변환
- `GeoDataFrame` 자료구조에 구역(Zone), 처방량(Rate) 속성 결합
- 트랙터 단말기(ISOBUS TC-GEO) 호환용 표준 포맷(GeoJSON) 데이터 출력

### 산출물 (Output)
- `vrt_rx_map.geojson`: GIS 소프트웨어(QGIS) 및 트랙터 직접 호환 공간 데이터
- `vrt_rx_map.png`: 시각화 검증용 결과 이미지

### 추가 학습 및 한계점
- **데이터 용량 문제**: 개별 픽셀 단위 폴리곤 변환 시 공간 데이터 파일 크기 기하급수적 증가 
- **현장 적용 보정**: 픽셀 병합(Dissolve) 및 스무딩(Smoothing)을 통한 트랙터 작업기 폭(예: 24m) 맞춤형 그리드 최적화 필요
