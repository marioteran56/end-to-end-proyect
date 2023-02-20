# Proyecto End-To-End para la Predicción del Precio de Casas en California

![House for sale image](https://monitor-media.s3.us-west-1.amazonaws.com/media/fotos/detalle/2021/05/26/aaa.jpg)

## Objetivo

El objetivo de este proyecto es entrenar una serie de modelos, como Linear Regressor, Decision Tree Regressor, Random Forest Regressor y Suport Vertor Regressor, cada uno con diferentes hiperparámetros para predecir el precio de las casas en California. Dichos modelos fueron entrenados con un dataset de 20.640 instancias y 9 atributos, indicando información como la población, la cantidad de habitaciones, la cantidad de habitaciones, etc. 

De esta manera, se crea un proyecto con Streamlit para que el usuario pueda ingresar los datos de su casa y el modelo le devuelva el precio estimado de la misma. Dicho proyecto se encuentra disponible en la siguiente liga de [Streamlit](https://marioteran56-end-to-end-proyect-app-c1xfmm.streamlit.app/)

## Requerimientos

El proyecto est disponible en la liga de [Streamlit](https://marioteran56-end-to-end-proyect-app-c1xfmm.streamlit.app/). No obstante, si se desea correr el proyecto en local, se requiere de los siguientes paquetes instalados dentro de nuestro entorno virtual:

- streamlit
- pandas
- numpy
- sklearn
- joblib

Por otro lado, si deseas reentrenar los modelos dentro de nuestro archivo de Jupyter Notebook, se requiere de los siguientes paquetes adicionales:

- matplotlib

## Uso

Para correr el proyecto de manera local, se debe abrir la terminal y dirigirse a la carpeta donde se encuentra el archivo `app.py`. Una vez ahí, se debe correr el siguiente comando:

```bash
streamlit run app.py
```
