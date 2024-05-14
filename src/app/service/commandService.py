def answer_command(bot, message):
    command = message.text[1:]
    match command:
        case "start":
            start(bot, message.chat.id)


def start(bot, chat_id):
    bot.send_message(chat_id, answers["start"])


answers = {
    "start": """
    🤘 Приветствуем в coddy-chat-bot-е!
    
👀 Это выпускной проект по курсу Python: telegram bots
    """
}

