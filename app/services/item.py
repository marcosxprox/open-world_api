from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas import item, item_update_base
from fastapi import HTTPException

def create_item(db: Session, item_data: item.ItemCreate):
    db_item = db.query(Item).filter(Item.description == item_data.description).first()# type: ignore
    if db_item:
        raise HTTPException(status_code=400, detail="Item is already registered")
    db_item = Item(**item_data.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()# type: ignore
    if db_item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return db_item

def update_item(db: Session, name:str, item_data: item_update_base.ItemUpdate):
    db_item = db.query(Item).filter(Item.name == name).first()# type: ignore
    if not db_item:
        raise HTTPException(status_code=404, detail="item not found")
    for key, value in item_data.model_dump(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()# type: ignore
    if db_item is None:
        raise HTTPException(status_code=404, detail="item not found")
    db.delete(db_item)
    db.commit()
    return {"detail":f"Item '{db_item.name}' deletado com sucesso"}


