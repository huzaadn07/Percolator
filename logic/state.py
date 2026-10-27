
class GameState:
    def __init__(self):
        self.money = 0
        self.currentScore = 0

    def calcHandScore(self, playedCards):
        # Add all card base points
        score = 0
        for card in playedCards:
            score += card.basePoints
        return score