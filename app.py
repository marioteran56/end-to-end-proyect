import streamlit as st
import pandas as pd
from prediction import predict
from combined_attributes_adder import CombinedAttributesAdder

st.title('Prediciendo el precio de una casa en California')
st.markdown('Se tienen multiples modelos entrenados para la predicción de precios de casas en California, elige el modelo que quieras utilizar para predecir el precio de una casa en California.')

st.header('Datos de la casa')
col1, col2 = st.columns(2)
with col1:
    longitude = st.number_input('Longitud', value=-122.23)
    latitude = st.number_input('Latitud', value=37.88)
    housing_median_age = st.number_input('Edad media de la vivienda', value=41)
    total_rooms = st.number_input('Total de habitaciones', value=880)
    total_bedrooms = st.number_input('Total de habitaciones', value=129)
with col2:
    population = st.number_input('Población', value=322)
    households = st.number_input('Casas', value=126)
    median_income = st.number_input('Ingreso medio', value=8.33)
    ocean_proximity = st.selectbox('Proximidad al océano', ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'], index=3)
    
st.header('Modelos')
model = st.selectbox('Modelo', ['Linear Regression', 'Random Forest Regressor', 'Decision Tree Regressor', 'Support Vector Regressor'])

if st.button('Predecir el precio de la casa'):
    data = pd.DataFrame({
            'longitude': [longitude],
            'latitude': [latitude],
            'housing_median_age': [housing_median_age],
            'total_rooms': [total_rooms],
            'total_bedrooms': [total_bedrooms],
            'population': [population],
            'households': [households],
            'median_income': [median_income],
            'ocean_proximity': [ocean_proximity]
        })
    if model == 'Linear Regression':
        result = predict(data, 'l_model.sav')
    elif model == 'Random Forest Regressor':
        result = predict(data, 'rf_model.sav')
    elif model == 'Decision Tree Regressor':
        result = predict(data, 'dt_model.sav')
    elif model == 'Support Vector Regressor':
        result = predict(data, 'sv_model.sav')
          
    st.text(f'El precio de la casa es de: ${result[0]}')

    
