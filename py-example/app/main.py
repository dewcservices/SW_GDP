from fastapi import FastAPI
from app.controllers import item_controller

app = FastAPI()

app.include_router(item_controller.router, prefix="/api/items", tags=["items"])

