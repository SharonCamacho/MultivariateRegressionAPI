import joblib
import pandas as pd
from app.config import MODEL_PATH

class ModelService:
    def __init__(self):
        try:
            self.model = joblib.load(MODEL_PATH)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def predict(self, df: pd.DataFrame):
        if self.model is None:
            raise ValueError("Model not found")
        return self.model.predict(df)
