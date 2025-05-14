from fastapi import APIRouter, Depends
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.services.player_login import player_login
from app.schemas.player_auth import Playerlogin

router = APIRouter()

@router.post("/login", tags=["Auth"])
def login(player_data: Playerlogin, db: Session = Depends(get_db)):
    return player_login(db, player_data)

