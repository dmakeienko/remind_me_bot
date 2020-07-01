from db.database import get_reminds
from datetime import datetime
from utils.constants import DATETIME_FORMAT, LIST_ALL_FLAG, LIST_WEEK_FLAG, LIST_ALL_BUTTON, LIST_WEEK_BUTTON, LIST_10_BUTTON, LIST_3_BUTTON
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.menu import build_menu


def list_button_menu(update, context):
    chat_id = update.message.chat_id
    keyboard = [
        InlineKeyboardButton("Last 3", callback_data=LIST_10_BUTTON),
        InlineKeyboardButton("Current week", callback_data=LIST_WEEK_BUTTON),
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=chat_id, text="Want to see more?🤔", reply_markup=reply_markup)



def list_reminds(update, context):
  my_reminds = ''
  remind_status = ''
  chat_id = update.message.chat_id
  interval = ''.join(context.args).lower()
  try:
    for r in get_reminds(chat_id, interval):
      if r['expired'] == False:
        remind_status = '🕖'
      elif r['expired'] == True:
        remind_status = '❌'
      if r['done'] == True:
        remind_status = '✅'
      time = datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')
      my_reminds += f"🗓 {r['id']}: ⏰ {time} 📌 {r['remind_text']}: {remind_status}\n"
    context.bot.send_message(chat_id=chat_id, text=my_reminds)
    list_button_menu(context.bot, chat_id)
  except:
    if interval == '':
      interval = "today"
    my_reminds = f"Oops 😯, you have no reminds for {interval}."
    context.bot.send_message(chat_id=chat_id, text=my_reminds)


def button_list_reminds(update, context, flag):
  my_reminds = ''
  remind_status = ''
  chat_id = update.message.chat_id
  interval = ''.join(flag).lower()
  try:
    for r in get_reminds(chat_id, interval):
      if r['expired'] == False:
        remind_status = '🕖'
      elif r['expired'] == True:
        remind_status = '❌'
      if r['done'] == True:
        remind_status = '✅'
      time = datetime.strptime(r['remind_time'], DATETIME_FORMAT).strftime('%d.%m %H:%M')
      my_reminds += f"🗓 {r['id']}: ⏰ {time} 📌 {r['remind_text']}: {remind_status}\n"
    context.bot.send_message(chat_id=chat_id, text=my_reminds)
    list_button_menu(update, context)
  except:
    if interval == '':
      interval = "today"
    my_reminds = f"Oops 😯, you have no reminds for {interval}."
    context.bot.send_message(chat_id=chat_id, text=my_reminds)
