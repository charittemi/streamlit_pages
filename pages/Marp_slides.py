import streamlit as st

# Streamlitアプリのタイトルを設定
st.title("Marp slides")

# 埋め込みたいWebページのURL
url = "https://charittemi-slide1.streamlit.app/Slide_1"

# iframeを作成して指定したURLを埋め込む
st.components.v1.iframe(url, width=900)
