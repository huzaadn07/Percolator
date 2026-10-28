#libraries

#used to make calculating scores easier down the line incase we add new feature
class ScoringContext:
    def __init__(self, currentScore, playedCards, currentMoney):
        self.handScore = currentScore
        self.playedCards = playedCards
        self.currentMoney = currentMoney

class GameState:
    def __init__(self):
        self.money = 0
        self.runningScore = 0
        self.activeEquipment = [] #modifiers thats bought from shop go here

    def add_equipment(self, equipmentItem):
        MAX_EQUIPMENT = 5 #5 active items at a time.
        if (len(self.activeEquipment) < 5):           
            self.activeEquipment.append(equipmentItem)

    #works when hand is played.
    def calc_hand_score(self, playedCards):

        # Add all card points before multis.
        score = 0
        for card in playedCards:
            score += card.basePoints

        context = ScoringContext(score, playedCards, self.money)

        for equipment in self.activeEquipment:
            context.handScore = equipment.modify_score(context)

        return context.handScore