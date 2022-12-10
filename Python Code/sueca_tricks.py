from sueca_cards import *
class Trick:
    def __init__(self, trick): #trump
        self.trick = trick
        #self.points = self.points()
        #self.trump = trump

    def points(self):
        trickPoints = 0
        for card in self.trick.split():
            trickPoints += rank_points(card[0])
        return trickPoints

    def trick_winner(self, t):
        cards = self.trick.split()
        winner = 0
        i = 1
        for i in range(1,4):
            if (parseCard(cards[i]).higher_than(parseCard(cards[winner]), "ZZZ", t)):
                winner = i
        return(winner + 1)

    def show(self):
        return self.trick

def parseTrick(ts):

    cardList = ["2H","3H","4H","5H","6H","7H","QH","JH","KH","AH",
                "2C","3C","4C","5C","6C","7C","QC","JC","KC","AC",
                "2S","3S","4S","5S","6S","7S","QS","JS","KS","AS",
                "2D","3D","4D","5D","6D","7D","QD","JD","KD", "AD"
                ]

    # Check if exactly 4 strings of length 2, seperated by 3 spaces, and each string of 2 is a valid card
    for card in ts.split(" "):
        if len(card) != 2 or card not in cardList:
            if not valid_rank(card[0]):
                raise CardInvalid(f"Card {card} is invalid!\nInvalid rank symbol: {card[0]}")
            else:
                raise CardInvalid(f"Card {card} is invalid!\nInvalid suit symbol: {card[1]}")
    if len(ts) != 11 or ts.count(" ") != 3:
        raise ValueError(f"A trick string must comprise four cards only; the given trick is: {ts}")
    trick = Trick(ts)
    return trick

def parseGameFile(fname):
    # Return a pair made up of the parsed trump card (object of Card class) and a list of objects of class Trick
    # Pair = (trump-card, list of tricks)
    trick_list = []
    with open(fname, "r") as file:
        cardList = file.read().splitlines()
        trump = parseCard(cardList.pop(0))
        for line in cardList:
            trick_list.append(parseTrick(line))
    return (trump, trick_list)

