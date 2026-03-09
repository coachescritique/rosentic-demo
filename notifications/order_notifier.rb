require_relative "mailer"

class OrderNotifier
  def initialize
    @mailer = Mailer.new
  end

  def order_placed(user_id, order_id)
    @mailer.send_notification(user_id, "Order Confirmed", "Your order #{order_id} has been placed.")
  end

  def order_shipped(user_id, order_id, tracking)
    @mailer.send_notification(user_id, "Order Shipped", "Your order #{order_id} is on the way. Tracking: #{tracking}")
  end

  def notify_all(user_ids, message)
    @mailer.send_bulk(user_ids, "Update", message)
  end
end
