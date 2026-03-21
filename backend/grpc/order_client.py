import grpc
from order_pb2 import CreateOrderRequest, OrderResponse, GetOrderRequest
from order_pb2_grpc import OrderServiceStub


def place_order(user_id: str, product_id: str, quantity: int = 1):
    channel = grpc.insecure_channel("localhost:50051")
    stub = OrderServiceStub(channel)

    request = CreateOrderRequest(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity,
    )
    response = stub.CreateOrder(request)
    print(f"Order {response.order_id} created, total: {response.total}")
    return response


def get_order(order_id: str):
    channel = grpc.insecure_channel("localhost:50051")
    stub = OrderServiceStub(channel)

    request = GetOrderRequest(order_id=order_id)
    response = stub.GetOrder(request)
    return response
