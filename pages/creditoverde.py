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

#import folium
#from streamlit_folium import st_folium

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Clima", page_icon="⛅")

st.title('Novus Clima ⛅ Tech for save the Planet 🌎')

st.markdown(
  """
  En esta web encontrarás:
  - 🌧️ _    Diagnóstico de tus riesgos climáticos y de transición energética
  - 💰 _    Plan de Crédito Verde requerido para Transición Energética-Climática a neutralidad en 2050
  - ✍️ _     Contrato Inteligente de Seguros Climáticos con Planes de Mitigación y Adaptación
    
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """)

st.header("¿Sabes cuánto te costaría la próxima crisis climática en tu zona?🌎")
#st.write("Selecciona una zona en el mapa y averígualo ahora 🕰")


territorio = st.selectbox("Indica el Territorio",
        ("Santander", "Tolima", "Caribe", "Pacífico", "Amazonas"),
    )

invertido = st.slider('¿Cuántos millones tienes invertido?', 0, 300000)

categoria = st.radio(
        "Indica el periodo de análisis👇 ",
        options=['2023', '2030','2040', '2050', '2060'],
    )

st.slider('En kilovatios hora (Kwh): ¿cuál es tu consumo energético mensual?', 0, 100000, key="consumo")

st.slider('En millones de pesos al año: ¿cuánto inviertes en energía?', 0, 1000000, key="presupuesto")

st.radio('¿Cuál es tu fuente principal de energia?', ['Agua', 'Carbon', 'Combustible', 'Termoelectrica', 'Solar', 'Viento'], key="fuente")


if st.button('Calcular diagnóstico gratuito'):
    st.header("Diagnóstico de Riesgos Climáticos + Transición Energética")
    st.write("Probabilidades de ocurrencia en el periodo ", categoria)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Derrumbes", "70%", "40%")
    col2.metric("Sequías", "30%", "-82%")
    col3.metric("Incedios", "16%", "43%")
    col4.metric("Inundaciones", "87%", "78%")
    st.write("Georreferenciación de riesgos climáticos")
    #datos
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [4.2620, -75.13],
    columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=4.26,
        longitude=-75.13,
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
    st.header("Mitigación requerida")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Movimiento de Tierras", "Motobombas", "Escombros"])
    st.area_chart(chart_data)
    st.write("Financiación necesaria en Crédito Verde")
        # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['3 meses antes del evento', 'Post evento', '3 meses después del evento']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    st.header("Plan de Adaptación por zonas")
    chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["emisiones", "flora", "fauna"])
    st.bar_chart(chart_data)

    def render_basic_radar():
        option = {
                "title": {"text": "Transición energética"},
                "legend": {"data": ["Consumo Actual", "Consumo Óptimo"]},
                "radar": {
                    "indicator": [
                        {"name": "Carbón", "max": 6500},
                        {"name": "Agua", "max": 16000},
                        {"name": "Viento", "max": 30000},
                        {"name": "Sol", "max": 38000},
                        {"name": "Petróleo", "max": 52000},
                        {"name": "Gas", "max": 25000},
                    ]
                },
                "series": [
                    {
                        "name": "Consumo Actual Vs Óptimo",
                        "type": "radar",
                        "data": [
                            {
                                "value": [6000, 10000, 20000, 3500, 15000, 11800],
                                "name": "Consumo Actual",
                            },
                            {
                                "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                "name": "Consumo Óptimo",
                            },
                        ],
                    }
                ],
            }
        st_echarts(option, height="500px")
    render_basic_radar()
# Data src:  https://www.kaggle.com/manohar676/hotel-reviews-segmentation-recommended-system
# Credit to: Manohar Reddy
    df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Plotly_Graphs/Radar-chart/ExistingHotels_CustomerVisitsdata-1554810038262.csv")
    df = df[df['Hotelid'].isin(['hotel_101','hotel_102','hotel_103'])]
    print(df.iloc[:20, :8])

    df = df.groupby('Hotelid')[['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                    'Rooms_rating','Checkin_rating',
                                    'Businessservice_rating']].mean().reset_index()
    print(df)

# Convert from wide data to long data to plot radar chart
    df = pd.melt(df, id_vars=['Hotelid'], var_name='category', value_name='rating',
                     value_vars=['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                 'Rooms_rating','Checkin_rating','Businessservice_rating'],
        )
    print(df)

# radar chart Plotly examples - https://plotly.com/python/radar-chart/
# radar chart Plotly docs = https://plotly.com/python-api-reference/generated/plotly.express.line_polar.html#plotly.express.line_polar
    fig = px.line_polar(df, r='rating', theta='category', color='Hotelid', line_close=True,
                                    line_shape='linear',  # or spline
                            hover_name='Hotelid',
                            hover_data={'Hotelid':False},
                            markers=True,
                            # labels={'rating':'stars'},
                            # text='Hotelid',
                            # range_r=[0,10],
                            direction='clockwise',  # or counterclockwise
                            start_angle=45
                            )
        # fig.update_traces(fill='toself')
    fig.show()
    
    @st.experimental_memo
    def get_chart_25713448():
        url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
    
        # override gray link colors with 'source' colors
        opacity = 0.4
        # change 'magenta' to its 'rgba' value to add opacity
        data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
        data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                            for src in data['data'][0]['link']['source']]
    
        fig = go.Figure(data=[go.Sankey(
            valueformat = ".0f",
            valuesuffix = "TWh",
            # Define nodes
            node = dict(
              pad = 15,
              thickness = 15,
              line = dict(color = "black", width = 0.5),
              label =  data['data'][0]['node']['label'],
              color =  data['data'][0]['node']['color']
            ),
            # Add links
            link = dict(
              source =  data['data'][0]['link']['source'],
              target =  data['data'][0]['link']['target'],
              value =  data['data'][0]['link']['value'],
              label =  data['data'][0]['link']['label'],
              color =  data['data'][0]['link']['color']
        ))])
    
        fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                          font_size=10)
    
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit")
        with tab2:
            st.plotly_chart(fig, theme=None)


st.write("""
**No asumas estos riesgos sin estar blindado**
- Financia tu Transición Climática y Asegúrate en el camino con `Novus Clima`
""")
st.write('---')

if st.button('Activa tu Plan anual de Transición Climática'):    
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
