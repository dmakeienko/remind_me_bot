from db.database import close

def close_remind(bot, update, args):
  user_chat_id = update.message.chat_id
  try: 
    close(user_chat_id, args)
    # TODO
    # Show id's of closed reminds
    bot.send_message(chat_id=update.message.chat_id, text=f"Your remind marked as Done!✅")
  except:
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, there is no remind(s) with such id(s) 😔")
