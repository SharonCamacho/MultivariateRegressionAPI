# ML Implementing Challenge
##### By Sharon Camacho

## Description

The goal is to predict the target variable using the given data regularly in a productive environment and how to use new data to keep good performance on the predictions in the long term.

**Tasks**
1. Train a model using the training data set.
2. Create a project that can be deployed easily. The PoC needs to use the model you created to provide new predictions (use the provided blind test dataset to test your solution).
3. Describe briefly how you can evolve the solution and any considerations you have in mind for it.

## Project Structure
```
MultivariateRegressionAPI
│──data  
|   ├── blind_test_data.csv  # Testing data without target variable  
|   ├── training_data.csv  # Training data with target variable
│──deploy  
│   ├── app  
│   │    ├── models  
│   │    │     ├── modelo_regresion.pkl  # Trained model
│   │    ├── routers  
│   │    │     ├──health.py  # Endpoint to verify the service
│   │    │     ├──home.py  # Home page for the prediction
│   │    │     ├──predict.py  # Endpoint for making predictions
│   │    ├── services  
│   │    │     ├──model_service.py  # Load and use training model
│   │    ├── config.py  # General setup
│   │    ├── main.py  # Main entry point
│   ├── static  
│   │    ├── index.html  # Web interface  
│   ├── Dockerfile  # File to create the Docker image
│   ├── Readme.md # API Documentation
│   ├── requirements.txt  # Project dependencies  
│   ├── .gitignore  # Files and folders ignored by Git
│   ├── .dockerignore  # Files ignored in the Docker image
│──scripts  
│   ├── model_selection.ipynb  # Training Notebook
│   ├── model.py  # Script for training the model
│   ├── modelo_regresion.pkl  # Trained model copy
│   ├── Readme.md # Scripts Documentation
│   ├── requirements.txt  # Project dependencies  
│──Readme.md  # General Project Documentation  
```

To achieve the proposed tasks, the project is structured as follows:

**scripts/** (Objective 1 - Model Training)
This folder contains the necessary scripts for training the model. The main components include:
- model_selection.ipynb: Jupyter Notebook for model experimentation and selection.
- model.py: Python script for training and saving the model.
- modelo_regresion.pkl: A copy of the trained model for inference.
- requirements.txt: Dependencies needed to run the Notebook and Script.

**deploy/** (Objective 2 - Deployment)
This folder provides the necessary components to deploy the trained model as a service. It includes:
- app/: Contains API endpoints to serve predictions.
- static/: Web interface for interacting with the model.
- Dockerfile: Instructions for containerizing the application.
- requirements.txt: Dependencies needed to run the service.

The architecture ensures an efficient workflow from model training to deployment, making it scalable and easy to maintain.

# Installation and Usage

## 1. Prerequisites

- Python (3.13)
- FastAPI (0.115.8)
- scikit-learn (1.6.1)
- Pandas (2.2.3)
- XGBoost (2.1.4)
- LightGBM (4.6.0)
- Statsmodels (0.14.4)
- Joblib (1.4.2)
- Uvicorn (0.34.0)
- Starlette (0.45.3)
- Jinja2 (3.1.5)
- Python-Multipart (0.0.20)
- Docker (optional)

## 2. Installation

Clone the repository and navigate to the project folder:

```bash
git clone <repository>
cd <repository>
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

It is important to know that each folder contains its own dependencies to facilitate the development of each objective.

## 3. Train the Model

To train the model, load new data into the `data/` directory with the name 'training_data.csv'.

For exploratory data analysis and data modeling, you can run the `model_selection.ipynb` notebook in the `scripts/` directory.

If you just want to retrain the model, after loading new data, execute the `model.py` script from the project root:

```bash
python scripts/model.py
```

The new model will be saved in the `models/` directory of the app.

## 4. API Usage  

The API is deployed on **Cloud Run**, and you can access it using **Postman** or directly from your web browser (for GET requests).  

### - Make a prediction  
You can send a file for prediction by opening the following URL in your browser:

[https://productivo-872939375636.us-central1.run.app/predict](https://productivo-872939375636.us-central1.run.app/predict)

Use 'blind_test_data.csv' in data directory to test the API.

You can also download predictions by clicking on the "Download CSV" button.

Or using **Postman**:  
1. Open **Postman** and select `POST`.  
2. Enter the URL:  
   ```
   https://productivo-872939375636.us-central1.run.app/predict/
   ```
3. Go to the **Body** tab, select **form-data**.  
4. Add a key named **file**, set its type to **File**, and upload your CSV file.  
5. Click **Send** to get the prediction.  

### - Check service health  
You can check the service health by opening the following URL in your browser:  

[https://productivo-872939375636.us-central1.run.app/health](https://productivo-872939375636.us-central1.run.app/health)

Or using **Postman**:  
```bash
GET https://productivo-872939375636.us-central1.run.app/health
```

## 5. Deploy the Service Locally

From the `deploy/` directory root:

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the API locally:

```bash
python -m app.main
```

The API will be available at:

[http://localhost:8080](http://localhost:8080)


- Make a prediction  

[http://localhost:8080/predict](http://localhost:8080/predict)


Or using **Postman** as we shown before.

## Evolution and Considerations

1. **Retraining:** The current process does not include metric comparison, which is essential for evaluating model improvements.
2. **Automated Training:** Implement pipelines for continuous model improvement using tools like MLflow, which allows tracking model performance over time.
3. **Monitoring:** Add logging and metrics to assess the model’s performance in production.
4. **Testing:** Implement unit and integration tests to ensure the API’s reliability and correctness before deployment.

## Contact

For any questions or improvements, feel free to contact me at [sharoncamachog@gmail.com].