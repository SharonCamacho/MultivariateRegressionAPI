# ML Implementing Challenge - Deployment

## Description

This section contains all the necessary components to deploy the trained model as a service. The API serves predictions based on input data and includes endpoints for health checks and web-based interaction.

## Deploy Directory Structure
```
│──deploy  
│   ├── app  #Application Code
│   │    ├── models  # Stores the trained regression model
│   │    │     ├── modelo_regresion.pkl  # Trained model
│   │    ├── routers  #Defines API endpoints
│   │    │     ├──health.py  # Endpoint to verify the service
│   │    │     ├──home.py  # Home page for the prediction
│   │    │     ├──predict.py  # Endpoint for making predictions
│   │    ├── services  #Implements model loading and prediction logic 
│   │    │     ├──model_service.py  # Load and use training model
│   │    ├── config.py  # General API setup
│   │    ├── main.py  # Main entry point
│   ├── static  
│   │    ├── index.html  # Web interface  
│   ├── Dockerfile  # Defines the environment to package and deploy the application using Docker.
│   ├── Readme.md # API Documentation
│   ├── requirements.txt  # Project dependencies  
│   ├── .gitignore  # Files and folders ignored by Git
│   ├── .dockerignore  # Files ignored in the Docker image
```

- app/: Contains API endpoints to serve predictions.
- static/: Web interface for interacting with the model.
- Dockerfile: Instructions for containerizing the application.
- requirements.txt: Dependencies needed to run the service.

# Installation and Usage

## 1. Prerequisites

- Python (3.13)
- FastAPI (0.115.8)
- scikit-learn (1.6.1)
- Pandas (2.2.3)
- XGBoost (2.1.4)
- Joblib (1.4.2)
- Uvicorn (0.34.0)
- Starlette (0.45.3)
- Jinja2 (3.1.5)
- Python-Multipart (0.0.20)
- Docker (optional)

## 2. Installation

From the `deploy/` directory root, install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the API Locally
Navigate to the `deploy/` directory and execute:

```bash
python -m app.main
```
The API will be available at:

[http://localhost:8080](http://localhost:8080)


### 4. Make Predictions
- Open the following URL in your browser:

[http://localhost:8080/predict](http://localhost:8080/predict)

- Or use **Postman**:
  1. Select `POST`.
  2. Enter the URL: `http://localhost:8080/predict/`
  3. In **Body** → **form-data**, add a key named `file`, set type to `File`, and upload a CSV file.
  4. Click **Send** to get the predictions.

### 5. Check API Health
Verify service availability using:

[http://localhost:8080/health](http://localhost:8080/health)

Or via **Postman**:
```bash
GET http://localhost:8080/health
```

### 6. Deploy Using Docker
Build and run the containerized application:
```bash
docker build -t ml-api .
docker run -p 8080:8080 ml-api
```
The service will be available at:
```
http://localhost:8080
```

### 7. Deploy to Cloud Run
#### Build the Image
```bash
gcloud builds submit --tag gcr.io/proyect_id/cloud_run_name
```

#### Deploy the Application
```bash
gcloud run deploy --image gcr.io/proyect_id/cloud_run_name --platform managed --region us-central1 --allow-unauthenticated
```

## Notes
- The API is designed for deployment on **Google Cloud Run**.
- The trained model should be updated periodically to maintain accuracy.
- CORS is enabled to allow external access to the API.
