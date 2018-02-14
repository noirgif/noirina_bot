class Quote:
    """Quote class.

    Members:
    keywords: a list of keywords associated with the quote
    idx: a tuple of (channel id, message id) of the quote
    text: content of the message, only used if the original message is deleted"""
    def __init__(self, keywords, idx, text):
        self.keywords = keywords
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


class QuoteSet:
    """Set of Quotes indexed by its keywords, provides adding, removing and searching operations

    Members:
    inner: mapping from keyword to a set of idxs
    msgid_index: mapping from msgid to the quote itself"""
    def __init__(self, **kwargs):
        inner = {}
        msgid_index = {}
        if "pickle" in kwargs:
            try:
                import pickle
                file = open(kwargs["pickle"], "rb")
                other = pickle.load(file)
                file.close()
                inner, msgid_index = other.inner, other.msgid_index
            except ImportError:
                print("Pickle not installed, using empty set")
            except FileNotFoundError:
                print("Save not found, using empty set")
        self.inner = inner
        self.msgid_index = msgid_index

    def save(self, **kwargs):
        """save the set to a file"""
        if "pickle" in kwargs:
            try:
                import pickle
                file = open(kwargs["pickle"], "wb")
                pickle.dump(self, file)
                file.close()
            except ImportError:
                print("Pickle not installed")

    def add(self, quote):
        """Add a quote to the set"""
        self.msgid_index[quote.idx] = quote
        for keyword in quote.keywords:
            if keyword in self.inner:
                self.inner[keyword].add(quote.idx)
            else:
                self.inner[keyword] = set([quote.idx])

    def _remove(self, quote):
        """remove a quote from the database"""
        for keyword in quote.keywords:
            self.inner[keyword].discard(quote.idx)
            # clean up the empty list
            if not self.inner[keyword]:
                self.inner.pop(keyword)

    def remove(self, **kwargs):
        """Removing the quote, by providing either a quote or a idx"""
        quote = None
        if "quote" in kwargs:
            quote = kwargs["quote"]
        elif "idx" in kwargs:
            quote = self.msgid_index[kwargs["idx"]]
        if quote:
            self._remove(quote)
            self.msgid_index.pop(quote.idx)

    def search(self, keywords):
        """Search the quote by the keywords given
        return a set of quotes that satisfy"""
        if not keywords:
            return set()
        if any([keyword not in self.inner for keyword in keywords]):
            return set()
        search_range = self.inner[keywords[0]]
        length = len(keywords)
        for i in range(1, length):
            search_range = search_range.intersection(self.inner[keywords[i]])
        return search_range
