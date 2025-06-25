from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import product as crud_product
from schemas import product as schema_product
from database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema_product.Product)
def create_product(product: schema_product.ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db, product)

@router.get("/", response_model=list[schema_product.Product])
def read_products(db: Session = Depends(get_db)):
    return crud_product.get_products(db)

@router.get("/{product_id}", response_model=schema_product.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_product.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
