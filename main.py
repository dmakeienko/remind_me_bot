from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import json
import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
import os
from os.path import join, dirname
from dotenv import load_dotenv


# Dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)


TOKEN = os.environ.get("TELEGRAM_TOKEN")

def start(bot, update):
  update.message.reply_text("I'm a bot, Nice to meet you!")
  
def convert_uppercase(bot, update):
  update.message.reply_text(update.message.text.upper())


def time(bot, update):
  current_time=datetime.datetime.now().strftime('%B %m, %A %H:%M')
  update.message.reply_text(text="It's " + current_time)


def get_remind(bot, update):
  user_message = bot.send_message(chat_id=update.message.chat_id, text=update.message.text).split()
  day_remind = user_message[0]
  time_remind = user_message[1]
  reminder_text = user_message[2]
  remind = "You will get remind about " + reminder_text + " at " + day_remind + time_remind
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
  get_remind_handler = MessageHandler(Filters.text, get_remind)
  dispatcher.add_handler(get_remind_handler)
  
  # Time
  time_handler = CommandHandler('time',time)
  dispatcher.add_handler(time_handler)

  # Always should be last
  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()


if __name__ == '__main__':
  main()