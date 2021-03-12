import telebot


bot = telebot.TeleBot('1686914993:AAEeko2Oy-yo5qOJcmgQAq3jlg3Krc_boTA');

@bot.message_handler(content_types=["text"])
def kompot(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True, interval=0)