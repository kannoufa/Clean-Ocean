import streamlit as st
import folium
from streamlit_folium import folium_static 

def detectionDebris():
    st.title('détection des débris')
    st.write('Choisir une zone dans le map')
    
    map = folium.Map(
        location=[28, 9],
        zoom_start=4
    )
    
    latLon = folium.LatLngPopup()
    print(latLon)
    map.add_child(latLon)
    
    folium_static(map)