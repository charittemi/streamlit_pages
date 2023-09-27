
import streamlit as st

st.title('Slide 1')
st.subheader('Marpスライドの複数カラムレイアウト例')
st.text('カスタムCSSを適用')

# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=720, height=540)
st.text('')