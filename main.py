import streamlit as st

# MBTI 정보 사전 (16개 유형)
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
        "image_url": "https://images.unsplash.com/photo-1502814511805-e8c9e29ed970"
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
        "image_url": "https://images.unsplash.com/photo-1495062350044-f4fe7beae83e"
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
        "image_url": "https://images.unsplash.com/photo-1518563436633-02a0d09c65be"
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
        "image_url": "https://images.unsplash.com/photo-1603025990137-2fe924e69944"
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
        "image_url": "https://images.unsplash.com/photo-1524952154698-7b5e58f69b35"
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
        "image_url": "https://images.unsplash.com/photo-1571072365107-bcd83389cc66"
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
        "image_url": "https://images.unsplash.com/photo-1554511240-520024fd9f5e"
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
        "image_url": "https://images.unsplash.com/photo-1562242334-22876d8ea865"
    },
    "ISTJ": {
        "emoji": "📚",
        "title": "현실주의자형",
        "description": """
ISTJ는 책임감이 강하고 실용적입니다. 정확하고 꼼꼼하게 일을 처리하며, 규칙과 절차를 중시하는 성격입니다.
업무를 체계적으로 처리하며, 안정적인 환경에서 잘 활동합니다.
        """,
        "traits": ["책임감", "실용적", "세밀한", "보수적"],
        "careers": ["경영자", "교사", "군인"],
        "best_matches": ["ESFP", "ESTP"],
        "image_url": "https://images.unsplash.com/photo-1581324181741-6d1f2166e5be"
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
        "image_url": "https://images.unsplash.com/photo-1541162804633-742734699566"
    },
    "ESTJ": {
        "emoji": "🏛️",
        "title": "경영자형",
        "description": """
ESTJ는 조직적이고 현실적인 성향을 가지고 있습니다. 체계적이고 책임감이 강하며, 업무를 신속하고 효율적으로 처리합니다.
높은 리더십과 관리 능력을 지니고 있습니다.
        """,
        "traits": ["실용적", "리더십", "결단력", "체계적"],
        "careers": ["경영자", "군인", "공무원"],
        "best_matches": ["ISFP", "INFP"],
        "image_url": "https://images.unsplash.com/photo-1505740150289-26c3d9c5f300"
    },
    "ESFJ": {
        "emoji": "🎀",
        "title": "집정관형",
        "description": """
ESFJ는 다른 사람들을 돕는 데 큰 만족을 느끼며, 사람들과의 관계를 중요하게 생각합니다.
배려심과 사교성이 뛰어나며, 타인의 감정을 잘 이해합니다.
        """,
        "traits": ["사교적", "배려심", "협동적", "친절함"],
        "careers": ["교사", "간호사", "사회복지사"],
        "best_matches": ["ISFP", "INFP"],
        "image_url": "https://images.unsplash.com/photo-1512402160761-1a93520a1a28"
    },
    "ISTP": {
        "emoji": "🛠️",
        "title": "장인형",
        "description": """
ISTP는 실용적이고 분석적인 성향을 지니고 있으며, 새로운 도전과 문제 해결을 좋아합니다.
기술적이고 현실적인 접근을 통해 문제를 해결하는 능력이 뛰어납니다.
        """,
        "traits": ["분석적", "냉정함", "실용적", "기술적"],
        "careers": ["기술자", "정비사", "엔지니어"],
        "best_matches": ["ESTJ", "ESFJ"],
        "image_url": "https://images.unsplash.com/photo-1500834971410-0f7586a67bdb"
    },
    "ISFP": {
        "emoji": "🍃",
        "title": "모험가형",
        "description": """
ISFP는 감성적이고 창의적이며, 자유롭고 자연을 사랑하는 성격입니다.
조용하고 내성적이지만, 자신이 관심 있는 분야에서 빛을 발하는 경향이 있습니다.
        """,
        "traits": ["자유로운", "감성적", "창의적", "내성적"],
        "careers": ["디자이너", "예술가", "사진작가"],
        "best_matches": ["ESTJ", "ENTP"],
        "image_url": "https://images.unsplash.com/photo-1521589686198-0f09b1da161b"
    },
    "ESTP": {
        "emoji": "🏍️",
        "title": "사업가형",
        "description": """
ESTP는 현실적이고 에너지 넘치는 성격으로, 도전적이고 모험적인 삶을 선호합니다.
즉흥적이며 변화에 잘 적응하고, 다른 사람들과 함께 활동하는 것을 즐깁니다.
        """,
        "traits": ["에너지 넘침", "즉흥적", "모험적", "사교적"],
        "careers": ["영업직", "스포츠 선수", "사업가"],
        "best_matches": ["ISFJ", "ISTJ"],
        "image_url": "https://images.unsplash.com/photo-1601700475523-64d9ad03404d"
    },
    "ESFP": {
        "emoji": "🎉",
        "title": "연예인형",
        "description": """
ESFP는 사교적이고 긍정적인 성격으로, 사람들과 함께 즐기며 살아가는 것을 좋아합니다.
주변 사람들에게 활력을 주고, 에너지가 넘치는 성격입니다.
        """,
        "traits": ["사교적", "유쾌함", "창의적", "열정적"],
        "careers": ["가수", "배우", "이벤트 기획자"],
        "best_matches": ["ISTJ", "ISFJ"],
        "image_url": "https://images.unsplash.com/photo-1585877973761-b4193b82e1bb"
    }
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
    
    # 웹에서 이미지 불러오기
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
