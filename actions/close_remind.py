from db.database import close, _get_remind
import datetime
from utils.constants import DATETIME_FORMAT

def close_remind(bot, update, args):
  user_chat_id = update.message.chat_id
  if len(args) > 1:
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I can't close more than one remind at a time 😔")
  else:
    try: 
        closed_id = close(user_chat_id, args)
        for r in _get_remind(user_chat_id, closed_id):
          remind = f"⏰ Remind ({r['id']}): 📌 \"{r['remind_text']} on {datetime.datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')}\" marked as Done!✅"
        bot.send_message(chat_id=update.message.chat_id, text=remind)
    except:
      bot.send_message(chat_id=update.message.chat_id, text="Sorry, there is no remind(s) with such id(s) 😔")


def close_remind(bot, chat_id):  
  try: 
      closed_id = close(chat_id, '')
      for r in _get_remind(chat_id, closed_id):
        remind = f"⏰ Remind ({r['id']}): 📌 \"{r['remind_text']} on {datetime.datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')}\" marked as Done!✅"
      bot.send_message(chat_id=chat_id, text=remind)
  except:
    bot.send_message(chat_id=chat_id, text="Sorry, there is no remind(s) with such id(s) 😔")
