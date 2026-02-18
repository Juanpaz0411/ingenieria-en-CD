import requests
import pandas as pd
from pathlib import Path

# URL ejemplo NASA exoplanets (puede cambiar según tu profe)
URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps&format=csv"

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True)

def download_data():
    print("Descargando datos...")

    response = requests.get(URL)
    response.raise_for_status()

    file_path = DATA_PATH / "exoplanets.csv"

    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"Datos guardados en {file_path}")

if __name__ == "__main__":
    download_data()
