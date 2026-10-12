from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.router.dashboard_router import router as dashboard_router
from src.router.relogio_router import router as relogio_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(dashboard_router)
app.include_router(relogio_router)
