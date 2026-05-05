class Mailer
  def send_notification(user_id, subject, body, priority)
    puts "Sending '#{subject}' to user #{user_id} [#{priority}]"
    { status: "sent", user_id: user_id, subject: subject, priority: priority }
  end

  def send_bulk(user_ids, subject, body, priority)
    user_ids.map { |uid| send_notification(uid, subject, body, priority) }
  end
end
