from backend.main import create_order


def test_create_order_returns_status():
    result = create_order("user_1", "prod_1")
    assert result["status"] == "created"


def test_create_order_returns_order_id():
    result = create_order("user_2", "prod_2")
    assert "order_id" in result


def test_create_order_multiple():
    r1 = create_order("user_3", "prod_3")
    r2 = create_order("user_4", "prod_4")
    assert r1["user_id"] == "user_3"
    assert r2["user_id"] == "user_4"
