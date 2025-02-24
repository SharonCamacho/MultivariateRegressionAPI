from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.config import STATIC_DIR

router = APIRouter()

@router.get("/predict")
def home():
    return FileResponse(f"{STATIC_DIR}/index.html")
