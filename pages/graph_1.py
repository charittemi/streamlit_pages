import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import t


st.title('t分布の可視化')
st.caption('スライダーを動かして標準偏差を変えることで分布の形が変わります')
st.text('')

# 標準偏差のスライダー
std_dev = st.slider("標準偏差", 1.0, 10.0, 5.0)

# 自由度（例: 10）
df = 10

# t分布を計算
x = np.linspace(-10, 10, 400)
pdf = t.pdf(x, df, scale=std_dev)

# グラフのサイズをページ幅の半分に設定
st.set_option('deprecation.showPyplotGlobalUse', False)
fig, ax = plt.subplots(figsize=(st._config.get_option("theme.primaryColor"), st._config.get_option("theme.primaryColor") / 2))


# グラフを描画
plt.figure(figsize=(8, 6))
plt.plot(x, pdf, label=f't分布 (自由度={df}, 標準偏差={std_dev})')
plt.xlabel('x')
plt.ylabel('確率密度')
plt.legend()
st.pyplot(plt)


