def help_remind(bot, update):
    text = """
To create remind use:
/remind 10.01 12:00 visit to doctor
To show all reminds for today, use:
/list 
If you want to list all reminds, use:
/list all
To mark remind as 'Done', use
/done - it will close last remind, 
or use:
/done 123, where '123' is id of Remind
To update remind, try to use:
/update 123 01.10 22:00 review schedule
To delete remind, use:
/delete 123, where '123' is id of Remind
    """
    feedback_text="""
If you have any feedback, plese send it to denys.makeienko@gmail.com
or use:
/feedback Here is what is think about your bot
    """
    bot.send_message(chat_id=update.message.chat_id, text=text)
    bot.send_message(chat_id=update.message.chat_id, text=feedback_text)