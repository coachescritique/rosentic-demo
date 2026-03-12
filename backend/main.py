from fastapi import FastAPI

app = FastAPI()


def create_order(user_id, product_id, shipping_address):
    return {
        "order_id": "ord_123",
        "user_id": user_id,
        "product_id": product_id,
        "shipping_address": shipping_address,
        "status": "created",
    }


@app.post("/order")
def order_endpoint(user_id: str, product_id: str, shipping_address: str):
    return create_order(user_id, product_id, shipping_address)
