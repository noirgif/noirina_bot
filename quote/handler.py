import quoteset
import random

# to-do: replace it with a database, and not store it in pwd
QUOTE_FILENAME = """quotes.sav"""

quotewords = quoteset.QuoteSet(pickle=QUOTE_FILENAME)

def handler(bot, update, args):
    msg = update.message
    quote = msg.reply_to_message
    keywords = args
    if quote:
        if keywords:
            if quote.text:
                quotewords.emplace(keywords, (msg.chat_id, msg.message_id), quote.text)
            else:
                bot.send_message(chat_id=msg.chat_id, text="Quote an empty line? Why bother?")
        else: # reply with no keywords
            bot.send_message(chat_id=msg.chat_id, text="Use /randquote if you want no keyword to be assigned?")
    else:
        # randomly choose one if there are alternatives
        idx = random.choice(quotewords.search(keywords))
        quote = quotewords.msgid_index[idx]
        if quote: # found something 
            bot.forward_message(chat_id=msg.chat_id, from_chat_id=quote.idx[0], message_id=quote.idx[1])
        else:
            bot.send_message(chat_id=msg.chat_id, text="Want me to say something? No way!")
