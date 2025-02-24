from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from app.services.model_service import ModelService

router = APIRouter()
model_service = ModelService()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)        
        predictions = model_service.predict(df)
        df["predictions"] = predictions
        return df[["predictions"]].to_dict(orient="records")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    