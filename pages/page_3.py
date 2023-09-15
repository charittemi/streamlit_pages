import streamlit as st
import markdown_it

st.title('Page 3')
st.caption('Markdownテスト用')
st.subheader('')
st.text('')

# Create a Markdown-It instance
md = markdown_it.MarkdownIt()

# Markdown text input
markdown_text = st.text_area('Markdown編集欄（Ctrl + Enterで表示反映）', """---
# Title
## Subtitle
### Another deeper title
---
This is a paragraph of text in *italic* and **bold**.
>- Item 1
>- Item 2

[Link to Google](https://www.google.com)
""", height=300)

# Convert Markdown to HTML
html_output = md.render(markdown_text)

# Display HTML output
st.write('Markdown ＞＞ HTML の出力結果:')
st.write(html_output, unsafe_allow_html=True)




