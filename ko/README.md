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

---

## 🚀 시작하기

1. **환경 설정**:
   ```bash
   pip install numpy matplotlib pandas opencv-python
   ```

2. **실습 진행**:
   각 주차별 폴더의 `*.md` 매뉴얼을 읽고 가이드에 따라 실습 코드를 실행합니다.

3. **퀴즈 및 토론**:
   본 저장소의 **[심화 토론 & 퀴즈 뱅크](QUIZ_BANK.md)**를 통해 개념을 복습하십시오.

---

## 📞 연락처 및 지원
- **교수**: 유동수 (ryudongsoo@jbnu.ac.kr)
- **연구실**: 전북대학교 농업생명과학대학 4호관 311호 (ASRL)

---
*© 2026 Jeonbuk National University. All rights reserved.*

## 📝 변경 이력 (Changelog)
- **2026-05-07 15:19:18** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Update video title to explicitly mention Daedong vs John Deere comparison
- **2026-05-07 15:18:35** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add second Daedong AI Tractor video to lab manuals
- **2026-05-07 15:15:47** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Daedong AI Tractor YouTube video link to lab manuals
- **2026-05-07 15:11:58** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Merge tracking algorithms into path_tracking_compare.py with 3x animation speed
- **2026-05-07 15:03:14** [[ryu-dongsoo](mailto:ryudongsoo@jbnu.ac.kr)] Add Stanley method simulator and animation explanations
