from db.database import check_remind
from utils.constants import EXPIRED_REMIND_TIME

def remind(bot, job):
  if check_remind():
    for r in check_remind():
      remind = f"Don`t forget: {r['remind_text']}\n"
      user_chat_id = r['chat_id']

    bot.send_message(chat_id=user_chat_id, text=remind)
  else:
    return


def remind_1(bot, job):
  if check_remind(1):
    for r in check_remind(1):
      remind = f"Don`t forget: {r['remind_text']}\n"
      user_chat_id = r['chat_id']

    bot.send_message(chat_id=user_chat_id, text=remind)
  else:
    return


def remind_2(bot, job):
  if check_remind(2):
    for r in check_remind(2):
      remind = f"Don`t forget: {r['remind_text']}\n"
      user_chat_id = r['chat_id']

    bot.send_message(chat_id=user_chat_id, text=remind)
  else:
    return


def check_expired(bot, job):
    for r in check_remind(4)[1]:
      if check_remind(4)[0] == 'expired':
        user_chat_id = r['chat_id']
        final_remind= 'Sorry, your task expired'
        bot.send_message(chat_id=user_chat_id, text=final_remind)
    else:
      return