# app.py

import streamlit as st
from pages import main_page, upload_page, more_page

# 페이지 상태 관리
if 'page' not in st.session_state:
    st.session_state['page'] = 1

# 페이지 변경 함수
def go_to_page(page_num):
    st.session_state['page'] = page_num

# 페이지별 내용 표시
if st.session_state['page'] == 1:
    st.session_state['page'] = main_page()

elif st.session_state['page'] == 2:
    st.session_state['page'] = upload_page()

elif st.session_state['page'] == 3:
    st.session_state['page'] = more_page()
