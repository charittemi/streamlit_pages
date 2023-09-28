# streamlit >streamlit run main.py

import streamlit as st
from PIL import Image

st.title('cartopyでカスタム地図作成')
st.text('')
st.write('basemapとほぼ同じ世界地図をcartopyを用いて作成しました。\n地図の中心経度を変更した際の表示調整はbasemapのほうが簡単な印象でした')
st.subheader('地図作成例')
st.text('')

image=Image.open('./data/map_cartopy.png')
st.image(image)
st.text('')

#コード表示用
st.text('コードは以下の通り')
code='''
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# 地図を作成します。緯度と経度の範囲を指定(左、右、下、上)
fig = plt.figure(figsize=(9, 10))
central_longitude = 135
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=central_longitude))
ax.set_extent([central_longitude - 150, central_longitude + 175, -60, 90], crs=ccrs.PlateCarree())

# 事業所の座標
places = {"Tokyo": (35.6895, 139.6917), "Fukuoka": (33.5904, 130.4017), "San Diego": (32.7157, -117.1611), "Dalian": (38.9140, 121.6147)}

# 地図に事業所をプロットします。
# 事業所の名前とその座標のオフセットを指定します。(右、上)
offsets = {"Tokyo": (8, -10), "Fukuoka": (-25, -10), "San Diego": (-40, -15), "Dalian": (-35, 0)}
for place, coords in places.items():
    lat, lon = coords
    ax.plot(lon, lat, 'bo', markersize=4, transform=ccrs.PlateCarree())
    ax.annotate(place, xy=(lon, lat), xycoords=ccrs.PlateCarree()._as_mpl_transform(ax),
                xytext=offsets[place], textcoords='offset points')

ax.add_feature(cfeature.LAND, facecolor='#D3D3D3')
ax.add_feature(cfeature.OCEAN, facecolor='white')

plt.title('World Map')
plt.savefig("map.svg", format='svg') # PNGならplt.show()
'''
st.code(code,language='python')
st.text('')
st.text('ok')



