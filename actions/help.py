def help_remind(bot, update):
    text = """
▫️ To create remind use:
/remind 10.01 12:00 visit a doctor
If remind should be set in upcoming month, please specify year directly:
/remind 10.02.19 12:00 visit a doctor
You can use aliases like /today, /tomorrow, /сегодня, /завтра etc

▫️ To show reminds for today, use:
/list 
If you want to list all reminds, use:
/list all
You can list week reminds (by adding 'week' argument) or last number of reminds:
/list 10

▫️ To mark last active remind as 'Done', use
/done - it will close last remind, 
or use:
/done 123, where '123' is an id of Remind

▫️ You can postpone remind, by using:
/postpone 10 , where 10 - time in minute to snooze
If you want to postpone for hours, you can specify 'h' argument:
/postpone 2 h
Aliases: /postpone, /snooze/, /pp

▫️ To update remind, try to use:
/update 123 01.10 22:00 review schedule

▫️ To delete remind, use:
/delete 123, where '123' is id of Remind
Alias: /rm 123

▫️ You can see changelog and discover source code. To get those links, type:
/about
    """

    feedback_text="""
If you have any feedback, plese send it to denys.makeienko@gmail.com
or use:
/feedback Here is what is think about your bot
    """
    bot.send_message(chat_id=update.message.chat_id, text=text)
    bot.send_message(chat_id=update.message.chat_id, text=feedback_text)