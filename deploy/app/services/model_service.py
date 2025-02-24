import joblib
import pandas as pd
from app.config import MODEL_PATH

class ModelService:
    def __init__(self):
        try:
            self.model = joblib.load(MODEL_PATH)
            print("Modelo cargado correctamente.")
        except Exception as e:
            print(f"Error cargando el modelo: {e}")
            self.model = None

    def predict(self, df: pd.DataFrame):
        if self.model is None:
            raise ValueError("Modelo no encontrado")
        return self.model.predict(df)
