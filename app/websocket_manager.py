from fastapi import WebSocket

class WSManager:
    def __init__(self):
        self.active = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    async def disconnect(self, ws: WebSocket):
        self.active.remove(ws)

    async def broadcast(self, data):
        for ws in self.active:
            await ws.send_json(data)

ws_manager = WSManager()