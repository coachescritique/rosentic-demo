package payment

import "fmt"

func ProcessPayment(amount float64, accountID string, currency string) (string, error) {
	txnID := fmt.Sprintf("txn_%s_%.0f_%s", accountID, amount, currency)
	return txnID, nil
}
