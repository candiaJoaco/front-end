import streamlit as st
import requests

API_URL = "https://<TU_URL_DE_CLOUD_RUN>/query"

st.title("Consulta de Productos")
message = st.text_input("Ingresa el producto:")

if st.button("Consultar"):
    response = requests.post(API_URL, json={"message": message})
    if response.status_code == 200:
        st.write(f"Respuesta: {response.json()['response']}")
    else:
        st.write("Error en la consulta.")
