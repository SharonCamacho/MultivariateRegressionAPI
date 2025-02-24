from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health Check"])
async def health_check():
    """
    Endpoint de Health Check.
    """
    return {"status": "ok", "message": "Service is running"}


