import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import t


st.title('t分布の可視化')
st.caption('スライダーを動かして標準偏差を変えることで分布の形が変わります')
st.text('')

# 標準偏差のスライダー
std_dev = st.slider("標準偏差", 1.0, 8.0, 4.0)
st.text('')
# 自由度（例: 10）
df = 10

# t分布を計算
x = np.linspace(-10, 10, 400)
pdf = t.pdf(x, df, scale=std_dev)

# グラフを描画
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label=f't分布 (自由度={df}, 標準偏差={std_dev})')
plt.xlabel('x')
plt.ylabel('確率密度')

# y軸の範囲を固定?
plt.ylim(0, 0.4)  
plt.legend()
st.pyplot(plt)


