from sueca_cards import *
class Trick:
    def __init__(self, trick): #trump
        self.trick = trick
        #self.trump = trump

    def points(self):
        trickPoints = 0
        for card in self.trick:
                trickPoints+= rank_points(card.show()[0])
        print(trickPoints)
        
    def trick_winner(self, t):
        list = []
        trump = t
        player1 = self.trick[0] 
        print(player1)
        player2 = self.trick[1]
        print(player2)
        player3 = self.trick[2]
        print(player3)
        player4 = self.trick[3]
        print(player4)
        print(self.trick)
        playerCounter = 0
        #lead_suit = self.trick[0][1]
        #lead_rank = self.trick[0][0]
        lead_card = self.trick[0].show()
        for card in self.trick:
            if card.show()[1] == t and rank_points(card.show()[0]) > rank_points(lead_card[0]):
                return (playerCounter + 1)
           # elif card[1] == lead_suit and rank_points(str(card[0])) > rank_points(str(lead_rank)):
        playercounter += 1
        #matching = [s for s in list if any("S" in s for list in trump)]
        #winning_card = self.trick[0]
        #for card in self.trick:
         #   if card[-1] == t:
          #      winning_card = card
           #     break
            #elif card[-1] == winning_card[-1] and int(card[:-1]) > int(winning_card[:-1]):
             #   winning_card = card
#
 #       return trick.index(winning_card) + 1

    def show(self):
        #print(self.trick)
        print(self.trick[0].show(), self.trick[1].show(), self.trick[2].show(), self.trick[3].show())
    

def parseTrick(ts):
    validCards = [  "2H","3H","4H","5H","6H","7H","QH","JH","KH","AH",
                    "2C","3C","4C","5C","6C","7C","QC","JC","KC","AC",
                    "2S","3S","4S","5S","6S","7S","QS","JS","KS","AS",
                    "2D","3D","4D","5D","6D","7D","QD","JD","KD", "AD"
                 ]
    cardList = []
    temp_ts = ts.split()
    if len(temp_ts) == 4:
        
        """the trick is 4 elements"""
        for x in temp_ts:
            if x in validCards:
                """all elements in temp_ts are valid"""
                for i in temp_ts:
                    add = parseCard(i)
                    cardList.append(add) 
                newInstance = Trick(cardList)
                return newInstance
            else:
                raise ValueError(f"the given string {ts} is invalid")
    else:
        raise ValueError(f"the given string {ts} is invalid")
    
def parseGameFile(fname):
    cardList = []
    trickList = []
    listA = []
    with open(fname, "r") as file:
        cardList = file.read().splitlines()
        trump = cardList.pop(0)
        finalList = cardList[:]
        for line in finalList:
            for each in line.split():
                add = parseCard(each)
                listA.append(add)
                trickList.append(Trick(listA))
            listA = []
    trumpInstance = parseCard(trump)
    #print(trickList)
    return (trumpInstance, trickList)
#parseTrick("AH 2D 5H KH").points()
#tc, ts = parseGameFile("game1.sueca")
#for each in ts:
 #   print(each)
#tc.show()
#ts[0].show()
#ts[2].show()
#ts[-1].show()
#parseTrick("AH 2D 5H 2H").show()
#parseTrick("AH 2D 5H 2H").points()
#parseGameFile("game1.sueca")
#parseTrick("AS 2S 7S JS").show()
#parseTrick("AS 2S 7S JS").points()
parseTrick("AH 2D 5H 2H").trick_winner("D")
