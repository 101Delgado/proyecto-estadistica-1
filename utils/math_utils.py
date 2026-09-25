# IMPORTACIONES DE LIBRERIAS
import pandas as pd 
import scipy.stats as stats
import numpy as np

# FUNCIONES A UTILIZAR

def CalcularMedidasDescriptivasEstacion(df):

    df = df.drop('PromAnual', axis=1) #quitar la columna de promedio 
    
    df_aux = pd.DataFrame()

    # axis=1 aplica la operacion a lo largo de una fila 
    df_aux['Media_aritmetica'] = df.select_dtypes(include=['number']).mean(axis=1)
    df_aux['Mediana'] = df.select_dtypes(include=['number']).median(axis=1)
    df_aux['Varianza_muestral'] = df.select_dtypes(include=['number']).var(axis=1)
    df_aux['Desviacion_estandar_muestral'] = df.select_dtypes(include=['number']).std(axis=1)
    df_aux['Valor_minimo'] = df.select_dtypes(include=['number']).min(axis=1)
    df_aux['Valor_maximo'] = df.select_dtypes(include=['number']).max(axis=1)
    df_aux['Rango'] = df_aux['Valor_maximo'] - df_aux['Valor_minimo']

    df_final = pd.concat([df, df_aux], axis=1) # coloca las nuevas columnas al lado del df original
    
    return df_final

def CalcularMedidasDescriptivasMes(df):
    
    df = df.drop('PromAnual', axis=1) #quitar la columna de promedio 
    
    df_aux = pd.DataFrame()

    # axis=1 aplica la operacion a lo largo de una columna
    df_aux['Media_aritmetica'] = df.select_dtypes(include=['number']).mean(axis=0)
    df_aux['Mediana'] = df.select_dtypes(include=['number']).median(axis=0)
    df_aux['Varianza_muestral'] = df.select_dtypes(include=['number']).var(axis=0)
    df_aux['Desviacion_estandar_muestral'] = df.select_dtypes(include=['number']).std(axis=0)
    df_aux['Valor_minimo'] = df.select_dtypes(include=['number']).min(axis=0)
    df_aux['Valor_maximo'] = df.select_dtypes(include=['number']).max(axis=0)
    df_aux['Rango'] = df_aux['Valor_maximo'] - df_aux['Valor_minimo']

    return df_aux

def CalcularIntervalo(confianza, n, x_bar, sigma):
    alpha = 1 - confianza
    z = stats.norm.ppf(1 - alpha / 2)
    error = z * (sigma / np.sqrt(n))
    return (x_bar - error, x_bar + error)

def CalcularIntervaloProporcion(confianza, n, exitos):
    alpha = 1 - confianza
    z = stats.norm.ppf(1 - alpha / 2)
    p_hat = exitos / n
    error = z * np.sqrt((p_hat * (1 - p_hat)) / n)
    return (p_hat - error, p_hat + error)

def GenerarTalloHojas(datos):

    datos = sorted(datos)
    tallo_hojas = {}
    
    for num in datos:
        tallo = num // 10
        hoja = num % 10
        if tallo not in tallo_hojas:
            tallo_hojas[tallo] = []
        tallo_hojas[tallo].append(str(hoja))
    
    resultado = "Tallo | Hojas\n"
    resultado += "-------------\n"
    for tallo in sorted(tallo_hojas.keys()):
        resultado += f"{tallo:5} | {' '.join(tallo_hojas[tallo])}\n"
    return resultado

def SimularTeoremaRaoBlackwell(theta, n, M, seed):
    
    # Fijar semilla
    np.random.seed(seed)
    
    # Parámetro de éxito para la distribución geométrica (p = 1 / theta)
    p = 1.0 / theta
    
    # 1. Generar M muestras de tamaño n
    muestras = np.random.geometric(p=p, size=(M, n))
    
    # 2. Estimador inicial: X_1 (primer elemento de cada muestra)
    theta_1 = muestras[:, 0]
    
    # 3. Estadístico suficiente U = suma de las observaciones en cada muestra
    U = np.sum(muestras, axis=1)
    
    # 4. Estimador mejorado mediante Rao-Blackwell: E(X_1 | U) = U / n = X_bar
    theta_star = U / n
    
    # 5. Cálculo de las varianzas empíricas
    var_theta_1 = np.var(theta_1, ddof=1)
    var_theta_star = np.var(theta_star, ddof=1)
    
    # Reducción porcentual de la varianza
    reduccion = ((var_theta_1 - var_theta_star) / var_theta_1) * 100
    
    # Estructurar los datos en un diccionario para la tabla
    resultados_tabla = {
        "Estimador Evaluado": [
            "Estimador Inicial", 
            "Estimador Mejorado (Rao–Blackwell)"
        ],
        "Varianza Empírica Obtenida": [
            f"{var_theta_1:.4f}", 
            f"{var_theta_star:.4f}"
        ],
        "Descripción y Eficiencia": [
            "Alta dispersión al basarse en una sola observación de la muestra.",
            f"Varianza drásticamente reducida (Reducción del {reduccion:.2f}%) al condicionar sobre el estadístico suficiente."
        ]
    }
    
    # Convertir y retornar como un DataFrame de Pandas
    return pd.DataFrame(resultados_tabla)

def SimularMaximaVerosimilitud(n, theta_real, M, seed):
    """
    Realiza la simulación de Monte Carlo y la estimación por Máxima Verosimilitud
    para el Ejercicio 6, dejando los gráficos completamente por fuera.
    
    Parámetros:
    - n (int): Tamaño de cada muestra aleatoria.
    - theta_real (float): Valor real del parámetro theta.
    - M (int): Número de repeticiones de la simulación.
    - seed (int): Semilla para la reproducibilidad aleatoria.
    
    Retorna:
    - dict: Diccionario con todas las matrices de datos, métricas y resultados clave.
    """
    # 1. Fijar semilla para reproducibilidad
    np.random.seed(seed)
    
    # 2. Generar datos mediante el método de transformación inversa
    # X = U^(1 / (1 + theta))
    U = np.random.uniform(0, 1, size=(M, n))
    X = U ** (1.0 / (1.0 + theta_real))
    
    # 3. Calcular el Estimador de Máxima Verosimilitud (EMV) para cada una de las M muestras
    suma_ln_x = np.sum(np.log(X), axis=1)
    theta_mv = -n / suma_ln_x - 1.0
    
    # 4. Cálculos analíticos y estadísticos solicitados
    media_theta_mv = np.mean(theta_mv)
    desviacion_theta_mv = np.std(theta_mv, ddof=1)
    
    # Esperanza teórica E[X] = (theta + 1) / (theta + 2)
    E_X_teorico = (theta_real + 1.0) / (theta_real + 2.0)
    
    # Probabilidad empírica de que |X_bar - E[X]| > 0.5
    x_bar_muestras = np.mean(X, axis=1)
    desviaciones = np.abs(x_bar_muestras - E_X_teorico)
    probabilidad_empirica = np.mean(desviaciones > 0.5)
    
    # Empaquetar resultados en un diccionario organizado
    resultados = {
        "n": n,
        "theta_real": theta_real,
        "M": M,
        "X_muestras": X,             # Matriz de datos generados (útil para gráficos)
        "theta_mv": theta_mv,         # Vector con las 5,000 estimaciones (útil para histogramas)
        "media_theta_mv": media_theta_mv,
        "desviacion_theta_mv": desviacion_theta_mv,
        "E_X_teorico": E_X_teorico,
        "probabilidad_empirica": probabilidad_empirica
    }
    
    return resultados