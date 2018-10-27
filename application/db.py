# coding=utf-8
from telebot import util
from application import bot
from model.User import User


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

    cid = message.chat.id
    data = User.get_config(cid)
    place = "none"
    status = "none"
    User.set_config(cid, place, status)
    bot.reply_to(message, "checked out from %s" %data.place)

@bot.message_handler(commands=['request'])
def load(message):
    cid = message.chat.id
    place = "test"
    status = "requesting"
    User.set_config(cid, place, status)



@bot.message_handler(commands=['ntf'])
def notifyFrom(message):
    data = User.get_config(message.chat.id)
    users = User.get_checked_in_at(data.place)

    if len(users) > 0:
        n_users=0
        for user in users:
            cid = user.cid
            bot.send_message(cid, 'un nuevo usuario quiere que le guardes el sitio, aceptas?')
            n_users = n_users + 1
        bot.reply_to(message, "%i usuarios fueron notificados, esperando respuesta"%n_users)
    else:
        bot.reply_to(message, "no hay ningun usuario en la biblioteca")


# dev functions

@bot.message_handler(commands=['list'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    users = User.get_all()

    if len(users)>0:
        for user in users:
            bot.send_message(message.chat.id, "user: %s\n    place: %s\n    status: %s" %(user.cid, user.place, user.status,))
    else:
        bot.reply_to(message, "not users")