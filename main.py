from fastapi import FastAPI
from app.routes.products import router as product_router

app = FastAPI()

app.include_router(product_router)
