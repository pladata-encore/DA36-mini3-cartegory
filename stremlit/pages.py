# pages.py

import streamlit as st

def main_page():
    main_bg_color = "#CEF6F5"  # 메인 페이지 배경색

    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {main_bg_color};
        }}
        </style>
    """, unsafe_allow_html=True)

    st.image("data/park.jpg")
    st.title("Where to Park?")
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Show me your car"):
        return 2  # 페이지 2로 이동
    return 1

def upload_page():
    main_bg_color = "#ECF8E0"  # 메인 페이지 배경색
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {main_bg_color};
        }}
        </style>
    """, unsafe_allow_html=True)

    st.title('어쩌구')
    st.write('-' * 10)

    st.subheader('upload here⬇️')
    img_file = st.file_uploader('', type=['png', 'jpg', 'jpeg'])
    st.markdown('Your car is..')
    st.markdown('Accuracy is..')

    col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기
    with col1:
        if st.button("⬅️Back"):
            return 1  # 페이지 1로 이동
    with col3:
        if st.button("More"):
            return 3  # 페이지 3으로 이동

    return 2

def more_page():
    main_bg_color = "#F8E6E0"  # 메인 페이지 배경색
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {main_bg_color};
        }}
        </style>
    """, unsafe_allow_html=True)

    st.title("More about EV!")
    st.write('-' * 20)

    place_list = st.session_state.get('place_list', [])
    others = place_list[4:10]

    col1, col2, col3 = st.columns([1, 1, 1])  # 첫 번째 행
    col4, col5, col6 = st.columns([1, 1, 1])  # 두 번째 행

    st.write('-' * 20)

    col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기
    with col1:
        if st.button("⬅️Back"):
            return 2  # 페이지 2로 이동

    return 3
