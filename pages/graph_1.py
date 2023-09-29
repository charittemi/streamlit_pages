import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t


st.title('Graph')
st.caption('グラフ読み込み確認用ページ')
st.text('')


# Streamlit UI部分
st.title("t分布の可視化")

# 標準偏差のスライダー
std_dev = st.slider("標準偏差", 1.0, 10.0, 5.0)

# 自由度（例: 10）
df = 10

# t分布を計算
x = np.linspace(-10, 10, 400)
pdf = t.pdf(x, df, scale=std_dev)

# グラフを描画
plt.figure(figsize=(8, 6))
plt.plot(x, pdf, label=f't分布 (自由度={df}, 標準偏差={std_dev})')
plt.xlabel('x')
plt.ylabel('確率密度')
plt.legend()
st.pyplot(plt)


col1,col2=st.columns([2,3]) # カラムの比率2:3で設定
with col1:
    df= pd.read_csv('./data/testdata.csv',index_col='No')
    
    # matplot棒グラフを生成する
    fig, ax = plt.subplots()  
    ax.bar(df.index, df['Value'])

    # タイトル、X軸ラベル、Y軸ラベルを設定する
    ax.set_title('matplotlib graph')
    ax.set_xlabel('No')
    ax.set_ylabel('Value')

    # Streamlitにプロットを表示する
    st.pyplot(fig)
with col2:
    st.text('グラフの説明')