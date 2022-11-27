from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Bot

token = '5841478407:AAFFAAILJqbLjPH_gDAJqUmyh34EENdIPkk'
updater = Updater(token=token)
bot = Bot(token=token)


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='hiii')


def wake_up(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='hello')


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling(poll_interval=20.2)

updater.idle()
