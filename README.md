# Noirina Bot

A telegram bot @noirina_bot

## Motif
Noirina is Magic!
## To do
* A quoting bot with keyword indexing
* A random speech emitter

## Design

### 0. Terms

Noirina: the bot @noirina_bot, that is, this one

### 1. Qb = Quoting bot

#### 1. Use a dictionary(or set) to store messages

##### 1.a Store

###### 1.a.i it is stored as a tuple of (keywords, index, text) called `Quote`

* 'keywords' is the list of keywords associated with the message, assigned on creation.

- 'index' is the unique identifier of a message, comprised of the pair of chatid and messageid.
- 'text' is the content of the message.

###### 1.a.ro All `Quote`'s are stored in `QuoteSet`

* a dictionary(`QuoteSet.msgid_index`) maps the index of a quote to quote itself.
* there is a dictionary(`QuoteSet.inner`) mapping each keyword to a set of quote indices(as in `1.a.i`) which quotes have the specific keyword, note, it is not exclusive, meaning that a quote can appear in multiple sets.

###### 1.a.ha Alternative storage

If a quote is not associated with any keyword, it should be stored in an array, and looked up with its index.

##### 1.b. Lookup

###### 1.b.i When a list of keywords is provided, first find out the intersection of all sets corresponding to the keyword, i.e. $Query = \bigcap_{keyword \in keywords}QuoteSet.Inner[keyword]$

* If the set is empty, return arbitrary response text like "You moron, nobody's talked about that".
* If one or more quotes are present, randomly choose one.

###### 1.b.ro When a nonnegative integer is provided, find out the quote in the array with the index

##### 1.c Interfaces

###### 1.b.i creating new entries

A new quote entry should be created by replying to the quote with keywords specified, there is only one way to do it: reply the message what you want Noirina to store with `\quote@noirina_bot [keywords]`.

* `keywords`: a whitespace-separated list of keywords.
* if no keyword is specified, Noirina should reply with the index of the quote in the array specified in `1.a.ha`.

###### 1.b.ro look up

Noirina should look up in its database and forward the quote which satisfies. There is only one way to evoke this action: send a message(not replying one) with `\quote@noirina_bot [keywords]`.

* `keywords`: as defined in `1.b.i`, note that to quote a sentence, not all of its keywords need to be provided, only one of them will suffice, as demonstrated in `1.b.i`.
* Using `\quote@noirina_bot [number]` to index quotes, however, this will precludes numeric keywords being used.

### 2. RGB=Random Generator of Bullshit

Using LSTM, still under consideration.

