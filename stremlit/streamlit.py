import pandas as pd
import streamlit as st
import os
from PIL import Image

if 'page' not in st.session_state:
    st.session_state['page'] = 1
# 페이지 변경 함수
def go_to_page(page_num):
    st.session_state['page'] = page_num

if st.session_state['page'] == 1:
    main_bg_color = "#CEF6F5"  # 메인 페이지 배경색

    # CSS 스타일을 적용하여 배경 색 변경
    st.markdown(f"""
            <style>
            /* 메인 페이지 배경 색 설정 */
            .stApp {{
                background-color: {main_bg_color};
            }}
            </style>
            """, unsafe_allow_html=True)
    # st.image("data/jeju.gif", use_column_width=True)
    st.image("data\park.jpg")
    st.title("Where to Park?")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Show me your car"):
        go_to_page(2)

# 페이지별 내용 표시
elif st.session_state['page'] == 2:
    # 배경색 설정 (고정)
    main_bg_color = "#ECF8E0"  # 메인 페이지 배경색
    # st.image("data\eyes.jpg")
    # CSS 스타일을 적용하여 배경 색 변경
    st.markdown(f"""
        <style>
        /* 메인 페이지 배경 색 설정 */
        .stApp {{
            background-color: {main_bg_color};
        }}
        </style>
        """, unsafe_allow_html=True)

    # 페이지 제목
    st.title('어쩌구')
    # if st.button("시작 화면으로️"):
    #     go_to_page(1)
    st.write('-'*10)
    # sidebar input
    # 첫 번째 구간
    # 선택된 옵션 - 메인 페이지에 표시
    st.subheader('upload here⬇️')
    img_file = st.file_uploader('', type=['png', 'jpg', 'jpeg'])
    st.markdown('Your car is..')
    st.markdown('Accuracy is..')
    st.write('-' * 10)
    #     go_to_page(3)
    # col1, col2, col3 = st.columns([2, 2.5, 2])  # 좌측, 중앙, 우측 열로 나누기
    col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col1:
        if st.button("⬅️Back"):
            go_to_page(1)

    with col3:
        if st.button("More"):
            go_to_page(3)

elif st.session_state['page'] == 3:
    # 배경색 설정 (고정)
    main_bg_color = "#F8E6E0"  # 메인 페이지 배경색

    # CSS 스타일을 적용하여 배경 색 변경
    st.markdown(f"""
        <style>
        /* 메인 페이지 배경 색 설정 */
        .stApp {{
            background-color: {main_bg_color};
        }}
        </style>
        """, unsafe_allow_html=True)

    # 페이지 제목
    st.title("More about EV!")
    st.write('-' * 20)

    place_list = st.session_state.get('place_list', [])
    others = place_list[4:10]

    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])  # 첫 번째 행
        col4, col5, col6 = st.columns([1, 1, 1])  # 두 번째 행

    st.write('-' * 20)

    # 페이지 하단에 양 옆에 버튼 배치
    col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col1:
        if st.button("⬅️Back"):
            go_to_page(2)

