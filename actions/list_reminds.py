from db.database import get_reminds
from datetime import datetime
from utils.constants import DATETIME_FORMAT, LIST_ALL_FLAG, LIST_WEEK_FLAG, LIST_ALL_BUTTON, LIST_WEEK_BUTTON, LIST_10_BUTTON, LIST_30_BUTTON
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.menu import build_menu

def list_button_menu(bot, chat_id):
    button_list = [
        InlineKeyboardButton("Last 1️⃣0️⃣", callback_data=LIST_10_BUTTON),
        InlineKeyboardButton("Last 3️⃣0️⃣", callback_data=LIST_30_BUTTON),
        InlineKeyboardButton("Current week 📒", callback_data=LIST_WEEK_BUTTON),
        InlineKeyboardButton("List all 🗂", callback_data=LIST_ALL_BUTTON)
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=3))
    bot.send_message(chat_id=chat_id, text="Want to see more?🤔", reply_markup=reply_markup)



def list_reminds(bot, update, args):
  my_reminds = ''
  user_chat_id = update.message.chat_id
  remind_status = ''
  interval = ''.join(args).lower()
  try:
    for r in get_reminds(user_chat_id, interval):
      if r['expired'] == False:
        remind_status = '🕖'
      elif r['expired'] == True:
        remind_status = '❌'
      if r['done'] == True:
        remind_status = '✅'
      time = datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')
      my_reminds += f"🗓 {r['id']}: ⏰ {time} 📌 {r['remind_text']}: {remind_status}\n"
    bot.send_message(chat_id=update.message.chat_id, text=my_reminds)
    list_button_menu(bot, user_chat_id)
  except:
    if interval == '':
      interval = "today"
    my_reminds = f"Oops 😯, you have no reminds for {interval}."
    bot.send_message(chat_id=update.message.chat_id, text=my_reminds)


def button_list_reminds(bot, user_chat_id, args):
  my_reminds = ''
  remind_status = ''
  interval = ''.join(args).lower()
  try:
    for r in get_reminds(user_chat_id, interval):
      if r['expired'] == False:
        remind_status = '🕖'
      elif r['expired'] == True:
        remind_status = '❌'
      if r['done'] == True:
        remind_status = '✅'
      time = datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')
      my_reminds += f"🗓 {r['id']}: ⏰ {time} 📌 {r['remind_text']}: {remind_status}\n"
    bot.send_message(chat_id=user_chat_id, text=my_reminds)
    list_button_menu(bot, user_chat_id)
  except:
    if interval == '':
      interval = "today"
    my_reminds = f"Oops 😯, you have no reminds for {interval}."
    bot.send_message(chat_id=user_chat_id, text=my_reminds)
