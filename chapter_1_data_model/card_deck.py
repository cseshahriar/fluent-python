""" Card Deck """
import collections

Card = collections.namedtuple('Card', ['rand', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # 2-10JQKA 
    suits = 'Spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card) # y / trye


deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])