class Quote:
    """Quote class.

    Members:
    keywords: a list of keywords associated with the quote
    idx: a tuple of (chat id, message id) of the quote
    text: content of the message, only used if the original message is deleted"""
    def __init__(self, keywords, idx, text):
        self.keywords = keywords
        # to-do: make idx independent
        self.idx = idx
        self.text = text

    def __hash__(self):
        # The message is determined by its id
        return hash((self.keywords, self.idx))

    @staticmethod
    def new(keywords, idx, text=""):
        """Make a new Quote instance, return the instance on success

        Parameters:
        keywords, idx, text: refer to Quote"""
        # check if the keyword list is valid
        if isinstance(keywords, list) and keywords and isinstance(idx, tuple):
            return Quote(keywords, idx, text)
        else:
            return None

    @property
    def text(self):
        return self.text
    
    @property
    def keywords(self):
        return self.keywords

    @property
    def index(self):
        return {'chat_id': self.idx[0], 'message_id': self.idx[1]}
