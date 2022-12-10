from sueca_tricks import *
class Game:
    def __init__(self, trump):
        self.trump = trump

    def gameTrump(self):
        return(self.trump)
        
    def score(self):
        cards = self.trick.split()
        pair_1 = (cards[0],cards[1])
        pair_2 = (cards[2],cards[3])
        pair_1_points = 0
        pair_2_points = 0
        for card in pair_1:
            pair_1_points += rank_points(card)
        for card in pair_2:
            pair_2_points += rank_points(card)
        return(pair_1_points, pair_2_points)

    def playTrick(self, t):
        return

    def cardsOf(self, p):
        return
    def gameTricks(self):
        return

    tc, ts = parseGameFile('game1.sueca')
    #g = Game(tc)

