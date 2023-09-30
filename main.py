# streamlit >streamlit run main.py

# 初期化時に一度だけ実行される処理
#image=Image.open('./data/okojo_side.jpg')
@st.cache
def load_image(path):
    return Image.open(path)

def main():
    st.title('はじめに')
    st.caption('本サイトはpython学習記録として作成したものであり、各種ライブラリを試しています.')
    st.subheader('About')
    st.text('streamlitでテストページを作ってみました')

    # 予めキャッシュしておいた画像を使用
    image = load_image('./data/okojo_side.jpg')
    st.image(image, width=250)
    st.text('')
    
#コード表示用
code='''
import streamlit as st
from PIL import Image

st.title('はじめに')
st.caption('本サイトはpython学習記録として作成したものです')
st.subheader('About')
st.text('streamlitでテストページを作ってみました')

image=Image.open('./data/okojo_side.jpg')
st.image(image, width=250)
'''
st.code(code,language='python')
st.text('')
st.text('')

