import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Graph')
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