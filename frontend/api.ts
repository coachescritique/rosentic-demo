import { z } from "zod";

export const createOrderSchema = z.object({
    userId: z.string(),
    productId: z.string(),
    quantity: z.number().optional(),
});

export const orderResponseSchema = z.object({
    orderId: z.string(),
    userId: z.string(),
    productId: z.string(),
    status: z.string(),
    total: z.number(),
});

export async function createOrder(data: z.infer<typeof createOrderSchema>) {
    const validated = createOrderSchema.parse(data);
    const response = await fetch("/api/order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userId: validated.userId, productId: validated.productId }),
    });
    const json = await response.json();
    return orderResponseSchema.parse(json);
}
