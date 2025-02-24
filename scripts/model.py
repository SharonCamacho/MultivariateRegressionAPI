import os
import pandas as pd
import joblib
import logging
from sklearn.model_selection import train_test_split
import xgboost as xgb

class ModelTrainer:
    def __init__(self, data_path: str, target_column: str, model_path: str = "deploy/app/models/modelo_regresion.pkl"):
        self.data_path = data_path
        self.target_column = target_column
        self.model_path = model_path
        self.model = None
        self.X_train, self.X_test, self.y_train, self.y_test = self.load_and_split_data()

    def load_and_split_data(self, test_size: float = 0.25, random_state: int = 42):
        """Split Data in train and test"""
        df = pd.read_csv(self.data_path)
        X = df.drop(columns=self.target_column)
        y = df[self.target_column]
        return train_test_split(X, y, test_size=test_size, random_state=random_state)

    def train(self, **model_params):
        """Train the model"""
        logging.info("XGBoost Training")
        self.model = xgb.XGBRegressor(**model_params)
        self.model.fit(self.X_train, self.y_train)
        logging.info("Training Completed")

    def save_model(self):
        """Save the model"""
        if self.model is None:
            raise ValueError("Model can't be saved")
        joblib.dump(self.model, self.model_path)
        logging.info(f"Model saved en {self.model_path}")

if __name__ == "__main__":
    trainer = ModelTrainer(data_path="data/training_data.csv", target_column="target")
    trainer.train(n_estimators=300, learning_rate=0.05, max_depth=3, subsample=0.7, colsample_bytree=1.0)
    trainer.save_model()

