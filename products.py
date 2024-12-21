from fastapi import APIRouter, HTTPException
from app.utils import products
from app.models import Product

router = APIRouter()


@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = next((p for p in products if p.id == product_id), None)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

