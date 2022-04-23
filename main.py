from email.policy import default
import streamlit as st
import pyrebase
import pandas as pd
import numpy as np

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

if home:
    st.title("Clean Ocean")
    st.write("""
         # Grace À Notre Site Vous Pouvez Détécter Facilement Les Plastiques Dans Les Océans
         """)

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
        
        
        
        
       