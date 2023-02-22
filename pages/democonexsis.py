import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Clima", page_icon="⛅")

st.title('Novus Clima ⛅ Demo by NovusTech+Exsis')
st.header("¿Sabes cuánto te costaría la próxima crisis climática en tu zona?🌎")
st.write("Averígualo ahora 🕰")


territorio = st.selectbox("Indica el Territorio",
        ("Santander", "Tolima", "Caribe", "Pacífico", "Amazonas"),
    )
categoria = st.radio(
        "Indica la crisis para la cual te quieres preparar👇 ",
        options=['Inundación', 'Sequía','Incendios', 'Huracanes', 'Deslizamientos'],
    )
