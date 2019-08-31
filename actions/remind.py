# from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from db.database import check_remind, expire_remind

def remind(bot, job):
  if check_remind():
    for r in check_remind():
      print(f"id: {r['id']}  {r['remind_text']}")
      remind = f"Don`t forget: {r['remind_text']}\n"
      user_chat_id = r['chat_id']

    bot.send_message(chat_id=user_chat_id, text=remind)
  else:
    return


def remind_1(bot, job):
  if check_remind(1):
    for r in check_remind(1):
      print(f"id: {r['id']}  {r['remind_text']}")
      remind = f"Don`t forget: {r['remind_text']}\n"
      user_chat_id = r['chat_id']

    bot.send_message(chat_id=user_chat_id, text=remind)
  else:
    return


def remind_2(bot, job):
  if check_remind(2):
    for r in check_remind(2):
      print(f"id: {r['id']}  {r['remind_text']}")
      remind = f"Don`t forget: {r['remind_text']}\n"
      user_chat_id = r['chat_id']

    bot.send_message(chat_id=user_chat_id, text=remind)
  else:
    return


def check_expired(bot, job):
    for r in check_remind(4)[1]:
      if check_remind(4)[0] == 'expired':
        print(f"id: {r['id']}  {r['remind_text']}")
        user_chat_id = r['chat_id']
        final_remind= 'Sorry, your task expired'
        bot.send_message(chat_id=user_chat_id, text=final_remind)
    else:
      return