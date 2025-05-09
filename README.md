# 🏋️ PHUL Tracker (Power Hypertrophy Upper Lower)

**PHUL Tracker**는 파워와 근비대를 목표로 한 고전적인 PHUL(2분할 4회 루틴) 프로그램을 웹에서 트래킹할 수 있도록 설계된 **Streamlit 기반의 운동 자동화 프로그램**입니다.  
각 세션의 운동을 기록하고, **더블 프로그레션 전략(반복수 → 중량)**에 따라 자동으로 중량을 증가시켜 **안전하고 체계적인 근성장**을 도와줍니다.

---

## 📋 PHUL 프로그램 개요 (Power Hypertrophy Upper Lower)

**PHUL**은 "Power Hypertrophy Upper Lower"의 약자로, 주 4일 기준 **상체/하체 분할 루틴**과 **근력(power) vs. 근비대(hypertrophy)** 개념을 결합한 프로그램입니다.  
전 세계적으로 많은 운동 초중급자 및 중상급자가 사용하며, 특히 **근력과 근육량을 균형 있게 향상**시키는 데 최적화되어 있습니다.

---

### 🔹 루틴 구성 방식

| 요일 | 루틴 이름 | 주요 목적 | 반복수 범위 | 중량 특성 |
|------|-----------|-----------|-------------|------------|
| 월요일 | Monday_Upper_Power | 상체 파워 | 3–5회 | 고중량 |
| 화요일 | Tuesday_Lower_Power | 하체 파워 | 3–5회 | 고중량 |
| 수요일 | 휴식 |  – | – | – |
| 목요일 | Thursday_Upper_Hypertrophy | 상체 근비대 | 8–15회 | 중간중량 |
| 금요일 | Friday_Lower_Hypertrophy | 하체 근비대 | 8–15회 | 중간중량 |
| 주말 | 휴식 | – | – | – |

---

### 🔸 운동 설계 원리

PHUL은 다음 3가지 과학적 근비대 메커니즘을 모두 반영합니다:

1. **기계적 장력 (Mechanical Tension)**  
   → 고중량 저반복 복합운동 (벤치프레스, 스쿼트, 데드리프트 등)

2. **대사 스트레스 (Metabolic Stress)**  
   → 중간 중량 고반복 운동 (8–15회), 펌핑 유도

3. **근육 손상 (Muscle Damage)**  
   → 다양한 각도와 움직임의 분리 운동 (플라이, 익스텐션 등)

---

### 🔸 점진적 과부하 (Double Progression)

PHUL 프로그램의 핵심은 **반복수 우선 과부하 + 중량 증가 전략**입니다:

- 매 운동은 반복수 범위를 가지며 (예: 3~5회)
- 최하치(3회)부터 시작해 성공 시 다음 주에 반복수 증가
- 최고치(5회)까지 도달하면 **중량 +2.5kg**, 반복수는 다시 하한으로 리셋

이 방식은:
- 빠르진 않지만 **장기적 근성장에 가장 안전하고 견고한 방식**이며
- 본 프로그램에서는 이를 자동으로 적용해줍니다.

---

### 🔸 본 프로그램에서의 구현 방식

이 트래커는 PHUL 루틴을 정확히 반영하며 다음과 같은 방식으로 구성되어 있습니다:

- ✅ **요일별 운동 루틴 자동 로딩**
- ✅ 각 운동별 중량/반복수/세트 수 표시
- ✅ 사용자가 성공 여부를 입력하면 → 반복수 or 중량 자동 갱신
- ✅ JSON 파일에 누적 기록 저장
- ✅ Streamlit 기반 GUI 제공으로 마우스 클릭만으로 사용 가능
- ✅ 사이드바에서 운동별 **초기 중량 설정** 가능

---

## ✅ 기능 요약

- 📅 **요일별 루틴** 자동 구성 및 시각화
- 🏷️ 각 운동의 **중량 / 반복 수 / 세트 수** 실시간 입력
- 🔁 **더블 프로그레션** 적용 (반복수 → 중량 자동 상승)
- 💾 **자동 저장** 기능 (`phul_log.json`)
- 🧠 **초기 중량 설정** 인터페이스 제공 (사이드바)
- 🔓 오픈소스 Streamlit 기반

---

## ⚙️ 설치 방법

### 1. 프로젝트 클론
```bash
git clone https://github.com/yourusername/phul-tracker.git
pip3 install streamlit 
streamlit run PHUL.py