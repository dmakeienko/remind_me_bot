from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.menu import build_menu
from actions.close_remind import close_remind_button
from actions.postpone import postpone_30, postpone_1h

def remind_button_menu(bot, chat_id):
    button_list = [
        InlineKeyboardButton("Postpone for 30 min 🕟", callback_data='postpone_30m'),
        InlineKeyboardButton("Postpone for 1 hour 🕕", callback_data='postpone_1h'),
        InlineKeyboardButton("Mark as done ✅", callback_data='done')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text="What should I do with remind?🤔", reply_markup=reply_markup)



def button(bot, update):
    query = update.callback_query
    data = update.callback_query.data
    print('---qury----------------')
    print(query) 
    print('-------data------------')
    print(data)
    print('-------------------')
    chat_id = query.message.chat.id
    print('chat_id= ' + str(chat_id))
    if data == 'list':
        print('list button')
    elif data == 'done':
        close_remind_button(bot, chat_id)
    elif data == 'postpone_30m':
        postpone_30(bot, chat_id)
    elif data == 'postpone_1h':
        postpone_1h(bot, chat_id)

    bot.answer_callback_query(update.callback_query.id)