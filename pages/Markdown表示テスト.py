import streamlit as st
import markdown_it

st.title('Markdown test page')
st.caption('Markdown表示テスト用')
st.text('')

# Create a Markdown-It instance
md = markdown_it.MarkdownIt()


# Markdown text input
st.subheader('Markdownテキスト編集欄')
markdown_text = st.text_area('（Ctrl + Enterで表示反映）', """
# Title
## Subtitle
### Another deeper title
---
This is a paragraph of text in *italic* and **bold**.
- Item 1
- Item 2

[Link to Google](https://www.google.com)
""", height=300)

# Convert Markdown to HTML
html_output = md.render(markdown_text)
st.text('')
# Display HTML output
st.subheader('Markdown ＞＞ HTML の出力結果:')
st.write(html_output, unsafe_allow_html=True)




