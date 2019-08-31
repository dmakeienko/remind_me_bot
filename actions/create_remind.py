from db.database import create

def create_remind(bot, update, args):
    user_chat_id = update.message.chat_id
    try:
        user_message = ' '.join(args).split(" ", 2)
        time_remind = user_message[0] + " " + user_message[1]
        reminder_text = user_message[2] 
        user_chat_id = update.message.chat_id
        remind = "You will get remind about " + reminder_text
        bot.send_message(chat_id=user_chat_id, text=remind)
        create(user_chat_id, time_remind, reminder_text, False)
    except:
        bot.send_message(chat_id=user_chat_id, text='Sorry, can`t create remind.')
