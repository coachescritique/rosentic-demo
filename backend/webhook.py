import subprocess


def call_payment_service(amount, account_id):
    """Call the Go payment microservice via subprocess."""
    result = subprocess.run(
        ["go", "run", "./payment", str(amount), account_id],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def handle_payment_webhook(event):
    """Process incoming payment webhook events."""
    amount = event["amount"]
    account_id = event["account_id"]

    txn_id = call_payment_service(amount, account_id)
    return {"transaction_id": txn_id, "status": "processed"}


def process_refund(original_amount, account_id):
    """Issue a refund by calling payment service with negative amount."""
    return call_payment_service(-original_amount, account_id)
