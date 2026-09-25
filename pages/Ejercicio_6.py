#IMPORTACIONES 
import streamlit as st
import matplotlib.pyplot as plt
from utils.math_utils import SimularMaximaVerosimilitud

# Variables utilizadas en el ejercicio 6
n = 100
theta_real = 2.0
M = 5000
seed = 42

resultados_simulacion = SimularMaximaVerosimilitud(n, theta_real, M, seed)

st.title(" Simulación y Estimación por Máxima Verosimilitud")

st.write("""Teniendo en cuenta la siguiente densidad""" )

st.latex(r"""f(x;\theta) = (1+\theta)x^\theta, \quad 0 \le x \le 1, \quad \theta > -1""")

st.write(r"""Se utilizara el método de transformación inversa para generar observaciones 
    de esta distribución. Si $U \sim \text{Uniform}(0,1)$, entonces $X = U^{\frac{1}{1+\theta}}$.""")

st.write(r"""Consideraremos $n = 100$ y $\theta = 2$. Generando una muestra aleatoria de tamaño $n$.""")

st.write("""Utilizando el estimador:""")

st.latex(r"""\hat{\theta}_{MV} = -\frac{n}{\sum_{i=1}^{n} \ln(X_i)} - 1""")

st.subheader("Código para la simulación y estimación")

codigo = """
    import numpy as np
    import pandas as pd

    # Parámetros del experimento
    np.random.seed(42)
    n = 100
    theta_real = 2.0
    M = 5000

    # 1. Generación de datos mediante transformación inversa
    # X = U^(1 / (1 + theta))
    U = np.random.uniform(0, 1, size=(M, n))
    X = U ** (1.0 / (1.0 + theta_real))

    # 2. Cálculo del Estimador de Máxima Verosimilitud (EMV) para cada una de las M muestras
    # theta_hat_mv = -n / sum(ln(X_i)) - 1
    suma_ln_x = np.sum(np.log(X), axis=1)
    theta_mv = -n / suma_ln_x - 1.0

    # 3. Estudio del punto 3: Probabilidad empírica de que |X_bar - E[X]| > 0.5
    E_X = (theta_real + 1.0) / (theta_real + 2.0)  # Debería ser 0.75 para theta = 2
    x_bar_muestras = np.mean(X, axis=1)
    desviaciones = np.abs(x_bar_muestras - E_X)
    probabilidad_empirica = np.mean(desviaciones > 0.5)
"""
st.code(codigo, language='python')

st.subheader("Resultados Numéricos Clave")
col1, col2, col3 = st.columns(3)
col1.metric("Media Empírica ($\\hat{\\theta}_{MV}$)", f"{resultados_simulacion['media_theta_mv']:.4f}")
col2.metric("Esperanza Teórica $\\mathbb{E}[X]$", f"{resultados_simulacion['E_X_teorico']:.4f}")
col3.metric("Probabilidad Empírica", f"{resultados_simulacion['probabilidad_empirica']:.4f}")

st.write(f"**Desviación estándar empírica de los EMV:** {resultados_simulacion['desviacion_theta_mv']:.4f}")

st.subheader("Distribución Empírica del Estimador de Máxima Verosimilitud")

# 2. Creación del gráfico con fondo transparente correcto
fig, ax = plt.subplots(figsize=(8, 4))

# Configurar fondos transparentes para que hereden el color de Streamlit
fig.patch.set_facecolor('none')
ax.patch.set_facecolor('none')

# Generar el histograma y la línea de referencia
ax.hist(resultados_simulacion["theta_mv"], bins=50, density=True, alpha=0.6, color='#bf00ff', edgecolor='white')
ax.axvline(resultados_simulacion["theta_real"], color='red', linestyle='--', linewidth=2, label=f'Valor Real $\\theta$ = {resultados_simulacion["theta_real"]}')

color_texto = 'white'

ax.set_title(f"Distribución Empírica de $\\hat{{\\theta}}_{{MV}}$ ($M = {M}$, $n = {n}$)", color=color_texto)
ax.set_xlabel("Valores de $\\hat{\\theta}_{MV}$", color=color_texto)
ax.set_ylabel("Densidad", color=color_texto)
ax.tick_params(axis='x', colors=color_texto)
ax.tick_params(axis='y', colors=color_texto)
for spine in ax.spines.values():
    spine.set_color(color_texto)
legend = ax.legend()
for text in legend.get_texts():
    text.set_color("black") # Texto oscuro dentro de la leyenda para que contraste con su fondo blanco

# NOTA: Se eliminaron las líneas con 'auto' que causaban el ValueError.
# Al dejar los ejes limpios sin forzar colores, Streamlit maneja la visibilidad de forma fluida.

# Renderizar en la aplicación con transparencia habilitada
st.pyplot(fig, transparent=True)

st.write(r"""El método de transformación inversa permite generar datos aleatorios de una 
    distribución continua a partir de una variable uniforme $U(0,1)$ igualando la 
    función de distribución acumulada ($F(x)$) a $U$. Para esta función de densidad, 
    al integrar se obtiene $F(x) = x^{\theta+1}$, y despejando $X$ se llega a la 
    expresión de generación $X = U^{\frac{1}{1+\theta}}$.""")

st.write(r"""De acuerdo con la teoría de Inferencia Estadística y el 
    Teorema Central del Límite (TCL), los Estimadores de Máxima Verosimilitud 
    poseen propiedades deseables en muestras grandes ($n = 100$), tales como 
    ser asintóticamente insesgados y asintóticamente normales. Por lo tanto, 
    la distribución empírica de $\hat{\theta}_{MV}$ tras $M = 5\,000$ 
    simulaciones tiende a adoptar una forma acampanada de tipo normal en 
    torno al valor verdadero $\theta = 2$.""")

st.write(r"""Al evaluar el comportamiento de la media muestral $\overline{X}$ 
    frente a su valor esperado teórico ($\mathbb{E}[X] = 0.75$), el cálculo 
    de la probabilidad empírica arroja qué tan frecuentes son las desviaciones 
    extremas mayores a $0.5$ en las muestras simuladas.""")
