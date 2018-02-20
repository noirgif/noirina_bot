import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import QuoteHandler

TOKEN = open('token.sav').readline()

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)

lookup_handler = CommandHandler('lookup', QuoteHandler.lookup, pass_args=True)

updater.dispatcher.add_handler(lookup_handler)

updater.start_polling()
