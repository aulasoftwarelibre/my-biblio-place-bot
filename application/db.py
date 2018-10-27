# coding=utf-8
from application import bot
from model.User import User
from application.boards import getanswer


@bot.callback_query_handler(func=lambda lib: lib.data in ["BRabanales", "BMedicinaEnfermeria", "BCienciasEducacion", "BDerecho", "BFilosofiaLetras", "BGeneral"])
def checkin(lib):
    uid = lib.message.chat.id
    data = User.get_config(uid)
    if data.status == "requesting":
        place = lib.data
        status = "requesting"
        User.set_config(uid, place, status)
        bot.reply_to(lib.message, "Pedido en %s" % place)
        notifyFrom(lib.message)
    else:
        place = lib.data
        status = "checked in"
        User.set_config(uid, place, status)
        bot.reply_to(lib.message, "Entrado a %s" % place)


@bot.callback_query_handler(func=lambda ans: ans.data)
def userDec(ans):
    if ans.data != "no":
        bot.send_message(ans.data, "Aceptado!")


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
    bot.reply_to(message, "Salido de %s" %data.place)


@bot.message_handler(commands=['ntf'])
def notifyFrom(message):
    data = User.get_config(message.chat.id)
    users = User.get_checked_in_at(data.place)

    if len(users) > 0:
        n_users = 0
        for user in users:
            cid = user.cid
            getanswer(cid, message.chat.id)
            n_users = n_users + 1
        bot.reply_to(message, "%i Usuarios fueron notificados, esperando respuesta" % n_users)
    else:
        bot.reply_to(message, "No hay ningun usuario en la biblioteca")


# dev functions

@bot.message_handler(commands=['list'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    users = User.get_all()

    if len(users) > 0:
        for user in users:
            bot.send_message(message.chat.id, "user: %s\n    place: %s\n    status: %s" % (user.cid, user.place, user.status,))
    else:
        bot.reply_to(message, "not users")
