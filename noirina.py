import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import QuoteHandler

TOKEN = open('token.sav').readline().strip()

updater = Updater(token=TOKEN)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

quote_handler = CommandHandler('quote', QuoteHandler.quote)

updater.dispatcher.add_handler(quote_handler)

updater.start_polling()
