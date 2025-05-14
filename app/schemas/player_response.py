from .player import PlayerBase

class Player(PlayerBase):
    id:int

    class Config:
        orm_mode = True