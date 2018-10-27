# coding=utf-8
from application import bot
from application.boards import getlocation


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(commands=['checkin'])
def preCheckIn(message):
    getlocation(message)





