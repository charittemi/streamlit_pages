import streamlit as st
from PIL import Image

st.title('Page 2')
st.caption('テストページ作成中です')
st.subheader('')
st.text('')

image=Image.open('./data/okojo.jpg')
st.image(image, width=250)
st.text('')

# Markdown
markdown = r"""

$e^{i\theta}$ は $\cos\theta$ と $i\sin\theta$ の和です。

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

"""
st.markdown(markdown)

st.write()

# Markdownで数式を記述する際、文字列の先頭に` r `をつけることで、pythonのraw stringとして扱われ、エスケープシーケンスが無効化されます。これにより、Markdown内で\記号をそのまま使用することが可能になります。

markdown = r"""

$e^{i\theta}$ は $\cos\theta$ と $i\sin\theta$ の和です。

"""
st.markdown(markdown)
