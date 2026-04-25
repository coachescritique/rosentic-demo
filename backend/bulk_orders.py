from backend.main import create_order


def process_bulk(order_list):
    results = []
    for item in order_list:
        result = create_order(item["user_id"], item["product_id"])
        results.append(result)
    return results


def create_sample_orders():
    create_order("bulk_user_1", "sku_001")
    create_order("bulk_user_2", "sku_002")
    create_order("bulk_user_3", "sku_003")
