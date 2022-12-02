from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Bot, ReplyKeyboardMarkup

token = '5841478407:AAFFAAILJqbLjPH_gDAJqUmyh34EENdIPkk'
updater = Updater(token=token)
bot = Bot(token=token)


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='hiii, \U0001f525')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup(
        [['Тык', 'айпи'],
         ['который час']
         ],
        one_time_keyboard=True, )
    context.bot.send_message(chat_id=chat.id,
                             text=f'hello, {name}',
                             reply_markup=buttons)


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling()

updater.idle()
