import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('6995749681:AAEeJcpEKx71NiSV5c7RIF4rcN5vPxj_0tQ')



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Информация")
    item2 = types.KeyboardButton("Стоп")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Здравствуйте! Выберите действие:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Информация":
        bot.send_message(message.chat.id, "Данный бот сделан студентом ПМИ Семеновым Иваном")
    elif message.text == "Стоп":
        bot.send_message(message.chat.id, "До встречи!")
        bot.stop_bot()

    if message.text == "сосал?":
        bot.send_message(message.chat.id, "сам сосал")
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю")
    


if __name__ == '__main__':
    bot.polling()