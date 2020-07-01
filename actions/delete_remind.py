from db.database import delete

def delete_remind(update, context):
  user_chat_id = update.message.chat_id
  if context.args:
    try:
      delete(context.args, user_chat_id)
      context.bot.send_message(
          chat_id=update.message.chat_id, text="Your remind(s) has been deleted ☑️")
    except:
      context.bot.send_message(chat_id=update.message.chat_id,
                              text="Sorry, there is no remind(s) with such id 😔")
  elif not context.args:
    context.bot.send_message(chat_id=update.message.chat_id,
                            text="Oops 😯, you forgot to specify id(s). Please, try again.")
  
