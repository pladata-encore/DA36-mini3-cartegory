import streamlit as st
import streamlit as st
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

if 'page' not in st.session_state:
    st.session_state['page'] = 1
# 페이지 변경 함수
def go_to_page(page_num):
    st.session_state['page'] = page_num

# if st.session_state['page'] == 1:
#     main_bg_color = "#CEF6F5"  # 메인 페이지 배경색
#
#     # CSS 스타일을 적용하여 배경 색 변경
#     st.markdown(f"""
#             <style>
#             /* 메인 페이지 배경 색 설정 */
#             .stApp {{
#                 background-color: {main_bg_color};
#             }}
#             </style>
#             """, unsafe_allow_html=True)
#     # st.image("data/jeju.gif", use_column_width=True)
#     st.image("data\park.jpg")
#     st.title("Where to Park?")
#     st.markdown("<br>", unsafe_allow_html=True)

if st.session_state['page'] == 1:
    # 배경 이미지 URL 또는 경로 설정
    background_image_url = "data/park.jpg"

    # CSS 스타일을 적용하여 배경 이미지 설정
    st.markdown(f"""
            <style>
            /* 메인 페이지 배경 이미지 설정 */
            .stApp {{
                background-image: url({background_image_url});
                background-size: cover;  /* 이미지 크기가 화면을 덮도록 설정 */
                background-position: center;  /* 이미지의 중앙에 위치하도록 설정 */
                background-repeat: no-repeat;  /* 이미지를 반복하지 않도록 설정 */
                
            /* 오버레이 추가 */
            .stApp::after {{
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.3);  /* 반투명 검정색 오버레이 */
                z-index: -1;  /* 오버레이를 내용 뒤에 배치 */
                
            }}
            </style>
            """, unsafe_allow_html=True)

    st.title("Where to Park?")
    st.markdown("CARTEGORY BY 하와수")
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Show me your car"):
        go_to_page(2)

# 페이지별 내용 표시
elif st.session_state['page'] == 2:
    # 배경색 설정 (고정)
    main_bg_color = "#F8E6E0"  # 메인 페이지 배경색
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
    st.title('Please register your vehicle 👀')
    # if st.button("시작 화면으로️"):
    #     go_to_page(1)
    st.write('-'*10)
    # sidebar input
    # 첫 번째 구간
    # 선택된 옵션 - 메인 페이지에 표시
    st.subheader('upload here⬇️')

    # 모델 로드
    @st.cache_resource  # 캐싱을 통해 모델 로드 속도 향상
    def load_trained_model(model_path):
        return load_model(model_path)

    model_path = "mb_model.h5"
    model_path = "Xception_model.h5"
    model = load_trained_model(model_path)

    label_classes = ['Carens', 'Kona', 'Mohave', 'Niro', 'Palisade', 'Santafe',
                     'Seltos', 'Sorento', 'Soul', 'Sportage', 'Tucson', 'Veracruz']

    electric_vehicles = ['Kona', 'Niro', 'Model', 'Santefe', 'Palisade']

    # 이미지 업로드
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # 업로드된 파일 정보 표시
        # st.write("file name:", uploaded_file.name)
        # st.write("file type:", uploaded_file.type)
        # st.write("file size:", uploaded_file.size, "byte")

        # 업로드된 이미지 표시
        st.image(uploaded_file, caption="car image", use_column_width=True)

        # 이미지 전처리
        IMAGE_SIZE = 299  # MobileNetV2 입력 크기
        image = Image.open(uploaded_file).convert("RGB")  # 이미지를 RGB로 변환
        image = image.resize((IMAGE_SIZE, IMAGE_SIZE))  # 크기 조정
        image_array = np.array(image)
        image_array = preprocess_input(image_array)
        batch_image = np.expand_dims(image_array, axis=0)

        pred_proba = model.predict(batch_image)
        pred_index = np.argmax(pred_proba)
        pred_label = label_classes[pred_index]
        confidence = pred_proba[0][pred_index]

        # 예측 결과 출력
        st.success(f"🚗...Your car is {pred_label}")
        st.success(f"🤖 Accuracy is...{confidence * 100:.2f}%")

        # 전기차일 경우 안내 문구 출력
        if pred_label in electric_vehicles:
            st.markdown(f"잠깐🤚🏻 {pred_label}는 전기차입니다! 지상 주차장을 이용해주세요.")
        else:
            st.info(f"{pred_label}는 지하 주차장에 진입할 수 있습니다. 🥳")

        # 서버에 이미지 저장
        SAVE_DIR = "./uploaded_images"
        os.makedirs(SAVE_DIR, exist_ok=True)
        save_path = os.path.join(SAVE_DIR, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        # st.info(f"The image is successfully saved: {save_path}")

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
    main_bg_color = "#ECF8E0"  # 메인 페이지 배경색

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

