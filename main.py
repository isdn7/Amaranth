import streamlit as st
import pandas as pd
import io
import csv
import os

# 1. 페이지 설정
st.set_page_config(layout="wide", page_title="교사 시간표 자석 보드")

# 2. 데이터 파싱 함수 (따옴표 내 줄바꿈 대응)
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
        # 33칸 맞춤 및 데이터 정제(공백 제거)
        clean_row = [cell.strip() for cell in row]
        if len(clean_row) < 33:
            clean_row += [""] * (33 - len(clean_row))
        else:
            clean_row = clean_row[:33]
        rows.append(clean_row)
    
    return pd.DataFrame(rows, columns=columns)

# 3. 세션 초기화
if 'df' not in st.session_state:
    df_loaded = load_data_from_file("data.txt")
    if df_loaded is not None:
        st.session_state.df = df_loaded
    else:
        st.error("data.txt 파일을 찾을 수 없습니다. 같은 폴더에 파일을 만들어주세요.")
        st.stop()
    st.session_state.buffer = []
    st.session_state.selected_chip_idx = None

df = st.session_state.df

# ---------------------------------------------------------
# UI: 상단 대기석 (들고 있는 수업 칩)
# ---------------------------------------------------------
st.title("🧲 시간표 자석 이동 보드")
st.subheader("📥 현재 들고 있는 수업 (임시 대기석)")

if st.session_state.buffer:
    buf_cols = st.columns(len(st.session_state.buffer))
    for i, chip in enumerate(st.session_state.buffer):
        with buf_cols[i]:
            # 현재 선택된 칩은 강조 표시
            is_selected = (st.session_state.selected_chip_idx == i)
            style = "primary" if is_selected else "secondary"
            
            st.info(f"**{chip['teacher']}**\n\n{chip['lesson']}")
            if st.button(f"이 수업 선택" if not is_selected else "✅ 선택됨", key=f"buf_{i}"):
                st.session_state.selected_chip_idx = i
                st.rerun()
else:
    st.write("시간표에서 옮길 수업을 클릭하세요.")

st.divider()

# ---------------------------------------------------------
# UI: 자석 시간표 보드
# ---------------------------------------------------------
col_search, col_board = st.columns([1, 4])

with col_search:
    st.write("### 🔍 교사 검색")
    search_name = st.text_input("이름 입력 (예: 기나현)", "")
    # 검색된 교사만 필터링 (90명은 너무 많으므로)
    view_df = df[df['교사명'].str.contains(search_name)] if search_name else df.head(5)
    st.caption("작업 효율을 위해 검색된 분들만 아래에 표시됩니다.")

with col_board:
    # 시간표 헤더 (월~금)
    st.write("### 📅 자석 판 (클릭하여 빼기/넣기)")
    
    for _, row in view_df.iterrows():
        t_name = row['교사명']
        st.write(f"**👤 {t_name}**")
        
        # 32개 교시를 버튼으로 생성
        # Streamlit 컬럼 제한 때문에 요일별로 나누어 표시
        day_names = ["월", "화", "수", "목", "금"]
        slots_per_day = [6, 7, 6, 6, 7]
        start_idx = 1
        
        for d_idx, day in enumerate(day_names):
            num_slots = slots_per_day[d_idx]
            day_cols = st.columns([0.5] + [1] * num_slots)
            day_cols[0].write(f"**{day}**")
            
            for s_offset in range(num_slots):
                col_name = df.columns[start_idx + s_offset]
                content = row[col_name]
                btn_label = content if content else "➕"
                
                # 버튼 클릭 로직
                if day_cols[s_offset + 1].button(btn_label, key=f"btn_{t_name}_{col_name}", use_container_width=True):
                    # 상황 1: 수업 칩을 들고 있고, 빈칸을 눌렀을 때 (넣기)
                    if st.session_state.selected_chip_idx is not None and not content:
                        chip = st.session_state.buffer[st.session_state.selected_chip_idx]
                        target_class = chip['lesson'].split('\n')[0].strip()
                        
                        # 학급 중복 체크
                        if any(df[col_name].str.contains(target_class, na=False)):
                            st.error(f"❌ {target_class}반은 이 시간에 이미 수업이 있습니다!")
                        else:
                            df.loc[df['교사명'] == t_name, col_name] = chip['lesson']
                            st.session_state.buffer.pop(st.session_state.selected_chip_idx)
                            st.session_state.selected_chip_idx = None
                            st.rerun()
                    
                    # 상황 2: 손이 비어 있고, 수업이 있는 칸을 눌렀을 때 (빼기)
                    elif content:
                        st.session_state.buffer.append({
                            "teacher": t_name,
                            "lesson": content,
                            "orig_slot": col_name
                        })
                        df.loc[df['교사명'] == t_name, col_name] = ""
                        st.rerun()
            
            start_idx += num_slots
        st.write("---")

# 4. 저장 기능
if st.sidebar.button("💾 최종 결과 엑셀 저장"):
    df.to_excel("final_timetable.xlsx", index=False)
    st.sidebar.success("final_timetable.xlsx 저장 완료!")
