# coding=utf-8
from application import bot
from model.users import User


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


# 
@bot.message_handler(commands=['chechin'])
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


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    """
    Hace un 'eco' de lo que se recibe y no se ha procesado en algún comando anterior.
    :param message:
    :return:
    """
    bot.reply_to(message, message.text)
