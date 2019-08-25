from apscheduler.schedulers.background import BackgroundScheduler 
from db.database import check_remind


def remind(bot, update):
  if check_remind:
    for r in check_remind():
      print(f"id: {r['id']}  {r['remind_text']}")
      remind = f"Don`t forget: {r['remind_text']}\n"

  bot.send_message(chat_id=update.message.chat_id, text=remind)



scheduler = BackgroundScheduler()


scheduler.add_job(remind, 'interval', minutes=5)
scheduler.start()
