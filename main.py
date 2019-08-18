from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import json
import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
import os
from dotenv import load_dotenv
from db.database import create_remind, get_reminds, expire_remind, check_remind
from schedule.jobs import test


load_dotenv()


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

logger = logging.getLogger(__name__)


TOKEN = os.environ.get("TELEGRAM_TOKEN")

def start(bot, update):
  update.message.reply_text("I'm a bot, Nice to meet you!")
  

def time(bot, update):
  current_time=datetime.datetime.now().strftime('%B %m, %A %H:%M')
  update.message.reply_text(text="It's " + current_time)


def set_remind(bot, update, args):
  user_message = ' '.join(args).split(" ", 2)
  time_remind = user_message[0] + " " + user_message[1]
  reminder_text = user_message[2]
  user_chat_id = update.message.chat_id
  remind = "You will get remind about " + reminder_text
  bot.send_message(chat_id=user_chat_id, text=remind)
  create_remind(user_chat_id, time_remind, reminder_text, False)


def list_reminds(bot, update):
  my_reminds = ''
  user_chat_id = update.message.chat_id
  for r in get_reminds(user_chat_id):
    print(f"id: {r['id']}  {r['remind_text']}")
    my_reminds += f"id: {r['id']}  {r['remind_text']}\n"

  bot.send_message(chat_id=update.message.chat_id, text=my_reminds)



def delete_remind(bot, update, args):
  expire_remind(args)
  bot.send_message(chat_id=update.message.chat_id, text="Your remind has been deleted")


def remind():
  if check_remind:
    for r in check_remind():
      print(f"id: {r['id']}  {r['remind_text']}")
      remind = f"Don`t forget: {r['remind_text']}\n"

  bot.send_message(chat_id=update.message.chat_id, text=remind)


def unknown(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


  

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater(token=TOKEN)
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher

  # Start
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)

  # Remind
  set_remind_handler = CommandHandler('remind', set_remind, pass_args=True)
  dispatcher.add_handler(set_remind_handler)
  
  # Time
  time_handler = CommandHandler('time',time)
  dispatcher.add_handler(time_handler)


  # List
  list_handler = CommandHandler('list', list_reminds)
  dispatcher.add_handler(list_handler)


  # Delete
  delete_handler = CommandHandler('rm', delete_remind, pass_args=True)
  dispatcher.add_handler(delete_handler)


  # Always should be last
  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()


if __name__ == '__main__':
  main()