from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health Check"])
async def health_check():
    """
    Endpoint de Health Check.
    Devuelve un mensaje indicando que el servicio está en funcionamiento.
    """
    return {"status": "ok", "message": "Service is running"}


