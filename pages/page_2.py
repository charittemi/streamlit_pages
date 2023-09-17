import streamlit as st
from PIL import Image

st.title('Page 2')
st.caption('テストページ作成中です')
st.subheader('')
st.text('')

image=Image.open('./data/okojo.jpg')
st.image(image, width=250)
st.text('ok')

# Markdown
markdown = """

$e^{i\theta}$ は $\cos\theta$ と $i\sin\theta$ の和です。

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

$e^{i\\th}$ は $cos\\th$ と $i\\sin\\th$ の和です。

$$
e^{i\\th} = cos\\th + i\\sin\\th
$$


"""
st.markdown(markdown)
