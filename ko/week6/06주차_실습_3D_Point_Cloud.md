# 06주차 실습: 3D Point Cloud 탐색 및 수간 지표 추정

## 🎯 실습 개요
- **목표**: 트랙터 탑재 LiDAR의 작동 원리를 애니메이션으로 체험하고, 수집된 3D Point Cloud에서 작물 형질을 자동 추출
- **실습 형태**: 파이썬 시뮬레이션(Step 1: LiDAR 스캐닝 애니메이션) → 데이터 분석(Step 2: 3D Phenotyping)
- **준비물**: Python 3.x (`numpy`, `matplotlib`)
- **비고**: Open3D 미설치 환경에서도 Matplotlib 3D 기반으로 완벽 실행 가능

---

## 💻 [Step 1] `step1_lidar_scanning_simulation.py`

### 목적
- 과수원 통로를 주행하는 **트랙터에 장착된 LiDAR**가 레이저 빔을 발사하여 3D Point Cloud를 실시간으로 구축하는 과정을 애니메이션으로 시각화

### 학습 포인트
- LiDAR의 ToF(Time-of-Flight) 원리의 직관적 체험
- Point Cloud가 '점 하나하나가 레이저 한 발의 반사점'임을 시각적으로 확인
- 트랙터 이동에 따라 3D 지도가 점진적으로 완성되는 SLAM 개념 체득

### 시뮬레이션 구성
- **좌측 패널**: 2D 탑뷰 — 트랙터 위치(빨간 사각형), LiDAR 스캔 범위(노란 원), 과수원 나무 배치(녹색)
- **우측 패널**: 3D 뷰 — 누적 Point Cloud가 실시간으로 쌓이며 높이(Height Ramp) 컬러맵 적용

### 출력 파일
- `scanned_orchard.npy`: 누적된 Point Cloud 데이터 (Step 2에서 재사용)
- `step1_result.png`: 최종 스캔 결과 캡처 이미지

---

## 💻 [Step 2] `step2_tree_phenotyping.py`

### 목적
- Step 1에서 수집한 Point Cloud를 자동 분석하여 **개별 나무의 수고(Height)와 수관 폭(Canopy Spread)** 추출

### 학습 포인트
- Grid 기반 세그멘테이션으로 개별 나무 자동 탐지
- 바운딩 박스(AABB)를 이용한 작물 치수 자동 산출
- 수작업 측정 대비 자동화의 효율성 체감

### 시각화 구성
- **좌측 패널**: 2D 탑뷰 — 탐지된 각 나무 위치에 빨간 바운딩 박스 + 수고 라벨 표시
- **우측 패널**: 3D 뷰 — 높이 컬러맵 + 반투명 빨간 바운딩 박스 오버레이

### 콘솔 출력
- 전체 나무 목록(중심좌표, 수고, 수관 폭) 테이블 형식 출력
- 평균/표준편차 통계 요약

### 출력 파일
- `step2_result.png`: 3D Phenotyping 자동 측정 결과 캡처 이미지
