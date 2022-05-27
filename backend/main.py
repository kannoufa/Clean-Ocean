from email.policy import default
import streamlit as st
import pyrebase
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static 
import json


# API
import requests
import json
import os

def getData():
    # connexion avec l'API
    url = 'https://services6.arcgis.com/C0HVLQJI37vYnazu/arcgis/rest/services/Estimate_of_Plastic_Pollution_in_the_World_s_Oceans_1_01_4_75/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
    response = requests.get(url)
    data = json.loads(response.text)
    #print(data)
    for feature in data["features"]:
        attr = feature["attributes"]
        #st.write(
        #    attr["LATITUDE"])
        print(attr["LONGITUDE"])
        print(attr["CD1____KM_"])
        print(attr["CD2____KM_"])
        print(attr["CD3____KM_"])
        print("--------------")
    return data

firebaseConfig = {
    'apiKey': "AIzaSyAwsnONm1QsLfgvklBHl8e38aKklatteu0",
    'authDomain': "cleanoceandatabase.firebaseapp.com",
    'projectId': "cleanoceandatabase",
    'databaseURL': "https://cleanoceandatabase-default-rtdb.firebaseio.com",
    'storageBucket': "cleanoceandatabase.appspot.com",
    'messagingSenderId': "757946421887",
    'appId': "1:757946421887:web:a3c12bcbe14bc34547a54a",
    'measurementId': "G-B8RQXKXPYJ"
  }

# Firebase authentication 
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# database
db = firebase.database()
storage = firebase.storage()




# SideBar
### Authentication

home = st.sidebar.button('Accueil', default)
statistique = st.sidebar.button('statistique')
detection = st.sidebar.button('détecter les débris')
about_us = st.sidebar.button('Qui somme-nous')
choice = st.sidebar.selectbox('Se connecter/Créer un compte', ['Se connecter', 'Créer un compte'])


   

### statistique
if statistique:
    st.title("Statistiques")
    st.write("""
         ### Vous Pouvez Consultez Les Statistiques En Temps Réel Sur Les Débris Dans Les Océans
         """)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    
    chart_data2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data2)
    
    
### Detection des débris
if detection:
    st.title("Détection des débris")
    st.write("""
         ### Vous Pouvez Consulter N'importe Quel Zone Géographique Sur Google Maps Et Grace À Nos Modèles ML Vous Pouvez Savoir L'état De Polution Des Zones Choisis
         """)

### About us
if about_us:
    st.title("Qui sommes-nous")
    st.write("""
         ## Dans Le Cadre Du Module Méthodes Agiles, On Est Chaegé De Créer Une Plateforme Qui Aide Les Gens À Détecter Facilement Les Débris Dans Les Océans En Se Basant Sur Les Images Satellitaires
         ## Equipe :
         ### Bentouhali narjis : Scrum master 
         ### Hamissou abdou aminatou : Dev Team 
         ### KANNOUFA fatima ezzahra : Dev Team 
         ### Tamega bougary : Product Owner
         """)


def get_data(url):
    return json.load(open(url))
 
if home:
    
    st.title("Clean Ocean")
    st.write("""
         # Grace À Notre Site Vous Pouvez Détécter Facilement Les Plastiques Dans Les Océans
         """)
    # data = pd.read_csv('cities.csv')
    
    map = folium.Map(
        location=[45.5236, -3],
        zoom_start=2
        )
    
    
    data_api = getData()
    print('DATA : ' + str(data_api))
    
    data = [
        {
            'name': 'Bilbao',
            'latitude': 40,
            'longitude': -5,
            'color': 'pink'
        }
    ]
    for item in data_api['features']:
        folium.Circle(
            location=[item['attributes']['LATITUDE'], item['attributes']['LONGITUDE']],
            popup=item['attributes']['CD3____KM_'],
            tooltip=item['attributes']['CD3____KM_'],
            color= 'pink'
        ).add_to(map)
    folium.CircleMarker(
        radius=50,
        fill_color="#3186cc",
            location=[60, 5],
            popup='guess',
            tooltip='guess',
            icon=folium.Icon(color='red', prefix='fa',
                             icon='circle')
    ).add_to(map)
    folium_static(map)

if choice == 'Créer un compte':
    email = st.sidebar.text_input('entrer votre email')
    password = st.sidebar.text_input('entrer votre mot de passe', type="password")
    username = st.sidebar.text_input('Entrer votre nom')
    submit = st.sidebar.button('Créer un compte')
    
    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Votre compte est créé avec succès!')
        st.balloons()
        
        #sign in
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child('username').set(username)
        db.child(user['localId']).child('ID').set(user['localId'])
        st.title('Bienvenue ' + username + ' dans Clean Ocean')

if choice == 'Se connecter':
    email = st.sidebar.text_input('entrer votre email')
    password = st.sidebar.text_input('entrer votre mot de passe', type="password")
    submit = st.sidebar.button('Se connecter')
    
    if submit:
        user = auth.sign_in_with_email_and_password(email, password)
        st.title('Bienvenue dans clean ocean')
        
        
getData()  
    

    
        
       