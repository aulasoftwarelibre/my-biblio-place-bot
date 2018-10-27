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
    status = "checked in"
    User.set_config(uid, place, status)
    bot.reply_to(message, "checked in at: %s" %place)


@bot.message_handler(commands=['chechout'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    uid = message.from_user.id
    place = "test"
    status = "checked in"
    User.set_config(uid, place, status)
    bot.reply_to(message, "checked out : %s" % place)