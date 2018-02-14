import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import QuoteHandler

token = open('token.sav').readline()

bot = telegram.Bot(token=)
updater = Updater(token=)

lookup_handler = CommandHandler('lookup', QuoteHandler.lookup, pass_args=True)

updater.dispatcher.add_handler(lookup_handler)

updater.start_polling()
