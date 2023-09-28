# streamlit >streamlit run main.py

import streamlit as st
from PIL import Image

st.title('basemapでカスタム地図作成')
st.text('')
st.write('basemapライブラリを用いて事業所マップを世界地図上にプロットしました.')
st.text('')
st.subheader('地図作成例')
st.text('')

image=Image.open('./data/map.png')
st.image(image)
st.text('')

#コード表示用
st.text('コードは以下の通り')
code='''
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 地図を作成します。緯度と経度の範囲を指定(南、北、左、右)
m = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=80,llcrnrlon=-25,urcrnrlon=330,resolution='c')

# 事業所の座標
places = {"Tokyo": (35.6895, 139.6917), "Fukuoka": (33.5904, 130.4017), "San Diego": (32.7157, 242.8389), "Dalian": (38.9140, 121.6147)}

# テキストのオフセット(右、上)
offsets = {"Tokyo": (1500000, -500000), "Fukuoka": (-1000000, -1800000), "San Diego": (1000000, -500000), "Dalian": (-3500000, -1200000)}

# 地図に事業所をプロットします。
for place, coords in places.items():
    lat, lon = coords
    xpt, ypt = m(lon, lat)
    m.plot(xpt, ypt, 'bo', markersize=4)  # プロットの色と形状を指定。
    offset = offsets[place]
    plt.annotate(place, xy=(xpt, ypt), xytext=(xpt+offset[0], ypt+offset[1]),
                 arrowprops=dict(facecolor='blue', arrowstyle='-'))  # プロットからの線を追加。

m.fillcontinents(color='#d3d3d3')
m.drawmapboundary()

plt.title('World Map')
# plt.show() # PNG出力の場合
plt.savefig("map.svg", format='svg') # SVG出力の場合
'''
st.code(code,language='python')
st.text('')
st.text('ok')



