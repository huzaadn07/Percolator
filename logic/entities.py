#libraries
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

      
class Customer:
    def __init__(self, name, targetScore):
        self.name = name
        self.targetScore = targetScore


class Equipment:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def modify_score(self, context): #base function that alters the score of the round, subclass inherits and overwrites this method.
        return context.handScore

# flat multi joker #1
class TipJar(Equipment):
    def __init__(self):
        super().__init__("Tip Jar", "Adds +20 score to your hand when played.")

    def modify_score(self, context):
        return (context.handScore + 20)

