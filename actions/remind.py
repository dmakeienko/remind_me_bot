# from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from db.database import check_remind

def remind(bot, job):
  if check_remind():
    for r in check_remind():
      print(f"id: {r['id']}  {r['remind_text']}")
      remind = f"Don`t forget: {r['remind_text']}\n"
      user_chat_id = r['chat_id']

    bot.send_message(chat_id=user_chat_id, text=remind)
  else:
    return

