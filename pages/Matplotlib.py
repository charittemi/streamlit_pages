

# streamlit >streamlit run main.py


import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

st.title('Matplotlib')
st.caption('これはグラフ表示ページです')
st.subheader('matplotlibでcsvからグラフ作成')

st.text('')
st.text('')

col1,col2=st.columns([1,2]) # カラムの比率1:2で設定
with col1:
    st.text('CSVの中身')
    #CSV挿入
    df= pd.read_csv('./data/testdata.csv',index_col='No')
    st.dataframe(df)
    
with col2:
    st.text('これをグラフにすると...')

    # matplot棒グラフを生成する
    fig, ax = plt.subplots()  
    ax.bar(df.index, df['Value'])

    # タイトル、X軸ラベル、Y軸ラベルを設定する
    ax.set_title('matplotlib graph')
    ax.set_xlabel('No')
    ax.set_ylabel('Value')

    # Streamlitにプロットを表示する
    st.pyplot(fig)
    
    
    #コード表示用
code='''
col1,col2=st.columns([1,2]) # カラムの比率1:2で設定
with col1:
    st.text('CSVの中身')
    #CSV挿入
    df= pd.read_csv('./data/testdata.csv',index_col='No')
    st.dataframe(df)
    
with col2:
    st.text('これをグラフにすると...')

    # matplot棒グラフを生成する
    fig, ax = plt.subplots()  
    ax.bar(df.index, df['Value'])

    # タイトル、X軸ラベル、Y軸ラベルを設定する
    ax.set_title('matplotlib graph')
    ax.set_xlabel('No')
    ax.set_ylabel('Value')

    # Streamlitにプロットを表示する
    st.pyplot(fig)
'''
st.code(code,language='python')
