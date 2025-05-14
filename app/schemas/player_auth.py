from .player import PlayerBase
from pydantic import BaseModel

class PlayerCreate(PlayerBase):
    password:str

class Playerlogin(BaseModel):
    username:str
    password:str
