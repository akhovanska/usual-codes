import collections

Card = collections.namedtuple('Card', ['rank', 'suits'])  # card has characters as rank and suit


class Deck: # not changing without __setitem__
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):  # create a new object
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,
                    position):  # to access the indexed instance attributes; returns the value available in the data
        # available to the client
        return self._cards[position]

    #def __setitem__(self): #now we can change cards, positions...
    
