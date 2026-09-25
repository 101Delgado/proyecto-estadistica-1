# 📊 Proyecto de Estadística 1 - UCV 2026

**Proyecto para la asignatura de Estadística - Universidad Central de Venezuela**

## 📋 Descripción del Proyecto
Este repositorio contiene el desarrollo del proyecto de estadística evaluado mediante una aplicación web interactiva construida con **Streamlit**. El proyecto aborda la resolución de seis ejercicios prácticos de análisis de datos, utilizando un set de datos de temperaturas (`temperaturas.txt`).

Además de la aplicación interactiva, en la carpeta `resources/` se encuentra el documento analítico formal (`informe.pdf`) con el sustento teórico y las conclusiones de los análisis realizados.

## 🗂 Estructura del Proyecto

El repositorio está organizado de la siguiente manera para separar la lógica, los datos y la presentación:

```text
ProyectoEstadistica1/
├── data/                   # Contiene los conjuntos de datos analizados
│   └── temperaturas.txt    # Dataset principal del proyecto
├── pages/                  # Páginas secundarias de la app en Streamlit
│   ├── Ejercicio_1.py      # Desarrollo del Ejercicio 1
│   ├── Ejercicio_2.py      # Desarrollo del Ejercicio 2
│   ├── Ejercicio_3.py      # Desarrollo del Ejercicio 3
│   ├── Ejercicio_4.py      # Desarrollo del Ejercicio 4
│   ├── Ejercicio_5.py      # Desarrollo del Ejercicio 5
│   └── Ejercicio_6.py      # Desarrollo del Ejercicio 6
├── resources/              # Documentos y recursos adicionales
│   └── informe.pdf         # Memoria formal del proyecto (Entrega oficial)
├── utils/                  # Módulos de soporte con lógica matemática y validaciones
│   ├── __init__.py
│   ├── math_utils.py       # Funciones matemáticas personalizadas
│   └── verification_utils.py # Funciones de verificación de datos
├── .gitignore              # Archivos y directorios ignorados por Git
├── Inicio.py               # Archivo principal y punto de entrada de la aplicación web
└── requirements.txt        # Lista de dependencias necesarias (Streamlit, Pandas, etc.)
```

## 🚀 Cómo ejecutar este proyecto localmente

Para visualizar la aplicación y los resultados de los ejercicios en tu propia computadora, sigue estos pasos:

1. **Clona el repositorio:**
   ```bash
   git clone [URL_DE_TU_REPOSITORIO]
   cd ProyectoEstadistica1
   ```

2. **Instala las dependencias necesarias:**
   Se recomienda usar un entorno virtual. Luego, instala los paquetes requeridos:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación de Streamlit:**
   Desde la raíz del proyecto, corre el archivo principal:
   ```bash
   streamlit run Inicio.py
   ```
   *Esto abrirá automáticamente una pestaña en tu navegador web por defecto (usualmente en `http://localhost:8501`).*

## 🛠 Tecnologías y Herramientas
* **Lenguaje:** Python 3.x
* **Framework Web:** Streamlit
* **Manejo y Análisis de Datos:** (Ej. Pandas, NumPy - *ver `requirements.txt`*)