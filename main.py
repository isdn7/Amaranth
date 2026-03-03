import streamlit as st
import pandas as pd
import io
import csv
import os

# 1. 페이지 설정 (가로로 넓게 사용)
st.set_page_config(layout="wide", page_title="교사 시간표 와이드 보드")

# 2. CSS 수정: 오타 해결 (unsafe_allow_html로 변경)
st.markdown("""
    <style>
    /* 버튼 내부 텍스트 크기 조절 및 여백 최소화 */
    .stButton > button {
        padding: 2px 2px !important;
        font-size: 11px !important;
        height: 60px !important;
        min-width: 45px !important;
        line-height: 1.2 !important;
    }
    /* 컬럼 간 간격 좁히기 */
    div[data-testid="stHorizontalBlock"] {
        gap: 2px !important;
    }
    </style>
    """, unsafe_allow_html=True) # <-- 이 부분의 오타를 수정했습니다!

# 3. 데이터 로드 함수 (data.txt 파일 읽기)
def load_data_from_file(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # 교사명 + 월(6) + 화(7) + 수(6) + 목(6) + 금(7) = 총 33개 컬럼
    columns = ['교사명', 
               '월1', '월2', '월3', '월4', '월5', '월6', 
               '화1', '화2', '화3', '화4', '화5', '화6', '화7',
               '수1', '수2', '수3', '수4', '수5', '수6',
               '목1', '목2', '목3', '목4', '목5', '목6',
               '금1', '금2', '금3', '금4', '금5', '금6', '금7']
    
    f_io = io.StringIO(text.strip())
    reader = csv.reader(f_io, delimiter='\t', quotechar='"')
    rows = []
    for row in reader:
        if not row or "교사명" in row[0]: continue
        clean_row = [cell.strip() for cell in row]
        # 부족한 칸 채우기
        if len(clean_row) < 33:
            clean_row += [""] * (33 - len(clean_row))
        else:
            clean_row = clean_row[:33]
        rows.append(clean_row)
    return pd.DataFrame(rows, columns=columns)

# 데이터 초기화
if 'df' not in st.session_state:
    df_loaded = load_data_from_file("data.txt")
    if df_loaded is not None:
        st.session_state.df = df_loaded
    else:
        st.error("'data.txt' 파일을 찾을 수 없습니다. 코드와 같은 폴더에 파일을 만들어주세요.")
        st.stop()
    st.session_state.buffer = []
    st.session_state.selected_chip_idx = None

df = st.session_state.df

# ---------------------------------------------------------
# UI: 상단 대기석
# ---------------------------------------------------------
st.title("🧲 시간표 와이드 자석 보드")
st.subheader("📥 현재 들고 있는 수업 (임시 대기석)")

if st.session_state.buffer:
    buf_cols = st.columns(len(st.session_state.buffer) + 1)
    for i, chip in enumerate(st.session_state.buffer):
        with buf_cols[i]:
            is_selected = (st.session_state.selected_chip_idx == i)
            style_label = "✅ 선택됨" if is_selected else "이 칩 선택"
            st.info(f"**{chip['teacher']}**\n{chip['lesson']}")
            if st.button(style_label, key=f"buf_{i}"):
                st.session_state.selected_chip_idx = i
                st.rerun()
else:
    st.write("옮길 수업을 아래에서 클릭하여 빼내세요.")

st.divider()

# ---------------------------------------------------------
# UI: 엑셀 스타일 와이드 보드 (가로 33열)
# ---------------------------------------------------------
# 교사 검색 필터
search_name = st.text_input("교사 검색 (이름을 입력하면 해당 교사만 나타납니다)", "")
view_df = df[df['교사명'].str.contains(search_name)] if search_name else df.head(10)

# 헤더 행 출력
header_cols = st.columns([1.5] + [1]*32)
header_cols[0].write("**교사명**")
for i, col_name in enumerate(df.columns[1:]):
    header_cols[i+1].write(f"**{col_name}**")

# 데이터 행 출력
for idx, row in view_df.iterrows():
    t_name = row['교사명']
    r_cols = st.columns([1.5] + [1]*32)
    
    # 교사 이름
    r_cols[0].write(f"**{t_name}**")
    
    # 32개 교시 버튼
    for i, slot in enumerate(df.columns[1:]):
        content = row[slot]
        # 빈칸인 경우 ➕ 표시, 내용이 있으면 내용 표시
        btn_label = content if content else "➕"
        
        if r_cols[i+1].button(btn_label, key=f"cell_{idx}_{slot}", use_container_width=True):
            # 상황 1: 수업 칩을 선택한 상태에서 빈칸(+)을 눌렀을 때 (넣기)
            if st.session_state.selected_chip_idx is not None and not content:
                chip = st.session_state.buffer[st.session_state.selected_chip_idx]
                target_class = chip['lesson'].split('\n')[0].strip()
                
                # 학급 중복 체크
                if any(df[slot].str.contains(target_class, na=False)):
                    st.error(f"❌ {target_class}반은 이 시간에 이미 수업이 있습니다!")
                else:
                    df.at[idx, slot] = chip['lesson']
                    st.session_state.buffer.pop(st.session_state.selected_chip_idx)
                    st.session_state.selected_chip_idx = None
                    st.rerun()
            
            # 상황 2: 손이 비어 있고, 수업이 있는 칸을 눌렀을 때 (빼기)
            elif content:
                st.session_state.buffer.append({
                    "teacher": t_name,
                    "lesson": content,
                    "orig_slot": slot
                })
                df.at[idx, slot] = ""
                st.rerun()

# 저장 기능
st.sidebar.header("💾 관리")
if st.sidebar.button("결과 엑셀로 저장"):
    df.to_excel("final_timetable.xlsx", index=False)
    st.sidebar.success("final_timetable.xlsx 저장 완료!")
