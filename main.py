import streamlit as st
import pandas as pd
import io
import csv
import os

# 1. 페이지 설정 (가로로 넓게 사용)
st.set_page_config(layout="wide", page_title="교사 시간표 와이드 보드")

# CSS: 버튼 크기를 줄여서 한 화면에 많이 보이게 함
st.markdown("""
    <style>
    .stButton > button {
        padding: 0px 0px !important;
        font-size: 10px !important;
        height: 60px !important;
        min-width: 45px !important;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 2px !important;
    }
    </style>
    """, unsafe_allow_name=True)

# 2. 데이터 파싱 함수 (data.txt 읽기)
def load_data_from_file(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    
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
        if len(clean_row) < 33:
            clean_row += [""] * (33 - len(clean_row))
        else:
            clean_row = clean_row[:33]
        rows.append(clean_row)
    return pd.DataFrame(rows, columns=columns)

# 3. 데이터 초기화
if 'df' not in st.session_state:
    df_loaded = load_data_from_file("data.txt")
    if df_loaded is not None:
        st.session_state.df = df_loaded
    else:
        st.error("같은 폴더에 'data.txt' 파일을 만들어주세요.")
        st.stop()
    st.session_state.buffer = []
    st.session_state.selected_chip_idx = None

df = st.session_state.df

# ---------------------------------------------------------
# UI: 상단 대기석
# ---------------------------------------------------------
st.title("🧲 시간표 와이드 자석 보드")
st.subheader("📥 임시 대기석 (들고 있는 수업 칩)")

if st.session_state.buffer:
    buf_cols = st.columns(len(st.session_state.buffer) + 1)
    for i, chip in enumerate(st.session_state.buffer):
        with buf_cols[i]:
            is_selected = (st.session_state.selected_chip_idx == i)
            style = "✅ 선택됨" if is_selected else "이 수업 칩 선택"
            st.info(f"**{chip['teacher']}**\n{chip['lesson']}")
            if st.button(style, key=f"buf_{i}"):
                st.session_state.selected_chip_idx = i
                st.rerun()
else:
    st.write("옮길 수업을 아래에서 클릭하세요.")

st.divider()

# ---------------------------------------------------------
# UI: 엑셀 스타일 와이드 보드
# ---------------------------------------------------------
# 교사 검색 필터
search_name = st.text_input("교사 검색 (인원이 많으니 검색을 활용하세요)", "")
view_df = df[df['교사명'].str.contains(search_name)] if search_name else df.head(10)

# 헤더 행 (교시 번호)
cols = st.columns([1.5] + [1]*32)
cols[0].write("**교사명**")
for i, col_name in enumerate(df.columns[1:]):
    cols[i+1].write(f"**{col_name}**")

# 데이터 행
for idx, row in view_df.iterrows():
    t_name = row['교사명']
    r_cols = st.columns([1.5] + [1]*32)
    
    # 첫 번째 열: 교사 이름
    r_cols[0].write(f"**{t_name}**")
    
    # 32개 교시 버튼
    for i, slot in enumerate(df.columns[1:]):
        content = row[slot]
        btn_label = content if content else " " # 빈칸은 공백으로 표시
        
        if r_cols[i+1].button(btn_label, key=f"cell_{idx}_{slot}", use_container_width=True):
            # 상황 1: 수업 칩을 들고 있고, 빈칸을 눌렀을 때 (넣기)
            if st.session_state.selected_chip_idx is not None and not content:
                chip = st.session_state.buffer[st.session_state.selected_chip_idx]
                target_class = chip['lesson'].split('\n')[0].strip()
                
                # 학급 중복 체크
                if any(df[slot].str.contains(target_class, na=False)):
                    st.error(f"{target_class}반은 이 시간에 이미 수업이 있습니다!")
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

# 4. 사이드바 저장
with st.sidebar:
    st.header("💾 관리")
    if st.button("결과 엑셀로 저장"):
        df.to_excel("timetable_result.xlsx", index=False)
        st.success("timetable_result.xlsx 저장 완료!")
