from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.menu import build_menu
from actions.close_remind import close_remind
from actions.postpone import postpone_30

def remind_button_menu(bot, chat_id):
    button_list = [
        InlineKeyboardButton("Mark as done", callback_data='done'),
        InlineKeyboardButton("Postpone for 30 min", callback_data='postpone')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text='What to do with remind?', reply_markup=reply_markup)



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
        close_remind(bot, chat_id)
    elif data == 'postpone':
        postpone_30(bot, chat_id)

    bot.answer_callback_query(update.callback_query.id)