# Local URL: http://localhost:8501
# Network URL: http://192.168.0.24:8501

# streamlit >streamlit run main.py


import streamlit as st
from PIL import Image

st.title('タイトル')
st.caption('これはテスト用です')
st.subheader('About')
st.text('streamlitでテストページを作ってみました')

image = Image.open('.\\data\\okojo_side.jpg')
st.image(image, width=250)
st.text('')

#コード表示用
code='''
import streamlit as st
from PIL import Image

st.title('タイトル')
st.caption('これはテスト用です')
st.subheader('About')
st.text('streamlitでテストページを作ってみました')

image = Image.open('.\\data\\okojo_side.jpg')
st.image(image, width=250)
st.text('')
'''
st.code(code,language='python')
st.text('')
st.text('')

