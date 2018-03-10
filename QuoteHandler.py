import QuoteSet

QUOTE_FILENAME = """quotes.sav"""

quotewords = QuoteSet.QuoteSet(pickle=QUOTE_FILENAME)

def quote(bot, update):
    msg = update.message
    quote = msg.reply_to_message
    keywords = msg.text.split(" ")[1:]
    # filter out empty strings
    keywords = [string for string in keywords if string]
    if quote:
        if keywords:
            if quote.text:
                q = Quote.new(keywords, (msg.chat_id, msg.message_id), quote.text)
                quotewords.add(q)
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
