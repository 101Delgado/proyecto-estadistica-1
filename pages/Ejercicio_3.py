# IMPORTACIONES 
import streamlit as st
from utils.math_utils import CalcularIntervaloProporcion

# Datos
n = 400
exitos = 280
confianza = 0.95

# mostrar codigo en pantalla 
st.title("Intervalos de confianza para una proporción poblacional")

st.write("Recordando la formula para el intervalo de confianza para una proporción poblacional:")
st.latex(r'''
    \hat{p} \pm Z_{\alpha/2} \cdot \frac{\sqrt{\hat{p}(1-\hat{p})}}{\sqrt{n}}
''')

st.subheader("Codigo para calcular el intervalo de confianza")

codigo = """
    import scipy.stats as stats
    import numpy as np

    # Datos
    n = 400
    exitos = 280
    confianza = 0.95

    # Proporción muestral
    p_hat = exitos / n

    # Intervalo de confianza
    z = stats.norm.ppf(1 - (1 - confianza) / 2)
    error = z * np.sqrt((p_hat * (1 - p_hat)) / n)
    intervalo = (p_hat - error, p_hat + error)
"""

st.code(codigo, language='python')

st.write("""Este codigo define la funcion `CalcularIntervaloProporcion` 
         dentro de la carpeta utils/math_utils.py, la cual se 
         importa al inicio de este archivo para ser utilizada 
         posteriormente.
""")

# Resultados
inter_1 = CalcularIntervaloProporcion(0.95, n, exitos)
inter_2 = CalcularIntervaloProporcion(0.95, n, exitos)

st.subheader("Interpretación de los resultados")
st.write(rf"""Tenemos una proporción poblacional de {exitos/n:.2f} ({exitos/n*100:.2f}%)
         y un nivel de confianza del 95% de que 
         la verdadera proporción poblacional de estudiantes 
         que utilizan herramientas de inteligencia artificial 
         está contenida en el intervalo de {inter_1[0]:.4f} a {inter_1[1]:.4f}.
""")
st.write(rf"""Dado que todo el intervalo de confianza 
         [{inter_1[0]:.4f}, {inter_1[1]:.4f}] se encuentra 
         por encima del valor 0.60 (60%), existe evidencia 
         estadística suficiente, con un nivel de confianza 
         del 95%, para concluir que la proporción de estudiantes 
         que utilizan herramientas de inteligencia artificial 
         es mayor al 60%.
""")

