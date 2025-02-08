from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def home():
    file_path = "ws.html"  # 请将此路径替换为实际的文件路径
    return FileResponse(file_path)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
