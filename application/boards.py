from telebot import types
from application import bot


def getlocation(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    keyboard.add(types.InlineKeyboardButton("Rabanales", callback_data="BRabanales"),
                 types.InlineKeyboardButton("Medicina y Enfermeria", callback_data="BMedicinaEnfermeria"),
                 types.InlineKeyboardButton("Ciencias de la Educacion", callback_data="BCienciasEducacion"),
                 types.InlineKeyboardButton("Derecho", callback_data="BDerecho"),
                 types.InlineKeyboardButton("Filosofia y Letras", callback_data="BFilosofiaLetras"),
                 types.InlineKeyboardButton("General", callback_data="BGeneral")
    )

    bot.send_message(message.chat.id, "¿En que biblioteca?", reply_markup=keyboard)