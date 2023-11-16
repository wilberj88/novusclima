import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk
from streamlit_echarts import st_echarts
import plotly.figure_factory as ff
import altair as alt
import plotly.graph_objects as go
import urllib, json
import folium
from streamlit_folium import st_folium
from streamlit_extras.colored_header import colored_header



# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Clima", page_icon="⛅")

st.title('Propuesta de Novus Clima ⛅ a Selvar 🌎')

colored_header(
    label="1. Alianza Comercial",
    description="Abarcar clientes conjuntos",
    color_name="violet-70",
)
with st.expander("Alcance"):
    st.subheader('Traer clientes')
    st.write('Centrales de Mando desde 2.500 USD mes')
    st.write('Comisión comercial: 20%')

colored_header(
    label="2. Alianza Financiera",
    description="Ayudar a financiar el Centro de Investigación y Desarrollo",
    color_name="violet-70",
)
with st.expander("Alcance"):
    st.subheader('Traer Inversionistas')
    st.write('Etapa 1: 1M USD')
    st.write('Etapa 2: 3M USD')
    st.write('Etapa 3: 10M USD')
    st.write('Comisión de banca de inversión: 5%')
    
colored_header(
    label="3. Alianza Operativa",
    description="Co Crear Juntos",
    color_name="violet-70",
)
with st.expander("Alcance"):
    st.subheader('Co crear Sistemas de Mitigación y Adaptación')
    st.write('Propiedad Intelectual Compartida')
    st.write('Participación comercial por sistema: 50%')
