from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.menu import build_menu
from actions.close_remind import close_remind

def remind_button_menu(bot, update):
    button_list = [
        InlineKeyboardButton("Mark as done", callback_data='done'),
        InlineKeyboardButton("Postpone for 30 min", callback_data='postpone')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(chat_id=update.message.chat_id, text='What to do with remind?', reply_markup=reply_markup)



def button(bot, update):
    query = update.callback_query
    data = update.callback_query.data
    print('-------------------')
    print(query) 
    print('-------------------')
    print(data)
    print('-------------------')
    if data == 'list':
        print('list button')
    elif data == 'done':
        close_remind(bot, update)
    elif data == 'postpone':
        print('postpone button')

    bot.answer_callback_query(update.callback_query.id)