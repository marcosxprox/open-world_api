from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Player(Base):

    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    level = Column(Integer, default=1)
    health = Column(Integer, default=100)
    stamine = Column(Integer, default=100)
    password = Column(String)