from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

@router.websocket("/ws/{player_id}")
async def websocket_endpoint(websocket: WebSocket, player_id:int):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            print(f"mensagem recebida do jogador {player_id}: {data}")
            await websocket.send_text(f"mensagem recebida: {data}")
    except WebSocketDisconnect:
        print(f"Jogador {player_id} se disconectou.")
