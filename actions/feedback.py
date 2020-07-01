from dotenv import load_dotenv
import os

def feedback(update, context):
    feedback_text = ' '.join(context.args)
    feedback = 'You received feedback from user: ⚠️\n' + feedback_text
    context.bot.send_message(chat_id=os.environ['ADMIN_CHAT_ID'], text=feedback)
    context.bot.send_message(chat_id=update.message.chat_id, text='Thank you for feedback! Here is a 🍩 for you ☺️.')