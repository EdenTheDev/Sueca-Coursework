from sueca_cards import *
class Trick:
    def __init__(self, trick):
        self.ts = trick
        return
    def points(self):
        self = self.upper()
        
        return
    def trick_winner(t):
        return
    def show(self):
        return
    
    pass

def parseTrick(ts):
    validCards = ["2H","3H","4H","5H","6H","7H","QH","JH","KH","AH",
                "2C","3C","4C","5C","6C","7C","QC","JC","KC","AC",
                "2S","3S","4S","5S","6S","7S","QS","JS","KS","AS",
                "2D","3D","4D","5D","6D","7D","QD","JD","KD", "AD"]
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
                print(cardList)
                print(temp_ts)
                newInstance = Trick(cardList)
                return newInstance
            else:
                raise ValueError(f"the given string {ts} is invalid")
    else:
        raise ValueError(f"the given string {ts} is invalid")
    
def parseGameFile(fname):
    global trump
    global lead
    cardList = []
    cardListParsed = []
    trickList = []
    with open(fname, "r") as readFile:
        cardList = readFile.read().splitlines()
        lead = cardList[0]
        trump = cardList[-1]
        for x in range(1,10):
            cardListSplit = cardList[x].split()
            
    return

parseTrick("4H 1B 7C 6D")
