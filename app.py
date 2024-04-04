import streamlit as st
import pandas as pd
import plotly_express as px

'''
# EDA - Vehicle dataset
'''

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

'''
### Dataset
'''
st.dataframe(car_data)

##
st.divider()
##

# definir las variables continuas
continuous_variables = ['price', 'odometer']

# crear los checkbox's
hist_chb = st.checkbox('Construir histograma')
scatter_chb = st.checkbox('Construir diagrama de dispersion')

if hist_chb: # al hacer clic en el botón
    st.divider()
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # seleccionar una columna a graficar
    option = st.selectbox(
        'Elige el valor a graficar',
        continuous_variables
    )
    
    # crear un histograma
    fig = px.histogram(car_data, x=option)

    # mostrar un gráfico
    st.plotly_chart(fig, use_container_width=True)

if scatter_chb: # al hacer clic en el botón
    st.divider()
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico
    st.plotly_chart(fig, use_container_width=True)