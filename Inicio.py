# IMPORTACIONES 
import pandas as pd 
import streamlit as st
import os
import utils.verification_utils as vu

st.set_page_config(page_title="Inicio", layout="wide")

st.title("Proyecto de Estadística 1")

# Lista de librerías necesarias 
librerias_req= [
    "pandas",
    "streamlit",
    "plotly",
    "scipy",
    "numpy"
]

st.subheader("Librerías necesarias")

# Crear una tabla 
for lib in librerias_req:
    if vu.verificar_instalacion(lib):
        st.success(f"✅ **{lib}** está instalada")
    else:
        st.error(f"❌ **{lib}** no encontrada")
        st.caption(f"Ejecuta: `pip install {lib}` o ejecute el el archivo install.bat para instalarla")

# Botón para refrescar
if st.button("Verificar de nuevo"):
    st.rerun()

st.subheader("Carga de datos para el funcionamiento del proyecto")

# El componente file_uploader
archivo_cargado = st.file_uploader("Suba el archivo temperaturas.txt", type=['txt'])

if archivo_cargado is not None:
    # Leemos el archivo y lo guardamos en el session_state
    df = pd.read_csv(archivo_cargado, sep='\s+')
    st.session_state['datos_cargados'] = df
    st.success("Archivo cargado y guardado en memoria.")

st.subheader("Descarga de informe técnico")

# Define la ruta de tu archivo PDF guardado (ajusta la ruta según tu estructura de carpetas)
ruta_pdf = "resources/informe.pdf"

# Verificar si el archivo existe antes de mostrar el botón de descarga
if os.path.exists(ruta_pdf):
    # Abrir el archivo en modo lectura binaria ('rb')
    with open(ruta_pdf, "rb") as archivo_pdf:
        pdf_bytes = archivo_pdf.read()

    # Botón de descarga de Streamlit
    st.download_button(
        label="📄 Descargar Informe Técnico en PDF",
        data=pdf_bytes,
        file_name="Informe_Tecnico_Estadistica_UCV.pdf",
        mime="application/pdf",
        help="Haz clic para descargar el documento oficial del proyecto."
    )
else:
    st.error(f"⚠️ No se encontró el archivo PDF en la ruta especificada: `{ruta_pdf}`. Por favor, verifica que el archivo esté guardado correctamente.")