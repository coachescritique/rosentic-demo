from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class CreateOrderRequest(BaseModel):
    user_id: str
    product_id: str
    quantity: int = 1
    shipping_address: str
    priority: Optional[str] = None


class OrderResponse(BaseModel):
    order_id: str
    user_id: str
    product_id: str
    status: str


def create_order(user_id, product_id, shipping_address):
    return {"order_id": "ord_123", "user_id": user_id, "product_id": product_id, "status": "created"}


@app.post("/order")
def order_endpoint(order: CreateOrderRequest) -> OrderResponse:
    return create_order(order.user_id, order.product_id, order.shipping_address)
