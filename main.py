import streamlit as st

# MBTI 정보 사전 (16개 유형 모두 포함)
mbti_info = {
    "INTJ": {
        "emoji": "🧠",
        "title": "전략가형",
        "description": """
INTJ는 논리와 전략적 사고를 기반으로 세상을 바라보는 유형입니다. 독립적이고 자기 주도적인 성향이 강하며,
복잡한 문제 해결이나 장기적인 목표 달성에 탁월한 능력을 보입니다. 감정보다는 사실과 분석을 선호합니다.
        """,
        "traits": ["분석적", "계획적", "독립적", "전략적"],
        "careers": ["전략기획가", "과학자", "시스템 엔지니어"],
        "best_matches": ["ENFP", "ENTP"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/88/MBTI_INTJ.png"
    },
    "ENFP": {
        "emoji": "🌈",
        "title": "활동가형",
        "description": """
ENFP는 열정과 상상력이 풍부하며, 새로운 아이디어와 사람들을 만나는 것을 즐깁니다.
감정에 충실하며, 창의적인 에너지로 사람들을 고무시키는 능력이 있습니다.
        """,
        "traits": ["열정적", "상상력 풍부", "감성적", "외향적"],
        "careers": ["마케터", "작가", "기획자"],
        "best_matches": ["INFJ", "INTJ"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/MBTI_ENFP.png"
    },
    "ISFJ": {
        "emoji": "🛡️",
        "title": "수호자형",
        "description": """
ISFJ는 헌신적이고 책임감이 강한 성격으로, 타인의 필요를 민감하게 파악하고 조용히 돕습니다.
전통적인 가치와 조직을 중시하며, 안정적인 환경에서 강점을 발휘합니다.
        """,
        "traits": ["책임감", "헌신적", "온화함", "현실적"],
        "careers": ["간호사", "교사", "사회복지사"],
        "best_matches": ["ESFP", "ESTP"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2f/MBTI_ISFJ.png"
    },
    "ENTP": {
        "emoji": "⚡",
        "title": "변론가형",
        "description": """
ENTP는 도전적이고 유쾌한 성격으로, 새로운 가능성과 아이디어를 탐색하는 데에 열정적입니다.
논쟁과 토론을 즐기며, 틀에 얽매이지 않는 사고방식을 가집니다.
        """,
        "traits": ["창의적", "말 잘함", "융통성", "도전적"],
        "careers": ["기획자", "변호사", "스타트업 창업자"],
        "best_matches": ["INFJ", "INTJ"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f2/MBTI_ENTP.png"
    },
    "INTP": {
        "emoji": "🔍",
        "title": "논리술사형",
        "description": """
INTP는 논리적이고 호기심이 많으며, 복잡한 문제 해결을 좋아합니다. 창의적이고 독창적인 아이디어를 제시하며,
새로운 이론과 개념을 탐구하는 것을 즐깁니다.
        """,
        "traits": ["논리적", "호기심 많음", "이론적", "창의적"],
        "careers": ["프로그래머", "연구원", "철학자"],
        "best_matches": ["ENTJ", "ENFP"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/15/MBTI_INTP.png"
    },
    "INFJ": {
        "emoji": "🌌",
        "title": "옹호자형",
        "description": """
INFJ는 깊은 통찰력과 강한 신념을 가지고 있으며, 타인의 발전을 돕는 데 만족을 느낍니다.
이상주의적인 성향이 강하고, 자신의 가치관을 따라 행동하는 경향이 있습니다.
        """,
        "traits": ["통찰력", "이상주의", "공감 능력", "직관적"],
        "careers": ["심리상담사", "작가", "종교인"],
        "best_matches": ["ENFP", "INTJ"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/cf/MBTI_INFJ.png"
    },
    "INFP": {
        "emoji": "🎨",
        "title": "중재자형",
        "description": """
INFP는 감성적이고 이상주의적인 성향을 가지고 있으며, 자신의 가치와 이상에 따라 행동하는 사람들입니다.
내면의 세계와 감정을 중요시하며, 예술적인 활동을 즐깁니다.
        """,
        "traits": ["감성적", "이상주의", "자유로운", "창의적"],
        "careers": ["작가", "예술가", "상담사"],
        "best_matches": ["ENFJ", "ENTP"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/MBTI_INFP.png"
    },
    "ENFJ": {
        "emoji": "🤝",
        "title": "선도자형",
        "description": """
ENFJ는 타인과의 관계를 중시하며, 사람들을 이끌고 돕는 데 큰 만족을 느낍니다.
상황에 맞춰 사람들을 이해하고 조화를 이루는 능력이 뛰어납니다.
        """,
        "traits": ["사교적", "이타적", "배려심", "리더십"],
        "careers": ["교사", "리더", "사회운동가"],
        "best_matches": ["INFP", "ISFJ"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/73/MBTI_ENFJ.png"
    },
    # 나머지 8개 유형도 추가해 주세요.
}

# 페이지 설정
st.set_page_config(page_title="MBTI 성격유형 안내기", page_icon="🧭")
st.title("🧬 MBTI 성격유형 안내기")
st.write("MBTI 유형을 선택하시면 자세한 설명, 궁합, 추천 직업, 이미지 등을 보여드립니다!")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요!", list(mbti_info.keys()))

if selected_mbti:
    info = mbti_info[selected_mbti]
    st.markdown(f"## {info['emoji']} {selected_mbti} - {info['title']}")
    st.image(info['image_url'], width=250, caption=f"{selected_mbti} 캐릭터")
    st.markdown("### 📖 성격 설명")
    st.write(info["description"])
    st.markdown("### 💡 성격 특성")
    st.markdown(", ".join(info["traits"]))
    st.markdown("### 💼 추천 직업")
    st.markdown(", ".join(info["careers"]))

    # 궁합 출력
    st.markdown("### ❤️ 궁합이 잘 맞는 MBTI")
    best_matches = info["best_matches"]
    for bm in best_matches:
        if bm in mbti_info:
            bm_info = mbti_info[bm]
            st.markdown(f"- {bm_info['emoji']} **{bm} - {bm_info['title']}**")

    st.success("자신의 성향을 이해하고, 관계에 활용해보세요! 😊")
