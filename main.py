import streamlit as st

# 16가지 MBTI 정보 사전
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/MBTI_ISTJ.png"
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/cc/MBTI_ESTJ.png"
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f0/MBTI_ESFJ.png"
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/5a/MBTI_ISTP.png"
    },
    "ISFP": {
        "emoji": "🍃",
        "title": "모험가형",
        "description": """
ISFP는 감성적이고 창의적이며, 자유롭고 자연을 사랑하는 성격입니다.
조용하고 내성적이지만, 자신이 관심 있는 분야에서 빛을 발하는 경향이 있습니다.
        """,
        "traits": ["자유로운", "감성적", "창의적", "내성적"],
        "careers": ["디
