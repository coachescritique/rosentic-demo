from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class CreateOrderRequest(BaseModel):
    user_id: str
    product_id: str
    quantity: int = 1


class OrderResponse(BaseModel):
    order_id: str
    user_id: str
    product_id: str
    status: str
    total: float


def create_order(user_id, product_id):
    return {"order_id": "ord_123", "user_id": user_id, "product_id": product_id, "status": "created"}


@app.post("/order")
def order_endpoint(order: CreateOrderRequest) -> OrderResponse:
    return create_order(order.user_id, order.product_id)
