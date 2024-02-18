import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Creación de gráficos de anuncios de venta de vehículos")

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada

    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer", color="condition")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter: # si la casilla de verificación está seleccionada

    #escribir un mensaje
    st.write("Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches")

    #crear un gráfico de dispersion
    fig_2 = px.scatter(car_data, x="model_year", y="price", color="type")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)    