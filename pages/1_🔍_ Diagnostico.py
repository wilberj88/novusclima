import streamlit as st
import pandas as pd
import numpy as np

st.title('Diagnosticamos tu riesgo climático ⛈️')
st.write('Indica la ubicación y modelaremos los riesgos del próximo año')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.text_input("¿Cuál es tu presupuesto anual para desastres climáticos?", key="presupuesto")
