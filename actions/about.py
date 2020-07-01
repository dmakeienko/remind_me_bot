def about(update, context):
    user_chat_id = update.message.chat_id
    with open('VERSION', 'r') as file:
        version = file.read()
    author = 'denys.makeienko@gmail.com'
    source_link = 'https://github.com/dmakeienko/remind_me_bot'
    changelog = 'https://github.com/dmakeienko/remind_me_bot/releases'
    message = f"Current version: {version}\nAuthor is: {author}\nLink to source code: {source_link}\nChangelog: {changelog}"
    context.bot.send_message(chat_id=user_chat_id, text=message)
