import telebot

token = '6974570282:AAEMq1syy4ZAruB2jKZ_db0CH_pxStEdhf0'

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello!")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text == "test":
            bot.send_message(message.chat.id, "test ok")
        elif message.text == "l":
            bot.send_message(message.chat.id, 'в разработке')

    bot.polling()


telegram_bot(token)