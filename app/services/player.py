from sqlalchemy.orm import Session
from app.models.player import Player
from app.schemas.player_auth import PlayerCreate
from app.schemas.player_update import PlayerUpdate
from fastapi import HTTPException
from app.core.security import hashed_password

def create_player(db: Session, player_data: PlayerCreate):
    db_player = db.query(Player).filter(Player.username == player_data.username).first()# type: ignore
    if db_player:
        raise HTTPException(status_code=400, detail="Username is already registered")

    hash_password = hashed_password(player_data.password)
    db_player = Player(**player_data.model_dump(), password = hash_password)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_player(db: Session, player_id: int):
    db_player = db.query(Player).filter(Player.id == player_id).first()# type: ignore
    if db_player is None:
        raise HTTPException(status_code=404, detail="player not found")
    return db_player

def update_player(db: Session, username: str, player_data: PlayerUpdate):
    db_player = db.query(Player).filter(Player.username == username).first()# type: ignore
    if not db_player:
        raise HTTPException(status_code=404, detail="player not found")
    for key, value in player_data.model_dump(exclude_unset=True).items():
        setattr(db_player, key, value)
    db.commit()
    db.refresh(db_player)
    return db_player

def delete_player(db: Session, player_id:int):
    db_player = db.query(Player).filter(Player.id == player_id).first()# type: ignore
    if not db_player:
        raise  HTTPException(status_code=404, detail="player not found")
    db.delete(db_player)
    db.commit()
    return {"detail":f"Player '{db_player.username}' deletado com sucesso"}