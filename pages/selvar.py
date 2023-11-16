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


colored_header(
    label="2. Alianza Financiera",
    description="Financiar el Centro de Investigación y Desarrollo",
    color_name="violet-70",
)

colored_header(
    label="3. Alianza Operativa",
    description="Co Crear Sistemas de Mitigación y Adaptación",
    color_name="violet-70",
)
