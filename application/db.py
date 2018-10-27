# coding=utf-8
from telebot import util
from application import bot
from model.User import User


@bot.message_handler(commands=['checkin'])
def checkin(message):
    """
    Guarda un dato en el chat que se puede recuperar después
    """
    uid = message.from_user.id
    place = "test"
    status = "checked in"
    User.set_config(uid, place, status)
    bot.reply_to(message, "checked in at %s" %place)
    bot.reply_to(message, "uid %s" %uid)


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


