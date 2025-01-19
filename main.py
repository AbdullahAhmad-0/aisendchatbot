from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = r'BOT Token'
BOT_USERNAME: Final = '@aisendchatbot'

import time
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello!")

def main():
    app = Application.builder().token(TOKEN).proxy('http://proxy.mtproto.co:443').build()


    print('POLLING...')
    app.run_webhook()
    # app.run_polling(poll_interval=1)

if __name__ == '__main__':
    main()
