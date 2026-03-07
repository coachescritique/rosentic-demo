package payment

import "testing"

func TestProcessPaymentBasic(t *testing.T) {
	txnID, err := ProcessPayment(100.0, "acc1")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if txnID == "" {
		t.Fatal("expected non-empty transaction ID")
	}
}

func TestProcessPaymentLargeAmount(t *testing.T) {
	txnID, err := ProcessPayment(9999.99, "acc2")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if txnID != "txn_acc2_10000" {
		t.Errorf("unexpected txnID: %s", txnID)
	}
}

func TestProcessPaymentZero(t *testing.T) {
	_, err := ProcessPayment(0, "acc3")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
}
