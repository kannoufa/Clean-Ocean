import streamlit as st
import streamlit as st
import pyrebase
from PIL import Image



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


def signup():
    st.title('Créer un compte')
    
    col1, col2 = st.columns(2)

    with col1:
        image = Image.open('static/images/logo.png')
        st.image(image)

    with col2:
        email = st.text_input('entrer votre email')
        username = st.text_input('entrer votre nom')
        password = st.text_input('entrer votre mot de passe', type="password")
        submit = st.button('Créer un compte')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Votre compte est créé avec succès!')
        st.balloons()
        st.write(f'''
            <a href="http://localhost:5000/clean-ocean/login" style="color:green">
                Connectez-vous
            </a>
            ''',
            unsafe_allow_html=True
        )
        
        
        
def signin():
    st.title('Se connecter')
    
    col1, col2 = st.columns(2)

    with col1:
        image = Image.open('static/images/logo.png')
        st.image(image)

    with col2:
        email = st.text_input('entrer votre email')
        password = st.text_input('entrer votre mot de passe', type="password")
        submit = st.button('Se connecter')
        st.write(f'''
            <a href="http://localhost:5000/clean-ocean/signup">
                Vous n'avez pas de compte? créez-le ;)
            </a>
            ''',
            unsafe_allow_html=True
        )
    
    
    if submit:
        user = auth.sign_in_with_email_and_password(email, password)
        st.success('Bienvenue sur Clean Ocean')
        st.balloons()