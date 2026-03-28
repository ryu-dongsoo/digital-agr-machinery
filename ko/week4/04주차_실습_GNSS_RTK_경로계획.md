# 04주차 실습: GNSS 정밀 측위 & A-B Line 경로 계획

## 🎯 실습 개요
- **목표**: GNSS 삼변측량 원리를 시각적으로 체험하고, RTK 보정의 효과와 A-B Line 경로 계획의 경제성을 정량적으로 분석
- **형식**: 단계별 Python 시뮬레이션 (numpy + matplotlib)
- **사전 준비**: Python 3.x

---

## 💻 [Step 1] `step1_gnss_trilateration.py`
- **목적**: 위성 4개의 거리 원이 교차하여 수신기 위치를 결정하는 삼변측량 원리 시각화
- **3개 패널 구성**:
  - ① 이상적 삼변측량 (오차 0) — 원들이 정확히 한 점에서 교차
  - ② 현실 GNSS — 대기 오차로 원이 어긋나 위치 산점도 형성
  - ③ Multi-Constellation 효과 — 위성 수 증가에 따른 오차 감소 추이
- **출력**: `step1_result.png`

## 💻 [Step 2] `step2_rtk_vs_gnss.py`
- **목적**: 일반 GNSS(2~5m 오차) vs RTK(2cm 오차)로 트랙터가 고랑을 따라 주행 시 경로 차이 비교
- **핵심 개념**: Cross-track Error(횡방향 이탈), 작물 피해 비율 정량화
- **4개 패널 구성**:
  - 상단: GNSS 궤적 vs RTK 궤적 (고랑 위 주행 시각화)
  - 하단: 횡방향 이탈 오차 시계열 비교
- **출력**: `step2_result.png`

## 💻 [Step 3] `step3_abline_path_planning.py`
- **목적**: 가상 농지(사다리꼴, ~1.2ha)에 A-B Line 기준 평행 패스 자동 생성 & 경제성 분석
- **3가지 시나리오 비교**: 초보 운전자(50cm 겹침) vs 숙련 운전자(20cm 겹침) vs RTK(2cm 겹침)
- **6개 패널 구성**:
  - 상단: 3개 시나리오별 농지 + 패스 시각화
  - 하단: 비용 비교, 작업 시간 비교, RTK 투자 회수(ROI) 분석
- **출력**: `step3_result.png`
