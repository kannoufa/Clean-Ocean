import streamlit as st
import requests
import json
import folium
from streamlit_folium import folium_static 


def getStatistiques():
    st.title('Statistiques')
    st.write('Ces statistiques sont récolter depuis l\'API de ArcGIS qui est une suite de logiciels d\'information géographique développés par la société américaine Esri.')
    st.write('')
    st.write(f'''
            Pour en savoir plus visiter leur site 
            <a href="https://www.arcgis.com/index.html" style="color:blue">
                ArcGIS
            </a>
            ''',
            unsafe_allow_html=True
        )
    
    map = folium.Map(
        location=[28, 9],
        zoom_start=4
    )
    
    data_api = getData()
    for item in data_api['features']:
        folium.Circle(
            location=[item['attributes']['LATITUDE'], item['attributes']['LONGITUDE']],
            popup=item['attributes']['CD3____KM_'],
            tooltip=item['attributes']['CD3____KM_'],
            color= 'green'
        ).add_to(map)
        
    folium_static(map)
    
    
    
# récupérer les données
def getData():
    url = 'https://services6.arcgis.com/C0HVLQJI37vYnazu/arcgis/rest/services/Estimate_of_Plastic_Pollution_in_the_World_s_Oceans_1_01_4_75/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
    response = requests.get(url)
    data = json.loads(response.text)
    return data
    
    
    