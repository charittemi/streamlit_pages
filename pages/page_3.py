import streamlit as st

st.title('Page 3')
st.caption('テストページ作成中です')
st.subheader('')
st.text('')
markdown_text = """
# My Markdown Example

This is a paragraph of text in *italic* and **bold**.

- Item 1
- Item 2

[Link to Google](https://www.google.com)
"""
print(markdown_text)
st.text('ok')

