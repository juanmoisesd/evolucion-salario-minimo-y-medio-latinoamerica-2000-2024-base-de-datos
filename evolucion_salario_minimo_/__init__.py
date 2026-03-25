"""Evolucion del Salario Minimo y Salario Medio en Latinoamerica 2000-2024 Base de Datos por País. DOI:
DOI: https://github.com/juanmoisesd/evolucion-salario-minimo-y-medio-latinoamerica-2000-2024-base-de-datos | GitHub: https://github.com/juanmoisesd/evolucion-salario-minimo-y-medio-latinoamerica-2000-2024-base-de-datos"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd,io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/evolucion-salario-minimo-y-medio-latinoamerica-2000-2024-base-de-datos".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs:raise ValueError("No CSV found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite():return f'de la Serna, Juan Moisés (2025). Evolucion del Salario Minimo y Salario Medio en Latinoamerica 2000-2024 Base de . Zenodo. https://github.com/juanmoisesd/evolucion-salario-minimo-y-medio-latinoamerica-2000-2024-base-de-datos'
def info():print(f"Dataset: Evolucion del Salario Minimo y Salario Medio en Latinoamerica 2000-2024 Base de \nDOI: https://github.com/juanmoisesd/evolucion-salario-minimo-y-medio-latinoamerica-2000-2024-base-de-datos\nGitHub: https://github.com/juanmoisesd/evolucion-salario-minimo-y-medio-latinoamerica-2000-2024-base-de-datos")