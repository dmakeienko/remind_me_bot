from db.database import check_remind
from utils.constants import EXPIRED_REMIND_TIME, SECOND_REMIND_TIME, THIRD_REMIND_TIME
from actions.menu import remind_button_menu

def remind(context):
  if check_remind():
    for r in check_remind():
      remind = f"📌Remind ❗️{r['remind_text']}\n"
      user_chat_id = r['chat_id']

    context.bot.send_message(chat_id=user_chat_id, text=remind)
    remind_button_menu(context.bot, user_chat_id)
  else:
    return


def remind_1(context):
  try:
    check_remind(SECOND_REMIND_TIME)
    for r in check_remind(SECOND_REMIND_TIME):
      remind = f"📌Remind ‼️{r['remind_text']}\n"
      user_chat_id = r['chat_id']

    context.bot.send_message(chat_id=user_chat_id, text=remind, )
    remind_button_menu(context.bot, user_chat_id)
  except:
    return

def remind_2(context):
  try:
    check_remind(THIRD_REMIND_TIME)
    for r in check_remind(THIRD_REMIND_TIME):
      remind = f"📌Remind ⁉️{r['remind_text']}\n"
      user_chat_id = r['chat_id']

    context.bot.send_message(chat_id=user_chat_id, text=remind)
    remind_button_menu(context.bot, user_chat_id)
  except:
    return


def check_expired(context):
    try:
      for r in check_remind(EXPIRED_REMIND_TIME)[1]:
        if check_remind(EXPIRED_REMIND_TIME)[0] == 'expired':
          user_chat_id = r['chat_id']
          final_remind= f"Looks like you forgot about your task ({r['id']}): \"{r['remind_text']}\" 💔\nIt's expired now ❌."
          context.bot.send_message(chat_id=user_chat_id, text=final_remind)
    except:
      return