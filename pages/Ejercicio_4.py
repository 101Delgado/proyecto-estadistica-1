# IMPORTACIONES 
import streamlit as st

# mostrar codigo en pantalla 
st.title("Cramér–Rao")

st.subheader("Codigo para calcular el sesgo y la varianza empírica")

codigo = """
    import numpy as np

    # Configuración inicial del experimento
    np.random.seed(42)  # Para reproducibilidad
    theta = 4.0
    p = 1.0 / theta
    n = 30
    M = 10000

    # 1. Simulación de M = 10,000 muestras de tamaño n = 30 de una distribución geométrica
    # Nota: np.random.geometric usa p como parámetro de éxito.
    muestras = np.random.geometric(p=p, size=(M, n))

    # 2. Calcular la media muestral X_bar para cada una de las M muestras
    x_bar = np.mean(muestras, axis=1)
    theta_hat = x_bar

    # 3. Estimar el sesgo de theta_hat
    esperanza_estimador = np.mean(theta_hat)
    sesgo = esperanza_estimador - theta

    # 4. Calcular la varianza empírica del estimador
    varianza_empirica = np.var(theta_hat, ddof=1)

    # 5. Calcular el límite teórico de Cramér-Rao: [theta * (theta - 1)] / n
    cramer_rao_bound = (theta * (theta - 1)) / n
"""

st.code(codigo, language='python')

st.subheader("Resultados de la Simulación")

# Tabla en Markdown usando st.markdown
tabla_markdown = """
| Variable o Métrica | Símbolo / Expresión | Valor Obtenido / Teórico | Descripción e Interpretación |
| :--- | :---: | :---: | :--- |
| **Parámetro Real** | $\\theta$ | $4.0000$ | Valor fijo establecido para el parámetro poblacional de interés. |
| **Parámetro de Éxito** | $p = \\frac{1}{\\theta}$ | $0.2500$ | Probabilidad de éxito asociada a la distribución geométrica simulada. |
| **Número de Muestras** | $M$ | $10\\,000$ | Cantidad de repeticiones de la simulación de Monte Carlo. |
| **Tamaño de Muestra** | $n$ | $30$ | Número de observaciones aleatorias extraídas en cada muestra. |
| **Media Teórica Esperada** | $\\mathbb{E}(X)$ | $4.0000$ | Valor esperado teórico de la media de una variable geométrica con $\\theta = 4$. |
| **Media Empírica (Estimador)** | $\\mathbb{E}(\\hat{\\theta}) = \\overline{X}$ | $4.0037$ | Promedio de las medias muestrales obtenidas a través de las $10\\,000$ simulaciones. |
| **Sesgo Estimado** | $\\text{Sesgo}(\\hat{\\theta})$ | $0.0037$ | Diferencia entre la media empírica y el valor real de $\\theta$. Al ser cercano a cero, confirma que $\\overline{X}$ es un estimador **insesgado**. |
"""

st.markdown(tabla_markdown)

st.write(r"""Consideramos una variable aleatoria $X$ con distribución geométrica 
    cuyo parámetro es $p = \frac{1}{\theta}$. Para esta distribución, la esperanza 
    matemática es:""")

st.latex(r'''
    E[X] = \frac{1}{p} = \theta''')

st.write(r"""Por lo tanto, la media muestral $\overline{X}$ es un estimador insesgado 
    de $\theta$, ya que $\mathbb{E}(\overline{X}) = \theta$.""")

st.subheader("Estimacion del sesgo")

st.write(r"""El sesgo de un estimador $\hat{\theta} = \overline{X}$ se define como:""")

st.latex(r'''
    \text{Sesgo}(\hat{\theta}) = \mathbb{E}(\hat{\theta}) - \theta''')

st.write(r"""Dado que $\hat{\theta}$ es insesgado teóricamente, el sesgo esperado es 0. 
    En los resultados de la simulación con $M = 10\,000$ muestras, el sesgo empírico 
    obtenido es un valor sumamente pequeño cercano a $0.0036$, lo cual confirma de forma 
    empírica la propiedad de insesgado del estimador.""")

st.subheader("Varianza Empírica vs. Límite de Cramér–Rao")

st.write(r"""Varianza empírica obtenida en la simulación $\approx 0.4079$""")

st.write("""Límite inferior de Cramér–Rao teórico:""")

st.latex(r'''\text{LCR} = \frac{\theta(\theta - 1)}{n} = \frac{4(4 - 1)}{30} = \frac{12}{30} = 0.40''')

st.write(r"""Como la varianza empírica del estimador ($\approx 0.4079$) es prácticamente igual al límite
     inferior de Cramér–Rao ($0.40$), se concluye que la media muestral $\overline{X}$ es un estimador 
     eficiente (o alcanza la cota de eficiencia de Cramér–Rao) para el parámetro $\theta$ de la distribución 
     geométrica bajo las condiciones del tamaño de muestra evaluado.""")
