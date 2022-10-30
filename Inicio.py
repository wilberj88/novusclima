import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Clima", page_icon="⛅")

st.title('Novus Clima ⛅')
st.header("Ahorra 💰 mientras salvamos juntos el planeta 🌎")

st.write("Bienvenidos al futuro climático 👋")

st.markdown(
  """
  En esta web encontrarás:
  - 🔎 _    Diagnóstico de tu riesgo climático
  - 🛒 _    Recomendación de Seguro y Planes de Mitigación y Adaptación
  - ✍️ _     Propuesta Inteligente de Contrato
  
  Todo lo anterior basado en:
  - Tecnología para la modelación de riesgos climáticos
  - Tecnología para la neutralidad de carbono: Planes de Mitigación
  - Tecnología para salvar el planeta: Innovación en toda la cadena energética y Planes de Adaptación
  
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)

st.write("Análisis Espacial de Datos")

#datos

df = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

#mapa
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
