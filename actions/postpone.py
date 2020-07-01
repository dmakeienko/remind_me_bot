from db.database import _update_time, _get_last_remind
from datetime import datetime, timedelta
from utils.constants import DATETIME_FORMAT, HOUR

def postpone(update, context):
    chat_id = update.effective_chat.id
    user_message = ' '.join(context.args).split(" ")
    postpone_timedelta = user_message[0]
    postpone_time = 0
    try:
        if len(user_message) > 1:
            postpone_format = user_message[1]
        else:
            postpone_format = 'm'

        if postpone_format.lower() == 'h':
            postpone_time = int(postpone_timedelta) * HOUR
        elif postpone_format.lower() == 'm':
            postpone_time = int(postpone_timedelta)

        remind_id = _get_last_remind(chat_id)['id']
        old_time = _get_last_remind(chat_id)['remind_time']
        new_time = (datetime.strptime(old_time, DATETIME_FORMAT) + timedelta(minutes=postpone_time)).strftime(DATETIME_FORMAT)
        _update_time(chat_id, remind_id, new_time)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"📌 Remind postponed for {str(timedelta(minutes=postpone_time))}")
    except ValueError:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"Oops 😯, you forgot to specify postpone time!")
    except TypeError: 
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"Sorry, there is no active remind to postpone😔")


def postpone_30(update, context):
    postpone_timedelta = '30'
    postpone_time = 0
    chat_id = update.effective_chat.id
    try:
        postpone_format = 'm'
        if postpone_format.lower() == 'h':
            postpone_time = int(postpone_timedelta) * HOUR
        elif postpone_format.lower() == 'm':
            postpone_time = int(postpone_timedelta)

        remind_id = _get_last_remind(chat_id)['id']
        old_time = _get_last_remind(chat_id)['remind_time']
        new_time = (datetime.strptime(old_time, DATETIME_FORMAT) + timedelta(minutes=postpone_time)).strftime(DATETIME_FORMAT)
        _update_time(chat_id, remind_id, new_time)
        context.bot.send_message(
            chat_id=chat_id, text=f"📌 Remind postponed for {str(timedelta(minutes=postpone_time))}")
    except ValueError:
        context.bot.send_message(
            chat_id=chat_id, text=f"Oops 😯, you forgot to specify postpone time!")
    except TypeError: 
        context.bot.send_message(
            chat_id=chat_id, text=f"Sorry, there is no active remind to postpone😔")


def postpone_1h(update, context):
    chat_id = update.effective_chat.id
    postpone_timedelta = '1'
    postpone_time = 0
    try:
        postpone_format = 'h'
        if postpone_format.lower() == 'h':
            postpone_time = int(postpone_timedelta) * HOUR
        elif postpone_format.lower() == 'm':
            postpone_time = int(postpone_timedelta)

        remind_id = _get_last_remind(chat_id)['id']
        old_time = _get_last_remind(chat_id)['remind_time']
        new_time = (datetime.strptime(old_time, DATETIME_FORMAT) + timedelta(minutes=postpone_time)).strftime(DATETIME_FORMAT)
        _update_time(chat_id, remind_id, new_time)
        context.bot.send_message(
            chat_id=chat_id, text=f"📌 Remind postponed for {str(timedelta(minutes=postpone_time))}")
    except ValueError:
        context.bot.send_message(
            chat_id=chat_id, text=f"Oops 😯, you forgot to specify postpone time!")
    except TypeError: 
        context.bot.send_message(
            chat_id=chat_id, text=f"Sorry, there is no active remind to postpone😔")
