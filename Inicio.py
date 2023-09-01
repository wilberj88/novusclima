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
  - 🔎 _    Diagnóstico de tu Riesgo Climático y de Brecha de Neutralidad a 2050
  - ➡️ _    Recomendación de Póliza Climática: Transición energética con Aseguramiento climático
  - 📜 _     Propuesta Personalizada de Contrato Inteligente 
  
  Todo lo anterior basado en:
  🤖 Tecnología para la modelación de riesgos climáticos y transición energética
  💰 CarbonTokens para Neutralidad de Cabrono y BioTokens para Mitigación y Adaptación Climática
  ♻️ Interoperabilidad entre soluciones basadas en la naturales
  
  
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)
