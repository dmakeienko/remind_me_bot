from actions.close_remind import close_remind
from actions.create_remind import create_remind
from actions.delete_remind import delete_remind
from actions.list_reminds import list_reminds
from actions.remind import remind, remind_1, remind_2, check_expired
from actions.start import start
from actions.unknown import unknown
from actions.update_remind import update_remind
from dotenv import load_dotenv
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import json
import logging
import os


load_dotenv()


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = os.environ.get("TELEGRAM_TOKEN")


def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater(token=TOKEN)
  j = updater.job_queue
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher

  # Start
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)

  # Remind
  set_remind_handler = CommandHandler('remind', create_remind, pass_args=True)
  dispatcher.add_handler(set_remind_handler)
  
  # List
  list_handler = CommandHandler('list', list_reminds)
  dispatcher.add_handler(list_handler)

  # Remind
  j.run_repeating(remind, interval=60,  first=0)
  j.run_repeating(remind_1, interval=60,  first=0)
  j.run_repeating(remind_2, interval=60,  first=0)
  j.run_repeating(check_expired, interval=60,  first=0)
  
  # Delete
  delete_handler = CommandHandler('rm', delete_remind, pass_args=True)
  dispatcher.add_handler(delete_handler)

  # Done
  done_handler =  CommandHandler('done', close_remind, pass_args=True)
  dispatcher.add_handler(done_handler)

  # Update
  update_remind_handler = CommandHandler('update', update_remind, pass_args=True)
  dispatcher.add_handler(update_remind_handler)

  # Always should be last
  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()


if __name__ == '__main__':
  main()