import streamlit as st
import pyrebase
from .config import firebaseConfig

# Firebase authentication 
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# database
db = firebase.database()
storage = firebase.storage()

