# IMPORTACIONES 
import pandas as pd 
import streamlit as st
import plotly.express as px
import utils.math_utils as math_utils

# dataframes a mostrar 
if 'datos_cargados' in st.session_state:
    df_original = st.session_state['datos_cargados']
    st.write("Datos recibidos correctamente:")
    df_por_mes = math_utils.CalcularMedidasDescriptivasMes(df_original)
    df_por_estacion = math_utils.CalcularMedidasDescriptivasEstacion(df_original)

    tab1, tab2, tab3 = st.tabs(["PARTE 1", "PARTE 2", "PARTE 3"])

    with tab1:
        # PREGUNTA 1
        st.title("Parte 1")
        # parte 1.1
        st.write("Parte 1.1")
        st.dataframe(df_por_estacion, use_container_width=True)
        # parte 1.2
        st.write("Parte 1.2")
        st.dataframe(df_por_mes, use_container_width=True)
        st.write("""
                Los datos reflejan una variabilidad térmica estacional marcada. Por ejemplo, en Enero, 
                 la desviación estándar es de 15.78 °F 
                 (indicando una alta diferencia entre estaciones), 
                 mientras que en Julio esta se reduce a 7.48 °F, lo 
                 que sugiere que las temperaturas son relativamente 
                 más homogéneas entre las distintas estaciones durante 
                 los meses de verano.
        """)

    with tab2:
        # PREGUNTA 2
        st.title("Parte 2")
        # parte a
        st.write("parte 2.1")
        st.write("""
                El diagrama de caja de la variable PromAnual presenta 
                 una asimetría positiva (sesgo a la derecha). Esto se 
                 evidencia tanto por un coeficiente de asimetría de 
                 0.518 como por la ubicación de la mediana dentro de 
                 la caja, la cual se encuentra desplazada hacia los valores 
                 inferiores, mientras que el bigote y la caja superior se 
                 extienden más hacia temperaturas elevadas. Esto sugiere que 
                 existen algunas estaciones con temperaturas promedio anuales 
                 notablemente más altas que arrastran la media hacia la derecha, 
                 alejándola del centro de la distribución.
        """)
        fig_caja = px.box(df_original, y='PromAnual', title="Distribución de PromAnual")
        st.plotly_chart(fig_caja, use_container_width=True)
        # parte b
        st.write("parte 2.2")
        colores = []
        max_val = df_original['PromAnual'].max()
        min_val = df_original['PromAnual'].min()

        for val in df_original['PromAnual']:
            if val == max_val:
                colores.append('red')    # Color para el máximo
            elif val == min_val:
                colores.append('blue')   # Color para el mínimo
            else:
                colores.append('lightgray') # Color para los demás

        fig_barras = px.bar(
            df_original, 
            x='Estacion', 
            y='PromAnual', 
            title="Comparacion de promedios de temperaturas"
        )
        fig_barras.update_traces(marker_color=colores)
        st.plotly_chart(fig_barras, use_container_width=True)
        # parte c
        st.write("parte 2.3")

        col1, col2, col3 = st.columns([0.2, 7, 0.2])

        with col2:
            st.subheader("Diagrama de Tallo y Hojas")
            st.code(math_utils.GenerarTalloHojas(df_original['PromAnual'].tolist()), language=None)
        
        st.write("""
                El diagrama de tallo y hojas revela una concentración 
                 de temperaturas promedio anuales en el rango de 50 a 70 °F, 
                 con un tallo principal en 6 (60-69 °F) que contiene la 
                 mayoría de los datos. Además, se observa un tallo secundario 
                 en 5 (50-59 °F) con una menor cantidad de datos, y algunos 
                 valores atípicos en el tallo 7 (70-79 °F), lo que sugiere que 
                 hay algunas estaciones con temperaturas promedio anuales 
                 significativamente más altas que el resto.
        """)
        st.write("""
                En conjunto, el análisis de las medidas descriptivas, 
                 el diagrama de caja y el diagrama de tallo y hojas sugiere
                 que las temperaturas promedio anuales presentan una distribución 
                 asimétrica con una concentración en torno a los 60 °F, pero con 
                 algunos valores atípicos que elevan la media y generan un sesgo 
                 hacia la derecha.
        """)
        st.write("""
                 Los datos muestran una alta concentración entre los 
                 30 °F y los 50 °F. Por el contrario, los valores en las 
                 ramas de los 60 °F y 70 °F son escasos, representando casos 
                 particulares de estaciones con temperaturas promedio anuales 
                 superiores a la mayoría del conjunto.
        """)

    with tab3:
        # PREGUNTA 3
        st.title("Parte 3")
        st.subheader("Parte 3.1")
        st.write("""
                Al comparar la media (46.11 °F) con la mediana, 
                 se observa una proximidad que sugiere una distribución 
                 relativamente simétrica, aunque se recomienda verificar 
                 visualmente con el histograma para confirmar si existe un 
                 leve sesgo.
        """)

        st.subheader("Parte 3.2")
        st.latex(r"""
                Q_1 = 39.30 \quad ; \quad Q_3 = 51.65 \\
                RIC = Q_3 - Q_1 = 12.35 \\
                \text{Límite inferior: } Q_1 - 1.5 \times RIC = 20.77 \\
                \text{Límite superior: } Q_3 + 1.5 \times RIC = 70.18
        """)
        st.write("""
                Utilizando el criterio de Tukey, se establecieron los 
                 límites inferior y superior para identificar valores 
                 atípicos. El límite inferior calculado es 20.77 °F y el 
                 límite superior es 70.18 °F.
        """)
        st.write("""
                Al aplicar estos límites a la variable PromAnual, 
                 no se identificaron valores atípicos en el 
                 conjunto de datos, ya que todas las observaciones 
                 se encuentran dentro del rango delimitado. 
                 Por lo tanto, se puede afirmar que la distribución 
                 de las temperaturas promedio anuales es consistente 
                 y no presenta estaciones con valores climáticos extremos 
                 que distorsionen significativamente el comportamiento del 
                 conjunto analizado. 
        """)
        st.subheader("Parte 3.3")
        st.write("""
                Con una desviación estándar de 10.11 °F respecto 
                a una media de 46.11 °F, la variabilidad se considera 
                moderada-alta, lo que demuestra diferencias climáticas 
                significativas entre las estaciones analizadas.     
        """)
        st.subheader("Parte 3.4")
        st.write("""
                La estación con mayor temperatura promedio anual es Honolulu.🔥         
        """)
        st.subheader("Parte 3.5")
        st.write("""
                La estación con menor temperatura promedio anual es Duluth.❄️         
        """)
        st.subheader("Parte 3.6")
        st.write("""
                A partir del análisis descriptivo de las temperaturas, 
                 se concluye que las estaciones meteorológicas evaluadas 
                 presentan un comportamiento térmico heterogéneo a lo largo 
                 del año. Esta variabilidad queda de manifiesto al observar 
                 que las medidas de dispersión mensual, tales como la 
                 desviación estándar que alcanza valores significativos de 
                 hasta 15.78 °F en los meses de invierno, evidencian 
                 diferencias marcadas entre las distintas regiones 
                 geográficas. Si bien todas las estaciones siguen un 
                 ciclo estacional común, la magnitud de la fluctuación 
                 térmica entre el mes más cálido y el más frío varía 
                 sustancialmente de una estación a otra, demostrando que no 
                 existe un patrón climático uniforme en el conjunto de datos 
                 estudiado, sino una diversidad de regímenes térmicos que 
                 responden a las particularidades climáticas de cada ubicación.         
        """)
        st.subheader("Parte 3.7")
        st.write("""
                La estación meteorológica con la mayor variabilidad térmica anual es Minneapolis. Esta estación presenta 
                 la fluctuación de temperatura más extrema del conjunto 
                 de datos analizado. La combinación de un rango elevado 
                 60.3 °F y una desviación estándar mensual considerable 
                 21.13 °F confirma que Minneapolis experimenta variaciones 
                 térmicas drásticas entre las distintas épocas del año, lo 
                 cual es indicativo de un clima continental con veranos 
                 calurosos e inviernos muy fríos, situándola como la estación 
                 con mayor variabilidad térmica anual en comparación con el 
                 resto de las localizaciones estudiadas.     
        """)
else:   
    st.warning("No hay datos cargados. Por favor, vuelve a la página de inicio y carga el archivo teperaturas.txt.")
