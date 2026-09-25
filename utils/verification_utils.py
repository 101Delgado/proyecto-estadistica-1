# IMPORTACIONES
import importlib

def verificar_instalacion(libreria):
    """Comprueba si una librería está instalada."""
    spec = importlib.util.find_spec(libreria)
    return spec is not None
