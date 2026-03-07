import { createOrder } from "../api";

interface CheckoutProps {
    userId: string;
    productId: string;
}

export function Checkout({ userId, productId }: CheckoutProps) {
    const handleSubmit = async () => {
        const order = await createOrder(userId, productId);
        console.log("Order placed:", order.orderId);
    };

    const handleBulkOrder = async (productIds: string[]) => {
        for (const pid of productIds) {
            await createOrder(userId, pid);
        }
    };

    return null;
}
