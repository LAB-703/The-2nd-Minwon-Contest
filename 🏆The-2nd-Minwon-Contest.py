import streamlit as st
import streamlit.components.v1 as components
from urllib import parse
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import clipboard
import random
import pandas as pd
from pytz import timezone
import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest
from googleapiclient import discovery


#전체 페이지
st.set_page_config(page_title="척척 석박의 기사 인용 도우미",          
    page_icon="👀",
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
    font-weight: 200;
}
</style>
'''

st.markdown(hide_menu, unsafe_allow_html=True)




# #page1#######################################################################################################

st.markdown('<p align="center" style=" font-size: 140%;"><b>👀 척척 석박들을 위한 기사 인용 도우미</b></p>', unsafe_allow_html=True)



