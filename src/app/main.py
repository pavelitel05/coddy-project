from telebot import *


file = open("../../res/token.txt")

token = file.readline()

bot = TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True)

