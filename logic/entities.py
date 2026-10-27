import random

class Card:
    def __init__(self, name, cardType, basePoints):
        self.name = name
        self.cardType = cardType
        self.basePoints = basePoints

    def get_stats(self):
        return f"Card: {self.name}\nCard Type: {self.cardType}\nBase Points: {self.basePoints}"

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, amount):
        drawn = []
        for i in range(amount):
            if self.cards:
                drawn.append(self.cards.pop())
        return drawn

#temp main
"""

newCard = Card("Chocolate", "Sweet", 100)
print(newCard.get_stats())

"""