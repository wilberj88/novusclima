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
    col1.metric("Riesgos", "70%", "40%")
    col2.metric("Oportunidades", "30%", "-82%")
    
    def render_basic_radar():
        option = {
                "title": {"text": "Costos estimados por tipos de Riesgos Climáticos"},
                "legend": {"data": ["Riesgo Detectado", "Riesgo Gestionado"]},
                "radar": {
                    "indicator": [
                        {"name": "Derrumbes", "max": 6500},
                        {"name": "Sequías", "max": 16000},
                        {"name": "Incendios", "max": 30000},
                        {"name": "Inundaciones", "max": 38000},
                        {"name": "Deslizamientos", "max": 52000},
                        {"name": "Contaminación", "max": 25000},
                    ]
                },
                "series": [
                    {
                        "name": "Costo Estimado Vs Costo Mitigado",
                        "type": "radar",
                        "data": [
                            {
                                "value": [2000, 10000, 20000, 3500, 15000, 11800],
                                "name": "Riesgo Detectado",
                            },
                            {
                                "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                "name": "Riesgo Gestionado",
                            },
                        ],
                    }
                ],
            }
        st_echarts(option, height="500px")
    render_basic_radar()
        
        
        
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
