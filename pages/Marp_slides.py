
import streamlit as st

st.title('Marp Slides')
st.subheader('')
st.text('作成例')
url = "https://charittemi-slide1.streamlit.app/Slide_1"
st.markdown(f"[{url}]({url})")

# # Slide1.htmlを埋め込む
# with open('Slide1.html', 'r', encoding='utf-8') as html_file:
#     slide_html = html_file.read()

# st.components.v1.html(slide_html, width=720, height=540)
# st.text('')