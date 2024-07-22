import collections

Cards = collections.namedtuple('card', ['suit', 'value'])

class FrenchDeck:
    RANKS = [str(n) for n in range(2,11)] + list('JQKA')
    SUITS = "spades diamonds clubs hearts".split()

    def __init__(self):
         self._cards=[Cards(rank,suit) for suit in self.SUITS for rank in self.RANKS]


    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

