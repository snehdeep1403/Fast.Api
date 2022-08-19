from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
import models
import schemas
import repositories
from sqlalchemy.orm import Session
from db import engine, get_db
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product - Store demo", description="This is same application for products and stores")

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})



@app.get('/')
def homepage():
    return "This is root directory"

@app.post('/stores', response_model=schemas.Store)
async def add_store(store_request : schemas.StoreCreate, db : Session = Depends(get_db)):
    return await repositories.StoreRepo.create(db, store_request)


@app.post('/products', response_model=schemas.Product)
async def add_product(product_request : schemas.ProductCreate, db : Session = Depends(get_db)):
    return await repositories.ProductRepo.create(db, product_request)

@app.get("/stores", response_model=List[schemas.Store])
def get_all_stores(db: Session = Depends(get_db)):
    return repositories.StoreRepo.fetch_all(db)
