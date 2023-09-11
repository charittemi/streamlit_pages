import streamlit as st
from PIL import Image

st.title('Page 2')
st.caption('テストページ作成中です')
st.subheader('')
st.text('')

image=Image.open('./data/okojo.jpg')
st.image(image, width=250)
st.text('ok')

