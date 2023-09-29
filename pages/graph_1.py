﻿import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import t,norm

st.title('t分布と正規分布')
st.caption('スライダーを動かして自由度を変えるとt分布の形が変わります')
st.text('')

# 自由度のスライダー
df = st.slider("自由度", 2, 50, 2)
st.text('')
# 固定された標準偏差
std_dev = 1.0

# t分布を計算
x = np.linspace(-10, 10, 400)
pdf = t.pdf(x, df, scale=std_dev)

# 正規分布を計算
norm_pdf = norm.pdf(x, loc=0, scale=std_dev)

# グラフを描画
plt.figure(figsize=(5,3))
plt.plot(x, pdf, label=f't分布 (自由度={df}, 標準偏差={std_dev})')
plt.plot(x, norm_pdf, label=f'正規分布 (標準偏差={std_dev})', color='orange')
plt.xlabel('x')
plt.ylabel('確率密度')

# y軸の範囲を固定
plt.ylim(0, 0.45)  
plt.legend()
st.pyplot(plt)
