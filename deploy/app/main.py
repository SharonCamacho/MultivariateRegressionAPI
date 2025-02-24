from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers import predict, home, health
import os

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
static_path = os.path.join(os.path.dirname(__file__), "../static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

app.include_router(predict.router)
app.include_router(home.router)
app.include_router(health.router)


@app.get("/")
async def root():
    return {"message": "Sharon Camacho - Data Science ML Modeling Challenge"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
