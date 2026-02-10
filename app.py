import streamlit as st

# 페이지 설정
st.set_page_config(page_title="반려견 산책 지수 계산기", page_icon="🐶")

# 스타일링 (CSS)
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button { width: 100%; background-color: #ffcc00; color: #333; font-weight: bold; border-radius: 10px; border: none; height: 3em; }
    .stButton>button:hover { background-color: #e6b800; color: #333; }
    .result-box { padding: 20px; border-radius: 15px; background-color: #fff9e6; text-align: center; border: 1px dashed #ffcc00; color: #d35400; font-weight: bold; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# 헤더 부분
st.caption("반려견 영양 오디오레터 [유료 구독자 전용]")
st.title("🐶 산책 지수 계산기")

# 입력창
dog_type = st.selectbox("우리 아이 상태", ["일반 건강한 강아지", "민감군(단두종/자견/노령견/질환견)"])
pm_value = st.number_input("현재 초미세먼지(PM2.5) 농도", min_value=0.0, step=1.0, format="%.1f")

# 계산 버튼
if st.button("산책 가능 여부 확인하기"):
    msg = ""
    if dog_type == "민감군(단두종/자견/노령견/질환견)":
        if pm_value <= 15: msg = "✅ 산책 가능! (15~20분 권장)"
        elif pm_value <= 25: msg = "⚠️ 주의! 10분 이내 퀵 산책"
        else: msg = "❌ 산책 포기! 실내 노즈워크 추천"
    else:
        if pm_value <= 15: msg = "✅ 산책하기 좋은 날! (20~30분)"
        elif pm_value <= 25: msg = "⚠️ 가벼운 산책 (15분 이내)"
        elif pm_value <= 50: msg = "🚫 배변 산책만 (5분 이내)"
        else: msg = "❌ 위험! 실내 활동 추천"
    
    st.markdown(f'<div class="result-box">{msg}</div>', unsafe_allow_html=True)

# 푸터
st.divider()
st.markdown("<p style='text-align: center; font-weight: bold;'>반려견영양연구소 Dognutritionlab</p>", unsafe_allow_html=True)
