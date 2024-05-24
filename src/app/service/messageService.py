def extract_words(text):
    symbols = ".,/(){}[]&?!#$@;%:*№''\"\""
    for sym in symbols:
        text = text.replace(sym, " ")
    text = [word.lower() for word in text.split(" ")]
    while "" in text:
        text.remove("")
    return text    


def answer_message(bot, message):
    text = message.text
    words = extract_words(text)
    # todo: сделать проверку, если какое-то слово содержится в базе, то давать ответ. Иначе unknown_message
    unknown_message(bot, message.chat.id)


def unknown_message(bot, chat_id):
    bot.send_message(chat_id, answers["unknown"])


answers = {
    "unknown": "Я ещё не умею общаться на такие темы"
}
