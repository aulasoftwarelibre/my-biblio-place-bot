# coding=utf-8
from application import bot
from application.boards import getlocation
from model.User import User


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(commands=['checkin'])
def preCheckIn(message):
    data = User.get_config(message.chat.id)
    cid = message.chat.id
    status = data.status
    User.set_config(cid, "none", status,)
    getlocation(message)


@bot.message_handler(commands=['request'])
def preLoad(message):
    data = User.get_config(message.chat.id)
    User.set_config(data.cid, "none", "requesting")
    User.get_config(data.cid)
    print(User.get_config(data.cid).status)
    getlocation(message)