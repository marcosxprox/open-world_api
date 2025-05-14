from pydantic import BaseModel

class ItemBase(BaseModel):
    name:str
    description:str
    quantity:int = 1

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id:int

    class Config:
            orm_mode = True