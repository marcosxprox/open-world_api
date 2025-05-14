from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import player_response, player_auth, player_update
from app.db.session import get_db
from app.services.player import create_player, get_player, update_player, delete_player
from .dependencies import get_current_user
from app.models.player import Player

router = APIRouter()

@router.post("/", response_model=player_response.Player)
def register_player(player: player_auth.PlayerCreate, db: Session = Depends(get_db)):
    return create_player(db, player)

@router.get("/{player_id}", response_model=player_response.Player)
def get_player(player_id: int, db: Session = Depends(get_db), current_user: Player = Depends(get_current_user)):
    if current_user.id != player_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Você não pode acessar dados de outro jogador.")
    return get_player(db, player_id)

@router.put("/{username}", response_model=player_update.PlayerUpdate)
def update_player_root(username:str, player_data: player_update.PlayerUpdate, db: Session = Depends(get_db),
                       current_user: Player = Depends(get_current_user)):
    if current_user.username != username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Você não pode acessar dados de outro jogador.")
    return update_player(db, username, player_data)

@router.delete("/{player_id}", response_model=player_response.Player)
def delete_player_root(player_id: int, db: Session = Depends(get_db), current_user: Player = Depends(get_current_user)):
    if current_user.id != player_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Você não pode acessar dados de outro jogador.")
    return delete_player(db, player_id)