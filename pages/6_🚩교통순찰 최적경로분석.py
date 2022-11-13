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
st.markdown('<p align="center" style=" font-size: 140%;"><b>🚩교통순찰 최적경로분석</b></p>', unsafe_allow_html=True)

st.subheader('오전 7시~오전 8시')
st.image("최적경로/7to8.png")

st.subheader('오전 9시~오전 10시')
st.image("최적경로/9새10.png")

st.subheader('오전 11시~오후 12시')
st.image("최적경로/11to12.png")

st.subheader('오후 1시~오후 2시')
st.image("최적경로/1to2.png")

st.subheader('오후 1시~오후 2시')
st.image("최적경로/1to2.png")

st.subheader('오후 3시~오후 4시')
st.image("최적경로/3to4.png")

st.subheader('오후 5시~오후 6시')
st.image("최적경로/5to6.png")

st.subheader('오후 7시~오후 8시')
st.image("최적경로/19to20.png")

st.subheader('오후 9시~오후 10시')
st.image("최적경로/21to22.png")

