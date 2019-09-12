from actions.about import about
from actions.close_remind import close_remind
from actions.create_remind import create_remind, create_tomorrow, create_today
from actions.delete_remind import delete_remind
from actions.list_reminds import list_reminds
from actions.remind import remind, remind_1, remind_2, check_expired
from actions.start import start
from actions.postpone import postpone
from actions.unknown import unknown
from actions.update_remind import update_remind
from actions.feedback import feedback
from actions.help import help_remind
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
  # Add command handler to dispatcher

  # Start
  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)

  # Create Remind
  create_remind_handler = CommandHandler('remind', create_remind, pass_args=True)
  dispatcher.add_handler(create_remind_handler)
  
  # Create Remind for today
  create_remind_today_handler = CommandHandler(['today', 'ty', 'at' 'сегодня', 'cьогодні'], create_today, pass_args=True)
  dispatcher.add_handler(create_remind_today_handler)

  # Create Remind for tomorrow
  create_remind_tomorrow_handler = CommandHandler(['tomorrow', 'tw', 'завтра'], create_tomorrow, pass_args=True)
  dispatcher.add_handler(create_remind_tomorrow_handler)

  # List
  list_handler = CommandHandler('list', list_reminds, pass_args=True)
  dispatcher.add_handler(list_handler)

  # Jobs
  j.run_repeating(remind, interval=60,  first=0)
  j.run_repeating(remind_1, interval=60,  first=0)
  j.run_repeating(remind_2, interval=60,  first=0)
  j.run_repeating(check_expired, interval=60,  first=0)
  
  # Delete
  delete_handler = CommandHandler(['delete', 'rm'], delete_remind, pass_args=True)
  dispatcher.add_handler(delete_handler)

  # Done
  done_handler =  CommandHandler('done', close_remind, pass_args=True)
  dispatcher.add_handler(done_handler)

  # Update
  update_remind_handler = CommandHandler('update', update_remind, pass_args=True)
  dispatcher.add_handler(update_remind_handler)

  # Update
  postpone_remind_handler = CommandHandler('postpone', postpone, pass_args=True)
  dispatcher.add_handler(postpone_remind_handler)

  # Feedback
  feedback_remind_handler = CommandHandler('feedback', feedback, pass_args=True)
  dispatcher.add_handler(feedback_remind_handler)
  
  # Help
  help_remind_handler = CommandHandler('help', help_remind)
  dispatcher.add_handler(help_remind_handler)
  
  # Help
  about_remind_handler = CommandHandler('about', about)
  dispatcher.add_handler(about_remind_handler)

  # Always should be last
  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()


if __name__ == '__main__':
  main()