# import streamlit as st
# from google.cloud import vision
# from google.cloud.vision import types
# import io
# from PIL import Image

# # Google Cloud Vision APIのクライアントを設定
# def setup_vision_client():
#     client = vision.ImageAnnotatorClient()
#     return client

# # 画像をアップロードし、OCRを実行する関数
# def perform_ocr(image, client):
#     content = image.read()
#     image = types.Image(content=content)
#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     return texts


# # Streamlitアプリケーション
# def main():
#     st.title("Google OCRアプリ")

#     # 画像アップロードパーツ
#     uploaded_image = st.file_uploader("画像をアップロードしてください", type=["jpg", "png", "jpeg"])
#     if uploaded_image is not None:
#         # 画像表示
#         image = Image.open(uploaded_image)
#         st.image(image, caption="アップロードされた画像", use_column_width=True)

#         # 実行ボタン
#         if st.button("OCRを実行"):
#             st.write("OCRを実行中...")
#             client = setup_vision_client()
#             texts = perform_ocr(uploaded_image, client)

#             # テキスト出力パーツ
#             if texts:
#                 st.subheader("OCR 結果:")
#                 for text in texts:
#                     st.write(text.description)

# if __name__ == "__main__":
#     main()
