# IMPORTACIONES 
import streamlit as st 
from utils.math_utils import SimularTeoremaRaoBlackwell

# mostrar codigo en pantalla 
st.title("Teorema de Rao–Blackwell")

st.write(r"""Considere la distribución geométrica con función de probabilidad:""")

st.latex(r"""f(x; \theta) = (1 - p)^{x-1} p, \quad x = 1, 2, 3, \ldots.""")

st.write(r"""Considere los siguientes estimadores:""")

st.write(r"""Estimador inicial: $\hat{\theta}_1 = X_1$.""")

st.write(r"""Estadístico suficiente: $U = \sum_{i=1}^{n} X_i$.""")

st.write(r"""Estimador mejorado: $\hat{\theta}_2 = \frac{1}{n} \sum_{i=1}^{n} X_i$.""")

st.subheader("Código en Python para la Simulación")

codigo = """
    import numpy as np
    import pandas as pd
    import streamlit as st

    # Configuración inicial del experimento
    np.random.seed(42)
    theta = 4.0
    p = 1.0 / theta
    n = 20
    M = 10000

    # 1. Generar M = 10,000 muestras de tamaño n = 20 de una distribución geométrica
    muestras = np.random.geometric(p=p, size=(M, n))

    # 2. Estimador inicial: X_1 (primer elemento de cada muestra)
    theta_1 = muestras[:, 0]

    # 3. Estadístico suficiente U = suma de los elementos de cada muestra
    U = np.sum(muestras, axis=1)

    # 4. Estimador mejorado por Rao-Blackwell: E(X_1 | U) = U / n = X_bar
    theta_star = U / n

    # 5. Cálculo de las varianzas empíricas
    var_theta_1 = np.var(theta_1, ddof=1)
    var_theta_star = np.var(theta_star, ddof=1)
    reduccion_porcentual = ((var_theta_1 - var_theta_star) / var_theta_1) * 100

    # Mostrar resultados en tabla dentro de Streamlit
    st.title("Resultados del Teorema de Rao–Blackwell (Ejercicio 5)")

    data_e5 = {
        "Estimador": ["Estimador Inicial (X₁)", "Estimador Mejorado (Rao-Blackwell)"],
        "Expresión": ["\\hat{\\theta}_1 = X_1", "\\hat{\\theta}^* = \\overline{X} = \\frac{U}{n}"],
        "Varianza Empírica": [f"{var_theta_1:.4f}", f"{var_theta_star:.4f}"],
        "Eficiencia": ["Baja eficiencia (usa 1 dato)", f"Alta eficiencia (reducción del {reduccion_porcentual:.1f}%)"]
    }

    df_e5 = pd.DataFrame(data_e5)
    st.dataframe(df_e5, use_container_width=True)
"""

st.code(codigo, language='python')

st.subheader("Propósito del Teorema de Rao–Blackwell:")

st.write(r"""Este teorema establece que si se tiene un estimador insesgado para 
    un parámetro y se le condiciona respecto a un estadístico suficiente ($U$), 
    el nuevo estimador resultante no solo sigue siendo insesgado, sino que garantiza 
    una varianza menor o igual que la del estimador original ($\text{Var}(\hat{\theta}^*) 
    \le \text{Var}(\hat{\theta}_1)$).""")

st.write(r"""El estimador inicial $\hat{\theta}_1 = X_1$ utiliza únicamente la primera observación 
    de la muestra, desperdiciando la información del resto de los datos, lo que genera una 
    dispersión (varianza) muy alta.""")

st.write(r"""Al aplicar la esperanza condicional dado el estadístico suficiente $U = \sum X_i$, se 
    obtiene la media muestral $\overline{X}$, la cual aprovecha toda la información contenida en 
    la muestra.""")

tabla_de_resultados = SimularTeoremaRaoBlackwell(theta=4.0, n=20, M=10000, seed=42)

st.subheader("Resultados de la Simulación")

st.table(tabla_de_resultados)

st.subheader("Conclusión sobre la Mejora Obtenida")

st.write(r"""La simulación demuestra de manera contundente que la varianza empírica de la media muestral 
    ($\text{Var}(\overline{X}) \approx 0.5956$) es significativamente menor que la varianza del estimador 
    inicial ($\text{Var}(X_1) \approx 11.9141$). Esto representa una reducción de la varianza del 95%, 
    comprobando empíricamente el Teorema de Rao–Blackwell.""")
