import streamlit as st


st.set_page_config(page_title="주정차 실시간 모니터링 시스템 구축 및 교통순찰 최적경로분석",          
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/LAB-703',
        'Report a bug': "https://github.com/LAB-703",
        'About': '''SPDX-FileCopyrightText: © 2022 LAB-703 SPDX-License-Identifier: MIT'''
    }
)    

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    

    
# 메인메뉴 없애고, 저작권 표시
hide_menu='''
<style>
#MainMenu {
    visibility:hidden;
}
#document{
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
}
footer {
    visibility:visible;
    size: 10%;
    font-family: 'Pretendard';
}
footer:after{
    content: 'SPDX-FileCopyrightText: © 2022 LAB-703 SPDX-License-Identifier: MIT';
    font-size: 30%;
    display:block;
    position:relative;
    color:silver;
    font-family: 'Pretendard';
}
code {
    color: #C0504D;
    overflow-wrap: break-word;
    background: linen;
    font-family: 'Source Code Pro';
}
#root > div:nth-child(1) > div > div > a {
    visibility:hidden;
}    
    
    
div.stButton > button:first-child {
font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
  font-size:100%;
    background-color: #FCF9F6;
    font-color: #C0504D;
}
</style>
'''
st.markdown(hide_menu, unsafe_allow_html=True)

################################# 팀 소개#############################################

st.markdown('<p align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 30px;">0️⃣ 팀 💪굳건히❓</p>', unsafe_allow_html=True)
st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">장애인이 <b>굳건히</b> 자립적인 생활을 도모할 수 있도록 <b>국</b>민 <b>권</b>익 <b>위</b>원회에 지원한 팀 💪굳건히입니다.</p>', unsafe_allow_html=True)
st.markdown(' ')
st.markdown('---------------------------------------------------- ')
st.markdown('<p align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 30px;">팀원 소개</p>', unsafe_allow_html=True)

# 페이지 레이아웃 3갈래
#팀원 소개
col1, col2, col3 = st.columns(3)
with col1:
    st.image("박지영.jpg", width=100)
    st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">팀장 : 이정민</p>', unsafe_allow_html=True)
    st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">경찰대학 치안대학원 범죄학과 석사과정</p>', unsafe_allow_html=True)

with col2:
    st.image("증명사진_이정민.jpg", width=100)
    st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">팀원 : 이수연</p>', unsafe_allow_html=True)
    st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">경찰대학 법학과 3학년</p>', unsafe_allow_html=True)

with col3:
    st.image("https://github.com/LAB-703/LAB-703/blob/main/%EB%B0%95%EC%98%81%EB%B9%88.jpg?raw=true", width=100)
    st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">팀원 : 김민정</p>', unsafe_allow_html=True)
    st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">경찰대학 법학과 4학년</p>', unsafe_allow_html=True)
st.markdown('---------------------------------------------------- ')   
st.markdown(' ')
st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">※ 팀원 2명은 행정안전부와 한국지능정보사회진흥원에서 실시 중인 ‘공공빅데이터 분석 청년인재 양성사업’을 통해 국립재활원에 파견된 인턴연구원임</p>', unsafe_allow_html=True)
    

