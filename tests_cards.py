from cards import Deck, spades_high
from cards import Card

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = Deck()
print(len(deck))

from random import choice
print(choice(deck))

deck = Deck()
print(deck[12::13])

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)
print(Card('Q', 'bes') in deck)

suits_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suits_value) + suits_value[card.suits]

for card in sorted(deck, key=spades_high):
    print(card)