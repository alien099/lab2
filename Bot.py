import telebot
bot = telebot.TeleBot('5148306588:AAGfvSqpcrNh5HwNZImu8bWTpPeiXCx6lHg')


@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я ПайТон".format(
                         message.from_user))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    bot.send_message(chat_id, text="Я тебя слышу! Ваше сообщение: " + ms_text)


bot.polling(none_stop=True, interval=0)
