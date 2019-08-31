from db.database import get_reminds

def list_reminds(bot, update):
  my_reminds = ''
  user_chat_id = update.message.chat_id
  if get_reminds(user_chat_id):
    for r in get_reminds(user_chat_id):
      my_reminds += f"id: {r['id']}  {r['remind_text']}\n"
  else: 
    my_reminds = 'Sorry, you have no reminds yet'

  bot.send_message(chat_id=update.message.chat_id, text=my_reminds)