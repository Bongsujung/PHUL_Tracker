# 🏋️ PHUL Tracker (Power Hypertrophy Upper Lower)

**PHUL Tracker**는 파워와 근비대를 목표로 한 고전적인 PHUL(2분할 4회 루틴) 프로그램을 웹에서 트래킹할 수 있도록 설계된 **Streamlit 기반의 운동 자동화 프로그램**입니다.  
각 세션의 운동을 기록하고, **더블 프로그레션 전략(반복수 → 중량)**에 따라 자동으로 중량을 증가시켜 **안전하고 체계적인 근성장**을 도와줍니다.

---

## 📋 PHUL 프로그램 개요

- **PHUL**: Power Hypertrophy Upper Lower의 약자
- **주 4회 루틴**: 상체(파워), 하체(파워), 상체(하이퍼트로피), 하체(하이퍼트로피)
- **운동 구성**: 5대 복합운동 + 보조 운동 포함
- **진행 방식**: 고중량 저반복 → 중간 중량 고반복 → 점진적 과부하

| 요일      | 루틴 이름               | 목적         |
|-----------|------------------------|--------------|
| 월요일    | Monday_Upper_Power     | 근력 (고중량) |
| 화요일    | Tuesday_Lower_Power    | 근력 (고중량) |
| 목요일    | Thursday_Upper_Hypertrophy | 근비대 (중량) |
| 금요일    | Friday_Lower_Hypertrophy  | 근비대 (중량) |

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
cd phul-tracker
pip3 install streamlit 
streamlit run PHUL.py