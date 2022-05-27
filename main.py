import streamlit as st

from functions.signup_signin import *
from functions.statistiques import getStatistiques
from functions.detection_debris import detectionDebris


def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path


if navigation() == "detection-debris":
    detectionDebris()

elif navigation() == "statistiques":
    getStatistiques()

elif navigation() == "login":
    signin()

elif navigation() == "signup":
    signup()

