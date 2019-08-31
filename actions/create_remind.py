from db.database import create

def create_remind(bot, update, args):
    user_chat_id = update.message.chat_id
    try:
        user_message = ' '.join(args).split(" ", 2)
        time_remind = user_message[0] + " " + user_message[1]
        reminder_text = user_message[2] 
        remind = "Your remind 📆 has been set!"
        create(user_chat_id, time_remind, reminder_text, False)
        bot.send_message(chat_id=user_chat_id, text=remind)
    except IndexError:
        bot.send_message(chat_id=user_chat_id, text='Oops 😯, can`t create remind. Maybe you missing your text 🤔')
    except ValueError:
        bot.send_message(chat_id=user_chat_id, text='Oops 😯, can`t create remind. Maybe something wrong with date/time? 🤔')