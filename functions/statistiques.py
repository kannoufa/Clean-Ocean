import streamlit as st
import requests
import json
import folium
from streamlit_folium import folium_static 


def getStatistiques():
    st.title('Statistiques')
    
    st.write(f'''
            <div >
                Savez-vous que <span style="color:#E06F85" >plus de 5 billions de pièces de plastique</span> pesant plus de 250 000 tonnes à flot en mer ! 
            </div><br>
            
            <div>
                La carte ci-dessous vous présente des Estimation de la pollution plsatique dans les océans du monde
            </div><br>
            
            <div style="color:#3c6382">
                Ces statistiques sont récolter depuis l\'API de ArcGIS qui est une suite de logiciels d\'information géographique développés par
                la société américaine Esri.
            </div><br>
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
            popup='Estimation de la pollution plsatique dans les océans du monde (/km2) ' + str(item['attributes']['CD3____KM_']),
            tooltip='Estimation de la pollution plsatique dans les océans du monde (/km2) ' + str(item['attributes']['CD3____KM_']),
            color= 'green'
        ).add_to(map)
        
    folium_static(map)
    
    st.write(f'''
            Pour en savoir plus visiter les sites suivantes : 
            <a href="https://www.arcgis.com/index.html" style="color:#0B539C; margin-right: 10px; margin-left: 10px;">
                ArcGIS
            </a>
            <a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0111913" style="color:#0B539C">
                PLOS ONE 
            </a>
            ''',
            unsafe_allow_html=True
    )
    
    
    
# récupérer les données
def getData():
    url = 'https://services6.arcgis.com/C0HVLQJI37vYnazu/arcgis/rest/services/Estimate_of_Plastic_Pollution_in_the_World_s_Oceans_1_01_4_75/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
    response = requests.get(url)
    data = json.loads(response.text)
    return data


# https://hub.arcgis.com/maps/uneplive::estimate-of-plastic-pollution-in-the-worlds-oceans/explore?location=-0.043402%2C-20.654350%2C-1.00
    
    
    