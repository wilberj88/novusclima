import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk
from streamlit_echarts import st_echarts
import plotly.figure_factory as ff
import altair as alt
#import folium
#from streamlit_folium import st_folium

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Clima", page_icon="⛅")

st.title('Novus Clima ⛅ Demo 2 by NovusTech + Exsis')
st.header("¿Sabes cuánto te costaría la próxima crisis climática en tu zona?🌎")
#st.write("Selecciona una zona en el mapa y averígualo ahora 🕰")

territorio = st.selectbox("Indica el Territorio",
        ("Santander", "Tolima", "Ciudad de México", "Miami", "Monterrey"),
    )
categoria = st.radio(
        "Indica el periodo de análisis👇 ",
        options=['2030', '2035','2040', '2045', '2050'],
    )


if st.button('Calcular diagnóstico gratuito'):
    st.header("Diagnóstico de Riesgos Climáticos")
    st.write("Probabilidades de ocurrencia en el periodo ", categoria)
    col1, col2 = st.columns(2)
    
st.write("""
**No asumas estos riesgos sin estar blindado**
- Asegúrate con `Novus Clima` y `Exsis` y despreocúpate de los riesgos climáticos
""")
st.write('---')

if st.button('Activa tu plan anual de Monitoreo + Mitigación + Adaptación'):    
        st.title('Tenemos un contrato 📜  personalizado 🎯 a tu diagnóstico 🔎 ')
        st.text_input("Incorpore su firma si está de acuerdo con las condiciones")

        st.text_input("Incorpore su correo electrónico para envío de factura")
        st.write('Gracias por confiar en los servicios de Novus Clima ⛅ y Exsis')
        
        
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
