import os
from telegram.ext import Updater,CommandHandler


def start(update,context):
    update.message.reply_text("Hola Humano")

if __name__ == '__main__':
    updater = Updater(token='2002499736:AAGWNSHuicZLJKe5Az1h6fgEHUtJ__MvxEI', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    print('Bot is polling')
    updater.idle()