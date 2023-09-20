import streamlit as st
from google_drive_ocr.application import GoogleOCRApplication
import os

# Streamlitアプリのタイトルを設定
st.title("Google OCRアプリ")

# 画像ファイルをアップロードするセクションを作成
uploaded_image = st.file_uploader("画像ファイルをアップロードしてください", type=["jpg", "png", "jpeg"])

# GoogleOCRApplicationを初期化
app = GoogleOCRApplication('./ocrch_client_secret.json')

# 実行ボタンがクリックされたかどうかを示すフラグ
execute_ocr = st.button("実行")

# OCRを実行するセクション
if uploaded_image is not None and execute_ocr:
    try:
        # 画像を一時的に保存
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_image.read())
        
        # OCRを実行
        extracted_text = app.perform_ocr("temp_image.jpg")

        # 出力テキストをカラム内に表示
        col1, col2 = st.columns(2)
        with col1:
            st.header("OCRの結果:")
        with col2:
            st.text(extracted_text)
    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")
    finally:
        # 一時ファイルを削除
        os.remove("temp_image.jpg")
