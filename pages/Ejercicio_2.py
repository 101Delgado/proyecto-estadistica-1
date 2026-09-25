# IMPORTACIONES 
import streamlit as st
from utils.math_utils import CalcularIntervalo

# Datos
n = 64
x_bar = 42
sigma = 8

# mostrar codigo en pantalla 
st.title("Intervalos de confianza para la media poblacional")

st.write("Recordando la formula para el intervalo de confianza para la media poblacional con sigma conocido:")
st.latex(r'''
    \bar{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
''')

st.subheader("Codigo para calcular el intervalo de confianza")

codigo = """
    import scipy.stats as stats
    import numpy as np

    # Datos
    n = 64
    x_bar = 42
    sigma = 8

    # funcion para calcular el intervalo de confianza
    def CalcularIntervalo(confianza, n, x_bar, sigma):
        alpha = 1 - confianza
        z = stats.norm.ppf(1 - alpha / 2)
        error = z * (sigma / np.sqrt(n))
        return (x_bar - error, x_bar + error)
"""

st.code(codigo, language='python')

st.write("""Este codigo define la funcion `CalcularIntervalo` 
         dentro de la carpeta utils/math_utils.py, la cual se 
         importa al inicio de este archivo para ser utilizada 
         posteriormente.
""")

# Resultados
inter_1 = CalcularIntervalo(0.95, n, x_bar, sigma)
inter_2 = CalcularIntervalo(0.99, n, x_bar, sigma)

st.subheader("Interpretación de los resultados")
st.write(rf"""Existe un nivel de confianza del 95% de que el 
         verdadero tiempo medio poblacional de entrega de los 
         pedidos de la empresa se encuentra comprendido entre 
         {inter_1[0]:.2f} y {inter_1[1]:.2f} minutos. 
         Esto significa que, si repitiéramos el muestreo 
         muchas veces, el 95% de los intervalos calculados 
         contendrían el verdadero tiempo promedio de entrega.
""")

st.write(rf"""Al aumentar el nivel de confianza al 99%, 
         el valor crítico Z aumenta (pasa de 1.96 a a
         proximadamente 2.58). 
         Esto provoca que el margen de error también aumente, siendo el intervalo
         {inter_2[0]:.2f} y {inter_2[1]:.2f} minutos el correspondiente con el 99% de confianza.
""")

st.write(r"""El intervalo al 99% es más estrecho 
         que el del 95%. Esto es consistente con la 
         teoría estadística: para tener una mayor certeza 
         (99% frente al 95%) de que el parámetro poblacional 
         se encuentra dentro de nuestro intervalo, necesitamos 
         abarcar un rango de valores mayor, sacrificando precisión 
         por una mayor seguridad.
""")