class Mailer
  def send_notification(user_id, subject, body)
    puts "Sending '#{subject}' to user #{user_id}"
    { status: "sent", user_id: user_id, subject: subject }
  end

  def send_bulk(user_ids, subject, body)
    user_ids.map { |uid| send_notification(uid, subject, body) }
  end
end
