# coding=utf-8
from telebot import util
from application import bot
from model.User import User


def update_user_status(message):
    """
    Guarda un dato en el chat que se puede recuperar después
    """

    data = util.extract_arguments(message.text)
    if not data:
        bot.reply_to(message, "Error del servidor, contacte el administrador github.com/aulasoftwarelibre/my-biblio-place-bot")
        return

    chat_id = message.chat.id
    Chat.set_config(chat_id, 'memory', data)
    bot.reply_to(message, "Dato guardado. Usa /load para recuperar")


@bot.callback_query_handler(func=lambda lib: lib.data in ["BRabanales", "BMedicinaEnfermeria", "BCienciasEducacion", "BDerecho", "BFilosofiaLetras", "BGeneral"])
def checkin(lib):
    uid = lib.from_user.id
    place = lib.data
    status = "checked in"
    User.set_config(uid, place, status)
    bot.reply_to(lib.message, "checked in at %s" % place)
    bot.reply_to(lib.message, "uid %s" % uid)

@bot.message_handler(commands=['checkout'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    uid = message.from_user.id
    data = User.get_config(uid)
    place = data.place
    status = "checked out"
    User.set_config(uid, "", status)
    bot.reply_to(message, "checked out from %s" %place)

@bot.message_handler(commands=['list'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    users = User.get_checked_in_at("test")

    if len(users)>0:
        for user in users:
            uid = user.uid
            bot.reply_to(message, "user: %s" % uid)
    else:
        bot.reply_to(message, "not users in this place")


