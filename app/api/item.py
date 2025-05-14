from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import item, item_update_base
from app.db.session import SessionLocal
from app.services.item import create_item, get_item, update_item, delete_item

router = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=item.Item)
def create_item(item_data: item.ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item_data)

@router.get("/{item_id}", response_model=item.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return get_item(db, item_id)

@router.put("/{name}", response_model=item_update_base.ItemUpdate)
def update_item_root(name:str, item_data: item_update_base.ItemUpdate, db: Session =Depends(get_db)):
    return update_item(db, name, item_data)

@router.delete("/{item_id}", response_model=item.Item)
def delete_item_root(item_id: int, db: Session = Depends(get_db)):
    return delete_item(db, item_id)