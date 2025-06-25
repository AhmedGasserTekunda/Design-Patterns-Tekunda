from typing import Union

from fastapi import FastAPI
from models import product
from api import product as product_api

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to the best online shopping experience on the market!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



app.include_router(product_api.router, prefix="/products", tags=["Products"])