from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from aibot.database import get_order_data
from aibot.vector_db import insert_vector, query_similar_vectors
import asyncio
import uvicorn
from aibot.websocket_server import start_websocket_server

app = FastAPI()


class OrderRequest(BaseModel):
    order_id: int


class VectorRequest(BaseModel):
    vector: List[float]


@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Agent API"}


@app.post("/order")
def get_order(order_request: OrderRequest):
    order = get_order_data(order_request.order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.post("/vector/insert")
def insert_vector_data(vector_request: VectorRequest):
    insert_vector("vectors", vector_request.vector)
    return {"message": "Vector inserted successfully"}


@app.post("/vector/query")
def query_vectors(vector_request: VectorRequest):
    results = query_similar_vectors("vectors", vector_request.vector)
    return {"results": results}


async def main():
    websocket_task = asyncio.create_task(start_websocket_server())
    api_task = asyncio.create_task(uvicorn.run(app, host="0.0.0.0", port=8000))
    await asyncio.gather(websocket_task, api_task)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "asyncio.run() cannot be called from a running event loop" in str(e):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        else:
            raise
