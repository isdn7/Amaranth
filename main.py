import streamlit as st

# MBTI 상세 설명 데이터
mbti_info = {
    "INTJ": {
        "emoji": "🧠",
        "title": "전략가형",
        "description": "창의적이고 분석적인 성향으로, 계획을 세우고 문제를 해결하는 데 탁월합니다. 독립적이며 장기 목표를 추구하는 성향이 강합니다.",
        "traits": ["분석적", "계획적", "독립적"],
        "careers": ["전략기획가", "데이터 분석가", "과학자"]
    },
    "ENFP": {
        "emoji": "🌈",
        "title": "활동가형",
        "description": "열정적이고 창의적이며, 다양한 사람들과의 소통을 즐깁니다. 자유롭고 새로운 경험을 좋아해요.",
        "traits": ["창의적", "외향적", "열정적"],
        "careers": ["마케터", "작가", "기획자"]
    },
    "ISFJ": {
        "emoji": "🛡️",
        "title": "수호자형",
        "description": "성실하고 책임감이 강하며, 조용히 헌신하는 스타일입니다. 다른 사람을 돕는 것을 좋아합니다.",
        "traits": ["책임감", "헌신적", "온화함"],
        "careers": ["간호사", "교사", "사회복지사"]
    },
    "ENTP": {
        "emoji": "⚡",
        "title": "변론가형",
        "description": "말이 많고 도전적인 성격으로, 다양한 아이디어와 토론을 즐깁니다. 유연하고 창의적이에요.",
        "traits": ["도전적", "말 잘함", "융통성 있음"],
        "careers": ["창업가", "변호사", "기획자"]
    },
    # 필요한 유형을 계속 추가하세요...
}

# 모든 MBTI 유형
mbti_types = list(mbti_info.keys())

# Streamlit UI
st.set_page_config(page_title="MBTI 안내기", page_icon="🧭")
st.title("🧬 MBTI 성격유형 안내기")
st.write("당신의 MBTI 유형을 선택하면, 친절하게 설명해드릴게요!")

selected_mbti = st.selectbox("🔍 MBTI를 선택하세요!", mbti_types)

if selected_mbti:
    info = mbti_info[selected_mbti]
    
    st.markdown(f"## {info['emoji']} {selected_mbti} - {info['title']}")
    st.markdown(f"**📖 설명:** {info['description']}")
    
    st.markdown("**🔍 대표 성격 특성:**")
    st.write(", ".join(info['traits']))
    
    st.markdown("**💼 추천 직업:**")
    st.write(", ".join(info['careers']))
    
    st.success("자신의 성향을 이해하고, 장점을 살려보세요! 💪")

