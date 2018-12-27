from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import logging


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = ""
TIME=datetime.datetime.now().time()

def start(bot, update):
  update.message.reply_text("I'm a bot, Nice to meet you!")
  
def convert_uppercase(bot, update):
  update.message.reply_text(update.message.text.upper())


def time(bot, update):
  update.message.reply_text(TIME)


def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater(TOKEN)
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  upper_case = MessageHandler(Filters.text, convert_uppercase)
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(upper_case)

  time_handler = CommandHandler('time',time)
  dispatcher.add_handler(time_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()


if __name__ == '__main__':
  main()