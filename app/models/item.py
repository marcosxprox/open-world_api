from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Item(Base):

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    quantity = Column(Integer, default=1)


