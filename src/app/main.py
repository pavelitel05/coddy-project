from telebot import *
from service.commandService import answer_command
from service.messageService import answer_message


file = open("../../res/token.txt")
token = file.readline()
bot = TeleBot(token)


@bot.message_handler(content_types=["text"])
def command_handler(message):
    text = message.text
    if text[0] == "/":
        answer_command(bot, message)
    else:
        answer_message(bot, message)


bot.polling(non_stop=True)
