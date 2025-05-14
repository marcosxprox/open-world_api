from sqlalchemy.orm import Session
from app.models.player import Player
from fastapi import HTTPException
from app.core.security import verify_password, create_access_token
from app.schemas.player_auth import Playerlogin

def player_login(db: Session, player_data: Playerlogin):
    db_player = db.query(Player).filter(Player.username == player_data.username).first()# type: ignore
    if db_player is None:
        raise HTTPException(status_code=400, detail="Player not found")
    db_password = verify_password(player_data.password, db_player.password)
    if db_password:
        access_token = create_access_token(data={"sub":player_data.username})
        return {"access_token":access_token, "token_type":"bearer"}
    else:
        raise HTTPException(status_code=400, detail="Invalid username or password")
