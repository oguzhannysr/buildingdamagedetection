import streamlit as st
import leafmap.foliumap as leafmap
import requests
import json

#%%
st.set_page_config(layout="wide")

st.sidebar.info("""
        Kahramanmaraş Depremi sonrasında Gaziantep ili İslahiye ilçesinde yapılan hasar tespit çalışmaları
    """)
# Leafmap ile bir harita oluştur
m = leafmap.Map()

# JSON dosyalarını bulmak için linki ziyaret et
url = "https://api.github.com/repos/giswqs/maxar-open-data/contents/datasets/Kahramanmaras-turkey-earthquake-23"
response = requests.get(url)
data = json.loads(response.text)
yikik = st.sidebar.checkbox("Yıkılan Binalar",value=False)
acil = st.sidebar.checkbox("Acil Yıkılması Gereken Binalar",value=False)
agir = st.sidebar.checkbox("Ağır Hasarlı Binalar",value=False)

st.sidebar.info("""
        Bu bölümde il ya da ilçe sınırları görüntülebilmektedir.
    """)

if yikik:
    m.add_geojson("https://raw.githubusercontent.com/oguzhannysr/buildingdamagedetection/main/islahiye_binatespit_yikik.geojson", layer_name="Yıkılan Binalar")
if acil:
    m.add_geojson("https://raw.githubusercontent.com/oguzhannysr/buildingdamagedetection/main/islahiye_binatespit_acil.geojson", layer_name="Acil Yıkılması Gereken Binalar")
if agir:
    m.add_geojson("https://raw.githubusercontent.com/oguzhannysr/buildingdamagedetection/main/islahiye_binatespit_agir.geojson", layer_name="Ağır Hasarlı Binalar")
    
il = st.sidebar.checkbox("İl Sınırları",value=False)
islahiye = st.sidebar.checkbox("İslahiye İlçe Sınırları",value=False)   

style = {
    "stroke": True,
    "color": "#0000ff",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,
}

style2 = {
    "stroke": True,
    "color": "#ff0000",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#ff0000",
    "fillOpacity": 0.1,
}

hover_style = {"fillOpacity": 0.3}

if il:
    m.add_geojson("https://raw.githubusercontent.com/oguzhannysr/buildingdamagedetection/main/türkiye_boundary.geojson", layer_name="İl Sınırları",style=style, hover_style=hover_style)
if islahiye:
    m.add_geojson("https://raw.githubusercontent.com/oguzhannysr/buildingdamagedetection/main/islahiye_boundary.geojson", layer_name="İslahiye İlçe Sınırları",style=style2, hover_style=hover_style) 
    
    
m.add_stac_layer("https://raw.githubusercontent.com/giswqs/maxar-open-data/master/datasets/Kahramanmaras-turkey-earthquake-23/1040010082698700.json", name="1040010082698700")
m.to_streamlit()

