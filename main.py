import streamlit as st

# MBTI 전체 정보
mbti_info = {
    "INTJ": {
        "emoji": "🧠",
        "title": "전략가형",
        "description": "INTJ는 독립적이고 분석적인 성격으로, 미래를 위한 계획을 세우고 복잡한 문제를 해결하는 데 탁월합니다. 혼자 있는 시간을 즐기며, 깊이 있는 사고를 통해 창의적인 전략을 구상하는 능력이 뛰어납니다. 감정보다는 논리를 중시하며, 목표 지향적입니다.",
        "traits": ["분석적", "계획적", "독립적", "전략적"],
        "careers": ["전략기획가", "과학자", "시스템 엔지니어"],
        "best_matches": ["ENFP", "ENTP"],
        "image_url": "https://i.imgur.com/oBjnh7m.png"
    },
    "ENFP": {
        "emoji": "🌈",
        "title": "활동가형",
        "description": "ENFP는 열정적이고 상상력이 풍부한 성격으로, 사람들과의 교류를 즐기며 새로운 가능성을 탐색합니다. 창의력과 유연한 사고를 바탕으로 다양한 활동을 시도하며, 타인에게 긍정적인 영향을 끼칩니다. 감정에 충실하며, 자율성과 모험심이 강합니다.",
        "traits": ["열정적", "상상력 풍부", "감성적", "외향적"],
        "careers": ["마케터", "작가", "기획자"],
        "best_matches": ["INFJ", "INTJ"],
        "image_url": "https://i.imgur.com/symJmNw.png"
    },
    # 나머지 14개 유형도 동일한 형식으로 추가해 주세요...
}

# 스트림릿 페이지 구성
st.set_page_config(page_title="MBTI 궁합 분석기", page_icon="🔮", layout="centered")
st.title("🔎 MBTI 성격유형 분석기")
st.markdown("MBTI 유형을 선택하면 자세한 설명과 궁합 정보, 캐릭터 이미지를 보여드려요!")

# 선택창
selected_mbti = st.selectbox("📌 당신의 MBTI를 선택하세요:", list(mbti_info.keys()))

# 선택한 MBTI 정보 출력
if selected_mbti:
    info = mbti_info[selected_mbti]
    
    st.markdown(f"## {info['emoji']} {selected_mbti} - {info['title']}")
    
    # 이미지 출력
    st.image(info['image_url'], width=300, caption=f"{selected_mbti} 캐릭터")

    # 설명
    st.markdown(f"**🧾 상세 설명**")
    st.write(info["description"])
    
    # 특성
    st.markdown("**💡 대표 성격 특성**")
    st.markdown(", ".join(info["traits"]))
    
    # 직업
    st.markdown("**💼 추천 직업**")
    st.markdown(", ".join(info["careers"]))
    
    # 궁합 MBTI 추천
    st.markdown("**❤️ 궁합이 잘 맞는 MBTI 유형**")
    matches = info["best_matches"]
    match_string = ", ".join([f"{mbti_info[m]['emoji']} {m} - {mbti_info[m]['title']}" for m in matches])
    st.markdown(match_string)

    st.success("자신의 성격을 이해하면, 타인과의 관계도 더 깊어져요 😊")

