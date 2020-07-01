from db.database import close, _get_remind
import datetime
from utils.constants import DATETIME_FORMAT

def close_remind(update, context):
  user_chat_id = update.message.chat_id
  if len(context.args) > 1:
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I can't close more than one remind at a time 😔")
  else:
    try: 
        closed_id = close(user_chat_id, args)
        for r in _get_remind(user_chat_id, closed_id):
          remind = f"⏰ Remind ({r['id']}): 📌 \"{r['remind_text']} on {datetime.datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')}\" marked as Done!✅"
        context.bot.send_message(chat_id=update.message.chat_id, text=remind)
    except:
      context.bot.send_message(chat_id=update.message.chat_id,
                               text="Sorry, there is no remind(s) with such id(s) 😔")


def close_remind_button(update, context):  
  try: 
      chat_id = update.effective_chat.id
      closed_id = close(chat_id, '')
      for r in _get_remind(chat_id, closed_id):
        remind = f"⏰ Remind ({r['id']}): 📌 \"{r['remind_text']} on {datetime.datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')}\" marked as Done!✅"
      context.bot.send_message(chat_id=chat_id, text=remind)
  except:
    context.bot.send_message(
        chat_id=chat_id, text="Sorry, there is no remind(s) with such id(s) 😔")
