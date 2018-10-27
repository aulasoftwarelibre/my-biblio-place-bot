# coding=utf-8
from telebot import util
from application import bot
from model.User import User
from application import boards


@bot.message_handler(commands=['checkin'])
def checkin(message):
    """
    Guarda un dato en el chat que se puede recuperar después
    """
    uid = message.from_user.id
    place = "test"
    status = "cheched in"
    record = User.set_config(uid, place, status)
    bot.reply_to(message, "test")


@bot.message_handler(commands=['chechout'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    chat_id = message.chat.id
    data = Chat.get_config(chat_id, 'memory')
    if not data:
        bot.reply_to(message, "Aún no has guardado nada")
        return

    bot.reply_to(message, "Dato recuperado: %s" % data.value)


def update_user_status(userid, place, status):
    """

    """
    if not userid:
        return -1

    # saves the status of the user in the database
    User.set_config(userid, place, status)
    return "Dato guardado correctamente."