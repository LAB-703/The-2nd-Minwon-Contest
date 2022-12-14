import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timedelta
import pandas as pd


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



hide_menu='''
<style>
#MainMenu {
    visibility:hidden;
}
#document{
    font-family:'Pretendard JP Variable', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Emoji', sans-serif;
    }
footer {
    visibility:visible;
    size: 10%;
    font-family: 'Pretendard JP Variable';
}
footer:after{
    content: 'SPDX-FileCopyrightText: © 2022 LAB-703 SPDX-License-Identifier: MIT';
    font-size: 30%;
    display:block;
    position:relative;
    color:silver;
    font-family: 'Pretendard JP Variable';
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
button.css-jgupqz.e10mrw3y2 {
    opacity: 0;
    height: 2.5rem;
    padding: 0px;
    width: 2.5rem;
    transition: opacity 300ms ease 150ms, transform 300ms ease 150ms;
    border: none;
    background-color: #C0504D;
    visibility: visible;
    color: rgba(0, 0, 0, 0.6);
    border-radius: 0.75rem;
    transform: scale(0);
}
div.viewerBadge_link__1S137 {
    display:none;
    background-color: #C0504D;
}
div.css-j7qwjs.e1fqkh3o5 {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
}
a.viewerBadge_container__1QSob {
    z-index: 50;
    font-size: .875rem;
    position: fixed;
    bottom: 0;
    right: 0;
    display: none;
}
div.streamlit-expanderHeader.st-ae.st-bq.st-ag.st-ah.st-ai.st-aj.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-as.st-at.st-by.st-bz.st-c0.st-c1.st-c2.st-b4.st-c3.st-c4.st-c5.st-b5.st-c6.st-c7.st-c8.st-c9 {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
    font-weight: 300;
    font-size: initial;
}
div.st-dc.st-ci.st-dd.st-de.st-df.st-co.st-dg.st-dh.st-di {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
}
div.streamlit-expanderContent.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bt.st-br.st-cf.st-eh.st-bw.st-bx.st-as.st-at.st-by.st-bz.st-c0.st-c1.st-ch.st-ci.st-am.st-ei.st-cl.st-b1.st-cm.st-b3.st-c7.st-c8.st-c9 {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
}
</style>
'''

st.markdown(hide_menu, unsafe_allow_html=True)




st.markdown('<p align="center" style=" font-size: 140%;"><b>🧭공간 EDA</b></p>', unsafe_allow_html=True)



# HtmlFile = open("서울시 자치구별 장애정도별 등록장애인 현황.html", 'r',encoding='utf-8')
# source_code = HtmlFile.read() 
# print(source_code)
# components.html(source_code, height=450,  scrolling=False)

st.image("시도별 신고량 순(최종).png")
expander1 = st.expander("시도 신고량(신고량 순)")
expander1.dataframe(pd.read_csv("시도_신고량순.csv",encoding='cp949',index_col=0), use_container_width=True)
expander1.write("*면적당 신고량=신고량/면적")

st.image("시도별 면적당 신고량 순(최종).png")
expander2 = st.expander("시군구 면적당 신고량(면적당 신고량 순)")
expander2.dataframe(pd.read_csv("시군구_면적별신고량순(최종).csv",encoding='cp949'), use_container_width=True)
expander2.write("*면적당 신고량=신고량/면적")

df=pd.read_csv("시군구_면적별신고량순(최종).csv",encoding='cp949')

expander31 = st.expander("서울특별시")
expander31.image("시군구/서울특별시.png")
expander31.image("시군구/서울특별시(면적당).png")
expander31.dataframe(df[df['시도']=="서울특별시"].sort_values(['신고량'],ascending=False), use_container_width=True)

expander3 = st.expander("부산광역시")
expander3.image("시군구/부산광역시.png")
expander3.image("시군구/부산광역시(면적당).png")
expander3.dataframe(df[df['시도']=="부산광역시"].sort_values(['신고량'],ascending=False), use_container_width=True)

expander4 = st.expander("대구광역시")
expander4.image("시군구/대구광역시.png")
expander4.image("시군구/대구광역시(면적당).png")
expander4.dataframe(df[df['시도']=="대구광역시"].sort_values('신고량',ascending=False), use_container_width=True)


expander5 = st.expander("인천광역시")
expander5.image("시군구/인천광역시.png")
expander5.image("시군구/인천광역시(면적당).png")
expander5.dataframe(df[df['시도']=="인천광역시"].sort_values('신고량',ascending=False), use_container_width=True)

expander6 = st.expander("광주광역시")
expander6.image("시군구/광주광역시.png")
expander6.image("시군구/광주광역시(면적당).png")
expander6.dataframe(df[df['시도']=="광주광역시"].sort_values('신고량',ascending=False), use_container_width=True)


expander7 = st.expander("대전광역시")
expander7.image("시군구/대전광역시.png")
expander7.image("시군구/대전광역시(면적당).png")
expander7.dataframe(df[df['시도']=="대전광역시"].sort_values('신고량',ascending=False), use_container_width=True)

expander8 = st.expander("울산광역시")
expander8.image("시군구/울산광역시.png")
expander8.image("시군구/울산광역시(면적당).png")
expander8.dataframe(df[df['시도']=="울산광역시"].sort_values('신고량',ascending=False), use_container_width=True)

expander9 = st.expander("경기도")
expander9.image("시군구/경기도.png")
expander9.image("시군구/경기도(면적당).png")
expander9.dataframe(df[df['시도']=="경기도"].sort_values('신고량',ascending=False), use_container_width=True)

expander10 = st.expander("강원도")
expander10.image("시군구/강원도.png")
expander10.image("시군구/강원도(면적당).png")
expander10.dataframe(df[df['시도']=="강원도"].sort_values('신고량',ascending=False), use_container_width=True)

expander11 = st.expander("충청남도")
expander11.image("시군구/충청남도.png")
expander11.image("시군구/충청남도(면적당).png")
expander11.dataframe(df[df['시도']=="충청남도"].sort_values('신고량',ascending=False), use_container_width=True)

expander12 = st.expander("충청북도")
expander12.image("시군구/충청북도.png")
expander12.image("시군구/충청북도(면적당).png")
expander12.dataframe(df[df['시도']=="충청북도"].sort_values('신고량',ascending=False), use_container_width=True)

expander13 = st.expander("경상남도")
expander13.image("시군구/경상남도.png")
expander13.image("시군구/경상남도(면적당).png")
expander13.dataframe(df[df['시도']=="경상남도"].sort_values('신고량',ascending=False), use_container_width=True)

expander14 = st.expander("경상북도")
expander14.image("시군구/경상북도.png")
expander14.image("시군구/경상북도(면적당).png")
expander14.dataframe(df[df['시도']=="경상북도"].sort_values('신고량',ascending=False), use_container_width=True)

expander15 = st.expander("전라남도")
expander15.image("시군구/전라남도.png")
expander15.image("시군구/전라남도(면적당).png")
expander15.dataframe(df[df['시도']=="전라남도"].sort_values('신고량',ascending=False), use_container_width=True)

expander16 = st.expander("전라북도")
expander16.image("시군구/전라북도.png")
expander16.image("시군구/전라북도(면적당).png")
expander16.dataframe(df[df['시도']=="전라북도"].sort_values('신고량',ascending=False), use_container_width=True)




