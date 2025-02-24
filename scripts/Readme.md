# ML Implementing Challenge - Scripts

## Description
This section focuses on training and evaluating machine learning models for regression tasks. The scripts provided facilitate the experimentation, selection, and training of the best-performing model to be deployed as part of the overall project.

## Scripts Directory Structure
```
│──scripts  
│   ├── model_selection.ipynb  # Training Notebook
│   ├── model.py  # Script for training the model
│   ├── modelo_regresion.pkl  # Trained model copy
│   ├── Readme.md # Scripts Documentation
│   ├── requirements.txt  # Project dependencies  
```

- model_selection.ipynb: Jupyter Notebook for model experimentation and selection.
- model.py: Python script for training and saving the model.
- modelo_regresion.pkl: A copy of the trained model for inference.
- requirements.txt: Dependencies needed to run the Notebook and Script.

# Installation and Usage

## 1. Prerequisites

- Python (3.13)
- scikit-learn (1.6.1)
- Pandas (2.2.3)
- XGBoost (2.1.4)
- LightGBM (4.6.0)
- Statsmodels (0.14.4)
- Joblib (1.4.2)


## 2. Installation

From the `scripts/` directory root, install the dependencies:

```bash
pip install -r requirements.txt
```

## 3. Contents

### A. `model_selection.ipynb` - Model Selection Notebook

This Jupyter Notebook is dedicated to selecting and evaluating machine learning models for regression problems. It covers the full workflow from data loading to model evaluation.

For exploratory data analysis and model selection, open and run:
```bash
jupyter notebook scripts/model_selection.ipynb
```

**Contents**
- **Data Loading **
  - Importing necessary libraries (pandas, numpy, scikit-learn, seaborn, etc.).
  - Reading the dataset (`training_data.csv`).
- **Exploratory Data Analysis (EDA)**
  - Visualizing the distribution of the target variable.
  - Statistical tests for normality (Shapiro-Wilk test).
- **Data Preprocessing**
  - Splitting data into training and test sets (`train_test_split`).
- **Model Selection 🤖**
  - Evaluating different regression models:
    - Linear Regression
    - Random Forest Regressor
    - Lasso
    - Ridge
    - XGBoost
    - LightGBM
- **Model Evaluation**
  - Using metrics like Mean Squared Error (MSE), Mean Absolute Error (MAE), R2 score, and Mean Absolute Percentage Error (MAPE).
  - Performing cross-validation (`cross_val_score`).
  - Hyperparameter tuning using `GridSearchCV`.

**Usage**
Execute the notebook step by step to determine the best-performing model based on evaluation metrics.

### B. `model.py` - Training Script

This Python script trains a regression model using XGBoost and saves it for later inference.

**Contents**
- **Data Loading**
  - Reads a dataset from a CSV file.
  - Splits the data into features (`X`) and the target variable (`y`).
  - Divides the dataset into training and testing sets (`train_test_split`).
- **Model Training**
  - Trains an `XGBRegressor` model with customizable hyperparameters.
- **Model Saving**
  - Saves the trained model as `modelo_regresion.pkl` in `deploy/app/models/` using `joblib`.

**Usage**
Run the script from the project root, to train and save the regression model:
```bash
python scripts/model.py
```

### C. `modelo_regresion.pkl` - Trained Model
- This file is a copy of the trained regression model, saved in a serialized format for deployment.

### D. `requirements.txt` - Dependencies
- Lists all the necessary libraries required to execute the notebook and training script.


## Notes
- The `modelo_regresion.pkl` file should be periodically updated with newly trained models to maintain performance over time.
- The scripts are modular and can be modified to test additional models or preprocessing techniques as needed.