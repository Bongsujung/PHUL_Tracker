import streamlit as st
import json
import os

# 기본 루틴 초기값
default_schedule = {
    "Monday_Upper_Power": [
        {"name": "벤치프레스", "reps_range": (3, 5), "sets": 3, "weight": 90, "current_reps": 3},
        {"name": "바벨로우", "reps_range": (3, 5), "sets": 3, "weight": 100, "current_reps": 3},
        {"name": "오버헤드 프레스", "reps_range": (3, 5), "sets": 3, "weight": 50, "current_reps": 3},
        {"name": "랫풀다운", "reps_range": (3, 5), "sets": 3, "weight": 60, "current_reps": 3},
        {"name": "바벨 컬", "reps_range": (3, 5), "sets": 3, "weight": 30, "current_reps": 3},
        {"name": "스컬 크러셔", "reps_range": (3, 5), "sets": 3, "weight": 30, "current_reps": 3}
    ],
    "Tuesday_Lower_Power": [
        {"name": "스쿼트", "reps_range": (3, 5), "sets": 3, "weight": 120, "current_reps": 3},
        {"name": "데드리프트", "reps_range": (3, 5), "sets": 3, "weight": 140, "current_reps": 3},
        {"name": "레그 프레스", "reps_range": (3, 5), "sets": 3, "weight": 180, "current_reps": 3},
        {"name": "레그 컬", "reps_range": (3, 5), "sets": 3, "weight": 50, "current_reps": 3},
        {"name": "시티드 카프 레이즈", "reps_range": (3, 5), "sets": 3, "weight": 40, "current_reps": 3}
    ],
    "Thursday_Upper_Hypertrophy": [
        {"name": "인클라인 벤치", "reps_range": (8, 12), "sets": 3, "weight": 70, "current_reps": 8},
        {"name": "덤벨 플라이", "reps_range": (8, 12), "sets": 3, "weight": 15, "current_reps": 8},
        {"name": "원암 덤벨 로우", "reps_range": (8, 12), "sets": 3, "weight": 25, "current_reps": 8},
        {"name": "랫풀다운", "reps_range": (8, 12), "sets": 3, "weight": 60, "current_reps": 8},
        {"name": "덤벨 컬", "reps_range": (8, 12), "sets": 3, "weight": 12, "current_reps": 8},
        {"name": "해머 컬", "reps_range": (8, 12), "sets": 3, "weight": 12, "current_reps": 8},
        {"name": "케이블 푸시 다운", "reps_range": (8, 12), "sets": 3, "weight": 25, "current_reps": 8},
        {"name": "오버헤드 익스텐션", "reps_range": (8, 12), "sets": 3, "weight": 20, "current_reps": 8}
    ],
    "Friday_Lower_Hypertrophy": [
        {"name": "레그프레스", "reps_range": (10, 15), "sets": 3, "weight": 160, "current_reps": 10},
        {"name": "레그 익스텐션", "reps_range": (10, 15), "sets": 3, "weight": 50, "current_reps": 10},
        {"name": "루마니안 데드리프트", "reps_range": (10, 15), "sets": 3, "weight": 90, "current_reps": 10},
        {"name": "레그 컬", "reps_range": (10, 15), "sets": 3, "weight": 50, "current_reps": 10},
        {"name": "스탠딩 카프 레이즈", "reps_range": (10, 15), "sets": 3, "weight": 40, "current_reps": 10},
        {"name": "시티드 카프 레이즈", "reps_range": (10, 15), "sets": 3, "weight": 40, "current_reps": 10}
    ]
}

LOG_FILE = "phul_log.json"

# 저장
def save_progress(data):
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

# 불러오기
def load_progress():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return default_schedule

# 더블 프로그레션 로직
def double_progression(ex, success):
    if success:
        if ex["current_reps"] < ex["reps_range"][1]:
            ex["current_reps"] += 1
        else:
            ex["weight"] += 2.5
            ex["current_reps"] = ex["reps_range"][0]
    return ex

# Streamlit UI 시작
st.set_page_config(page_title="PHUL 트래커", layout="centered")
st.title("🏋️ PHUL 프로그램 트래커")

# 스케줄 불러오기
schedule = load_progress()
days = list(schedule.keys())
selected_day = st.selectbox("📆 오늘의 루틴을 선택하세요", days)

# 사이드바에 초기 중량 설정 폼 추가
with st.sidebar.form("initial_weight_form"):
    st.header("📌 초기 중량 설정")
    weight_inputs = {}
    for i, ex in enumerate(schedule[selected_day]):
        weight_inputs[ex["name"]] = st.number_input(
            f"{ex['name']} 중량 (kg)",
            min_value=0.0,
            value=float(ex["weight"]),
            step=0.5,
            key=f"init_weight_{i}"
        )
    submitted = st.form_submit_button("초기 중량 저장")
    if submitted:
        for i, ex in enumerate(schedule[selected_day]):
            schedule[selected_day][i]["weight"] = weight_inputs[ex["name"]]
        save_progress(schedule)
        st.sidebar.success("초기 중량이 저장되었습니다.")

st.subheader(f"📋 {selected_day.replace('_', ' ')} 루틴")

updated = False

# 루틴별 운동 반복
for i, ex in enumerate(schedule[selected_day]):
    with st.expander(f"▶ {ex['name']}"):
        st.text(f"🔧 현재 중량: {ex['weight']}kg")
        st.text(f"🔁 반복수: {ex['current_reps']}회")
        st.text(f"📦 세트수: {ex['sets']}세트")
        success = st.radio("해당 세트를 모두 성공했습니까?", [True, False], key=f"{i}_success")
        if st.button("🔄 업데이트", key=f"{i}_update"):
            schedule[selected_day][i] = double_progression(ex, success)
            updated = True
            st.success("✅ 업데이트 완료!")

# 저장
if updated:
    save_progress(schedule)
    st.info("💾 변경사항이 저장되었습니다.")

# 전체 데이터 보기
st.markdown("---")
if st.button("📜 전체 운동 기록 보기"):
    st.json(schedule)

# 종료 메시지
st.markdown("Bong su Jung provided this program.")
st.markdown("이 프로그램은 PHUL 프로그램을 기반으로 하며, 중량 상승과 근비대에 초점을 둡니다")
st.markdown("Email : qhd0330@inu.ac.kr")