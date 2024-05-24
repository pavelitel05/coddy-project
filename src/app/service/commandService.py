def answer_command(bot, message):
    command = message.text[1:]
    match command:
        case "start":
            start(bot, message.chat.id)
            return
    unknown_command(bot, message.chat.id)


def start(bot, chat_id):
    bot.send_message(chat_id, answers["start"])


def unknown_command(bot, chat_id):
    bot.send_message(chat_id, answers["unknown"])


answers = {
    "start": """
    🤘 Приветствуем в coddy-chat-bot-е!
    
👀 Это выпускной проект по курсу Python: telegram bots
    """,
    "unknown": """
     к сожелению данная комманда не существует
    """
}

