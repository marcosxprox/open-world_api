from pydantic import BaseModel

class PlayerBase(BaseModel):
    username:str
    level:int = 1
    health:int = 100
    stamine:int = 100

    class Config:
        orm_mode = True