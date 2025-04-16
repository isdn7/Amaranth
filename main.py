import streamlit as st

# 16가지 MBTI 정보 딕셔너리
mbti_info = {
    "INTJ": {
        "emoji": "🧠",
        "title": "전략가형",
        "description": "창의적이고 분석적이며, 장기 목표를 계획하는 데 능합니다.",
        "traits": ["분석적", "독립적", "계획적"],
        "careers": ["전략기획가", "과학자", "시스템 엔지니어"]
    },
    "INTP": {
        "emoji": "🔍",
        "title": "논리술사형",
        "description": "논리적이고 호기심이 많으며, 복잡한 문제 해결을 좋아합니다.",
        "traits": ["논리적", "호기심 많음", "이론적"],
        "careers": ["프로그래머", "연구원", "철학자"]
    },
    "ENTJ": {
        "emoji": "📈",
        "title": "지도자형",
        "description": "결단력 있고 추진력이 강하며, 리더 역할을 즐깁니다.",
        "traits": ["리더십", "목표지향", "결단력"],
        "careers": ["CEO", "변호사", "정치가"]
    },
    "ENTP": {
        "emoji": "⚡",
        "title": "변론가형",
        "description": "아이디어가 풍부하고 토론을 즐기며, 유연한 사고방식을 지녔습니다.",
        "traits": ["창의적", "융통성", "말 잘함"],
        "careers": ["기획자", "변호사", "창업가"]
    },
    "INFJ": {
        "emoji": "🌌",
        "title": "옹호자형",
        "description": "깊이 있는 통찰과 강한 신념을 바탕으로 타인을 돕고자 합니다.",
        "traits": ["통찰력", "이상주의", "공감 능력"],
        "careers": ["심리상담사", "작가", "종교인"]
    },
    "INFP": {
        "emoji": "🎨",
        "title": "중재자형",
        "description": "감성적이며 이상주의자로, 가치 있는 삶을 추구합니다.",
        "traits": ["감성적", "이상주의", "자유로움"],
        "careers": ["작가", "예술가", "상담사"]
    },
    "ENFJ": {
        "emoji": "🤝",
        "title": "선도자형",
        "description": "타인을 이끄는 데 탁월하며, 배려심이 깊고 사교성이 좋습니다.",
        "traits": ["사교적", "헌신적", "영향력 있음"],
        "careers": ["교사", "리더", "사회운동가"]
    },
    "ENFP": {
        "emoji": "🌈",
        "title": "활동가형",
        "description": "열정적이고 창의적이며, 새로운 사람과 경험을 좋아합니다.",
        "traits": ["열정적", "상상력 풍부", "외향적"],
        "careers": ["마케터", "배우", "기획자"]
    },
    "ISTJ": {
        "emoji": "📚",
        "title": "현실주의자형",
        "description": "책임감 있고 신뢰할 수 있으며, 전통과 규칙을 중시합니다.",
        "traits": ["신중함", "책임감", "현실적"],
        "careers": ["공무원", "회계사", "행정직"]
    },
    "ISFJ": {
        "emoji": "🛡️",
        "title": "수호자형",
        "description": "조용하고 헌신적이며, 타인을 돕는 데 기쁨을 느낍니다.",
        "traits": ["온화함", "헌신적", "성실함"],
        "careers": ["간호사", "교사", "사회복지사"]
    },
    "ESTJ": {
        "emoji": "🏛️",
        "title": "경영자형",
        "description": "현실적이고 체계적이며, 조직 운영에 강점을 지닙니다.",
        "traits": ["관리 능력", "결단력", "실용성"],
        "careers": ["관리자", "군인", "경찰관"]
    },
    "ESFJ": {
        "emoji": "🎀",
        "title": "집정관형",
        "description": "사교적이고 배려심 많으며, 주변 사람을 돌보는 데 능합니다.",
        "traits": ["친절함", "배려심", "협동적"],
        "careers": ["초등교사", "간호사", "서비스직"]
    },
    "ISTP": {
        "emoji": "🛠️",
        "title": "장인형",
        "description": "조용하고 실용적이며, 도구나 기계 다루기를 좋아합니다.",
        "traits": ["관찰력", "냉정함", "유형적"],
        "careers": ["엔지니어", "기술자", "정비사"]
    },
    "ISFP": {
        "emoji": "🍃",
        "title": "모험가형",
        "description": "온화하고 예술적 감성이 풍부하며, 조용한 자유를 즐깁니다.",
        "traits": ["감성적", "자유로움", "예술적"],
        "careers": ["예술가", "디자이너", "사진작가"]
    },
    "ESTP": {
        "emoji": "🏍️",
        "title": "사업가형",
        "description": "에너지 넘치고 현실적이며, 새로운 도전에 흥미를 가집니다.",
        "traits": ["모험심", "사교성", "즉흥적"],
        "careers": ["영업직", "기업가", "스포츠선수"]
    },
    "ESFP": {
        "emoji": "🎉",
        "title": "연예인형",
        "description": "사교적이고 밝으며, 사람들과 함께 즐기는 것을 좋아합니다.",
        "traits": ["사교성", "감각적", "유쾌함"],
        "careers": ["가수", "배우", "이벤트 플래너"]
    }
}

# Streamlit 페이지 설정
st.set_page_config(page_title="MBTI 안내기", page_icon="🧭")
st.title("🔎 MBTI 성격유형 안내기")
st.markdown("당신의 MBTI 유형을 선택하면 자세한 성격 설명을 드릴게요!")

# 사용자 선택
selected_mbti = st.selectbox("📌 MBTI를 선택하세요!", list(mbti_info.keys()))

# 결과 출력
if selected_mbti:
    info = mbti_info[selected_mbti]
    
    st.markdown(f"## {info['emoji']} {selected_mbti} - {info['title']}")
    st.markdown(f"**📖 설명:** {info['description']}")
    
    st.markdown("**🧬 대표 성격 특성:**")
    st.write(", ".join(info['traits']))
    
    st.markdown("**💼 추천 직업:**")
    st.write(", ".join(info['careers']))
    
    st.success("나의 성향을 이해하고, 장점을 살려보세요! 🌱")

