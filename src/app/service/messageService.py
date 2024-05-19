import random


def answer_message(bot, message):
    command = message.text[1:]
    match command:
        case "unknown_message":
            unknown_message(bot, message.chat.id)


def unknown_message(bot, chat_id):
    responce = random.choice(answers["unknown"])
    bot.send_message(chat_id, responce)


answers = {
    "unknown": [
        "😕 К сожалению, данная команда не существует",
        "❓ Извините, я не знаю такой команды",
        "🙁 Команда не распознана. Попробуйте другую"
    ]
}