import QuoteSet

QUOTE_FILENAME = """quotes.sav"""

quotewords = QuoteSet.QuoteSet(pickle=QUOTE_FILENAME)

def lookup(bot, update):
    keywords = update.message.text.split(" ")
    bot.send_message(chat_id=update.message.chat_id, text=" ".join(keywords))
