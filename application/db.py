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


@bot.message_handler(commands=['checkin'])
def checkin(message):
    """
    Guarda un dato en el chat que se puede recuperar después
    """
    cid = message.chat.id
    place = "test"
    status = "checked in"
    User.set_config(cid, place, status)
    bot.reply_to(message, "checked in at %s" %place)
    bot.reply_to(message, "cid %s" %cid)


@bot.message_handler(commands=['checkout'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    cid = message.chat.id
    data = User.get_config(cid)
    place = data.place
    status = "checked out"
    User.set_config(cid, "", status)
    bot.reply_to(message, "checked out from %s" %place)

@bot.message_handler(commands=['list'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    users = User.get_checked_in_at("test")

    if len(users)>0:
        for user in users:
            cid = user.cid
            bot.reply_to(message, "user: %s" %cid)
    else:
        bot.reply_to(message, "not users in this place")


@bot.message_handler(commands=['ntf'])
def notify(message):
    users = User.get_checked_in_at("test")

    if len(users) > 0:
        for user in users:
            cid = user.cid
            bot.send_message(cid, 'you are being notified')
    else:
        bot.reply_to(message, "not users in this place")
