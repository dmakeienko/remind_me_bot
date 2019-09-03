from dotenv import load_dotenv
import os

def feedback(bot, update, args):
    feedback_text = ' '.join(args)
    feedback = 'You received feedback from user: ⚠️\n' + feedback_text
    bot.send_message(chat_id=os.environ['ADMIN_CHAT_ID'], text=feedback)
    bot.send_message(chat_id=update.message.chat_id, text='Thank you for feedback! Here is a 🍩 for you ☺️.')