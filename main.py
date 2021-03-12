import telebot
from settings import TOKEN

bot = telebot.TeleBot(TOKEN);

@bot.message_handler(content_types=["text"])
def kompot(message):
    #bot.send_message(message.chat.id, message.text)
    if message.text == "Дурак":
        bot.send_message(message.from_user.id, "Сам такой!")
    else : bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True, interval=0)
