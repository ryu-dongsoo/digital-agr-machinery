# 🚜 디지털농업기계개론 실습 포트폴리오 (Korean)

> **Author / Rights Holder:** 전북대학교 생물산업기계공학과 유동수 (ryudongsoo@jbnu.ac.kr)

> **강의:** 유동수 (전북대학교 생물산업기계공학과)  
> **[English Version Link](../en/README.md)**

본 디렉토리는 **디지털농업기계개론** 수업의 주차별 실습 자료를 포함하고 있습니다. 각 주차별 폴더에는 파이썬 실습 코드와 실습 매뉴얼이 포함되어 있습니다.

---

## 🗓️ 주차별 실습 목록

| 주차 | 주제 | 핵심 내용 | 소스 코드 |
|:---:|---|---|:---:|
| **02** | **트랙터 동력 및 경제성 분석** | 디젤 vs 전기 트랙터의 10년 총소유비용(TCO) 시뮬레이션 | [Link](week2/) |
| **03** | **농기계 통신 (CAN & ISOBUS)** | J1939 CAN ID 분석 및 PGN/SPN 데이터 디코딩 실습 | [Link](week3/) |
| **04** | **GNSS 측위 및 경로 계획** | RTK 보정 원리 및 A-B Line 기반 작업 경로 생성 | [Link](week4/) |
| **05** | **광학 센서 및 NDVI 분석** | 멀티스펙트럼 영상 데이터를 활용한 식생지수 산출 및 지도화 | [Link](week5/) |
| **06** | **3D 공간 인식 (LiDAR)** | Point Cloud 데이터 처리 및 작물 구조적 표현형 분석 | [Link](week6/) |
| **07** | **스마트팜 제어 시스템** | 센서 기반 환경 모니터링 및 PID 기반 수량 제어 | [Link](week7/) |
| **09** | **VRT 처방 지도 작성** | 처방 지도(Rx Map) 기반 가변 변량 제어(VRT) 적용 시뮬레이션 | [Link](week9/) |
| **10** | **농업용 드론(UAV) 비행 제어** | 자동 비행 경로(Waypoint) 생성 및 방제 시뮬레이션 | [Link](week10/) |
| **11** | **자율주행 경로 추종 시뮬레이션** | 전방 주시 거리(Ld) 튜닝에 따른 Pure Pursuit 조향 성능 분석 | [Link](week11/) |
| **12** | **필드 로봇 및 엔드 이펙터** | 2-DOF 기구학 연산 및 소프트 그리퍼 형태 순응성 시뮬레이션 | [Link](week12/) |
| **13** | **농업 인공지능(AI) 및 데이터 분석** | No-Code AI (Teachable Machine) 기반 작물/잡초 판독 모델 구축 | [Link](week13/) |
| **14** | **시스템 통합 및 산업 분석** | 글로벌 상용화 기술 분석 및 차세대 디지털 농업 시스템 설계 | [Link](week14/) |

---

## 🚀 시작하기

> 📌 **처음 실습을 시작하는 학생은 [실습 환경 설정 가이드](실습_환경_설정_가이드.md)를 먼저 참고**

### 1단계: 기본 환경 설치

- **Python 3.11+**, **VS Code**, **Git** 설치 필요
- 상세 절차 → [실습 환경 설정 가이드](실습_환경_설정_가이드.md)

### 2단계: 실습 자료 다운로드

```bash
git clone https://github.com/ryu-dongsoo/digital-agr-machinery.git
```

### 3단계: Python 패키지 설치

#### 필수 패키지 (전 주차 공통)

```bash
pip install numpy matplotlib
```

#### 주차별 추가 패키지

| 주차 | 추가 패키지 | 설치 명령 | 비고 |
|:---:|-----------|----------|------|
| **03** | *(추가 패키지 없음)* | — | 표준 라이브러리만 사용 |
| **05** | `rasterio` | `pip install rasterio` | GeoTIFF 영상 처리 |
| **09** | `geopandas`, `shapely` | `pip install geopandas shapely` | GeoJSON 처방 지도 생성 |
| **13** | `opencv-python`, `tensorflow` | `pip install opencv-python tensorflow` | AI 모델 로드 및 추론 |
| **13** | `ultralytics` | `pip install ultralytics` | YOLO 객체 탐지 (선택) |

> ⚠️ **일괄 설치 명령** (전체 패키지를 한 번에 설치할 경우):
> ```bash
> pip install numpy matplotlib rasterio geopandas shapely opencv-python tensorflow ultralytics
> ```

### 4단계: 실습 진행

1. 해당 주차 폴더의 **실습 매뉴얼(`*.md`)** 먼저 읽기
2. `step0_xxx.py` → `step1_xxx.py` → ... 순서대로 실행
3. 매뉴얼 지시에 따라 파라미터 변경 및 결과 관찰
4. 결과 스크린샷 캡처 (`Win+Shift+S`) → 보고서에 첨부

### 5단계: 보고서 제출

- **GitHub Issue**를 통해 제출 → [제출 가이드](실습_환경_설정_가이드.md#8-실습-보고서-제출-github-issue)
- 제목 형식: `[WeekXX] 학번_이름_실습보고서`

### 6단계: 퀴즈 및 토론

- **[심화 토론 & 퀴즈 뱅크](QUIZ_BANK.md)**를 통해 개념 복습

---

## 📞 연락처 및 지원
- **교수**: 유동수 (ryudongsoo@jbnu.ac.kr)
- **연구실**: 전북대학교 농업생명과학대학 4호관 311호 (ASRL)

---
*© 2026 Jeonbuk National University. All rights reserved.*

## 📝 변경 이력 (Changelog)
- **2026-05-15 04:22:00** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Week 14 System Integration and Industry Analysis materials
- **2026-05-15 03:36:00** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Week 13 Agricultural AI lab materials and Quiz/Report
- **2026-05-15 03:15:00** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Week 12 Field Robot and End-effector lab materials
- **2026-05-07 15:19:18** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Update video title to explicitly mention Daedong vs John Deere comparison
- **2026-05-07 15:18:35** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add second Daedong AI Tractor video to lab manuals
- **2026-05-07 15:15:47** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Daedong AI Tractor YouTube video link to lab manuals
- **2026-05-07 15:11:58** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Merge tracking algorithms into path_tracking_compare.py with 3x animation speed
- **2026-05-07 15:03:14** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Stanley method simulator and animation explanations
