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
This is a paragraph of text in *italic* and **bold**.
- Item 1
- Item 2
---

[参考: Markdownの書き方](https://openstudy.jp/contribute/markdown-cheetsheet/)

---

""", height=250)

# Convert Markdown to HTML
html_output = md.render(markdown_text)
st.text('')
# Display HTML output
st.subheader('Markdown ＞＞ HTML の出力結果:')
st.write(html_output, unsafe_allow_html=True)




st.text('')
st.subheader('Markdown記法で数式がうまく表示されない場合')
st.text('文字列の先頭に` r `をつけることで、pythonのraw stringとして扱われ、  
        エスケープシーケンスが無効化されるためMarkdown内で'\'記号をそのまま使用可能になります')

markdown = r"""

$e^{i\theta}$ は $\cos\theta$ と $i\sin\theta$ の和です。

"""
st.markdown(markdown)

code = '''

<!-- 。-->

markdown = r"""

$e^{i\theta}$ は $\cos\theta$ と $i\sin\theta$ の和です。

"""
st.markdown(markdown)

'''
st.code(code)