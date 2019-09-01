from dotenv import load_dotenv
import os

def feedback(bot, update, args):
    feedback = ''.join(args)
    bot.send_message(chat_id=os.environ['ADMIN_CHAT_ID'], text=feedback)