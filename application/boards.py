from telebot import types
from application import bot


def getlocation(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)

    itembtn1 = types.KeyboardButton('Biblioteca Rabanales')
    itembtn2 = types.KeyboardButton('Biblioteca Medicina')

    markup.add(itembtn1, itembtn2)

    bot.send_message(message.chat.id, "¿En que biblioteca?", reply_markup=markup)