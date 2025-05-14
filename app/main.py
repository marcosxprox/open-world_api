from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import player, item, player_login
from app.sockets.websocket import router as websocket_router

app = FastAPI(
title="OpenWorld API",
    description="API para um mundo aberto com jogadores, itens e batalhas.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message":"Bem-vindo ao openworld Api!"}

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(player.router, prefix="/players", tags=["Players"])
app.include_router(item.router, prefix="/items", tags=["Items"])
app.include_router(player_login.router, prefix="/Auth", tags=["Auth"])
app.include_router(websocket_router)
