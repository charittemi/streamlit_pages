import streamlit as st
from PIL import Image

st.title('Page 2')
st.caption('')
st.subheader('')
st.text('')

image=Image.open('./data/okojo.jpg')
st.image(image, width=250)
st.text('')

# Markdownセクション
markdown = r"""

"""
st.markdown(markdown)



st.write('')
#コードセクション
code = '''

'''
st.code(code)
