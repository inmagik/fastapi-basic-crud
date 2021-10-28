from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items", response_model=List[schemas.Item])
def items_action_list(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    items = crud.list_items(db, offset, limit)
    return items


@app.get("/items/{item_id}", response_model=schemas.Item)
def items_action_retrieve(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404)
    return item


@app.post("/items", response_model=schemas.Item)
def item_action_create(data: schemas.ItemCreate, db: Session = Depends(get_db)):
    item = crud.create_item(db, data)
    return item


@app.put("/items/{item_id}", response_model=schemas.Item)
def items_action_retrieve(item_id: int, data: schemas.ItemUpdate,  db: Session = Depends(get_db)):
    item = crud.update_item(db, item_id, data)
    if item is None:
        raise HTTPException(status_code=404)
    return item


@app.delete("/items/{item_id}", status_code=204)
def items_action_retrieve(item_id: int,  db: Session = Depends(get_db)):
    crud.drop_item(db, item_id)
    return None