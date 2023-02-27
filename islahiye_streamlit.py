import streamlit as st
import leafmap.foliumap as leafmap
import requests
import json
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

if yikik:
    m.add_geojson("https://raw.githubusercontent.com/oguzhannysr/buildingdamagedetection/main/islahiye_binatespit_yikik.geojson", layer_name="Yıkılan Binalar")

if acil:
    m.add_geojson("https://raw.githubusercontent.com/oguzhannysr/buildingdamagedetection/main/islahiye_binatespit_acil.geojson", layer_name="Acil Yıkılması Gereken Binalar")
if agir:
    m.add_geojson("https://raw.githubusercontent.com/oguzhannysr/buildingdamagedetection/main/islahiye_binatespit_agir.geojson", layer_name="Ağır Hasarlı Binalar")
    
    
    
    
m.add_stac_layer("https://raw.githubusercontent.com/giswqs/maxar-open-data/master/datasets/Kahramanmaras-turkey-earthquake-23/1040010082698700.json", name="1040010082698700")
m.to_streamlit()

