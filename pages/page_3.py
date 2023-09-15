import streamlit as st
import markdown_it

st.title('Page 3')
st.caption('テストページ作成中です')
st.subheader('')
st.text('')

# Create a Markdown-It instance
md = markdown_it.MarkdownIt()

# Markdown text to be converted
markdown_text = """
# My Markdown Example

This is a paragraph of text in *italic* and **bold**.

- Item 1
- Item 2

[Link to Google](https://www.google.com)
"""

# Convert Markdown to HTML
html_output = md.render(markdown_text)

# Print the HTML result
print(html_output)



