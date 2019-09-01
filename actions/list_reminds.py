from db.database import get_reminds
from datetime import datetime
from utils.constants import DATETIME_FORMAT

def list_reminds(bot, update):
  my_reminds = ''
  user_chat_id = update.message.chat_id
  remind_status = ''
  if get_reminds(user_chat_id):
    for r in get_reminds(user_chat_id):
      if r['expired'] == False:
        remind_status = '🕖'
      elif r['expired'] == True:
        remind_status = '❌'
      elif r['done'] == True:
        remind_status = '✅'
      time = datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')
      my_reminds += f"🗓 {r['id']}: ⏰ {time} 📌 {r['remind_text']}: {remind_status}\n"
  else: 
    my_reminds = 'Oops 😯, you have no reminds yet.'

  bot.send_message(chat_id=update.message.chat_id, text=my_reminds)