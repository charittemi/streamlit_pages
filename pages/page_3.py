import streamlit as st
import markdown_it

st.title('Page 3')
st.caption('テストページ作成中です')
st.subheader('')
st.text('')

# Create a Markdown-It instance
md = markdown_it.MarkdownIt()

# Markdown text input
markdown_text = st.text_area('Enter Markdown Text', """
# My Markdown Example

This is a paragraph of text in *italic* and **bold**.

- Item 1
- Item 2

[Link to Google](https://www.google.com)
""")

# Convert Markdown to HTML
html_output = md.render(markdown_text)

# Display HTML output
st.write('HTML Output:')
st.write(html_output, unsafe_allow_html=True)




