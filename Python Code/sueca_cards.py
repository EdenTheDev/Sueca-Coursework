from sueca_suit_ranks import *

class CardInvalid(Exception):
    pass
       
def parseCard(cs: str):
    cardList = ["2H","3H","4H","5H","6H","7H","QH","JH","KH","AH",
                "2C","3C","4C","5C","6C","7C","QC","JC","KC","AC",
                "2S","3S","4S","5S","6S","7S","QS","JS","KS","AS",
                "2D","3D","4D","5D","6D","7D","QD","JD","KD", "AD"
                ]

    if cs in cardList:
        new = Card(cs[0], cs[1])
        return new
    elif len(cs) != 2:
        raise CardInvalid(f"Card {cs} is invalid! \n A card string representation must contain 2 characters only")
    else:
        raise CardInvalid(f"Invalid card symbol: {cs[0]}")
    
class Card:
    rank: str
    suit: str
    def __init__(self, rank, suit): 
        """initialize class with attributes rank and suit"""
        self.rank= rank
        self.suit= suit
        
    def points(self): 
        if rank_points(self.show()) == 0:
            print(self.rank+self.suit)
        elif valid_rank(self.show()) == False:
            raise CardInvalid(f"Invalid suit symbol {self}") #run custom exception error from class CardInvalid
        else:
            print(rank_points(self))
        
       
             

    def higher_than(self, other, s, t):        
        if self.suit == other.suit:
            """compare the points returned from each instance"""
            if self.points() > other.points():
                return True
            elif self.points() < other.points():
                return False
            else:
                """cards must be same so this is an impossible instance"""
                return CardInvalid(f"Invalid card symbol each card must be unique ({self} : {other} are the same)")

        elif self.suit != other.suit: #different suits
            """suit are different""" 
            if self.suit == s:
                """this is a lead suit card"""
                if self.points() > s.points():
                    return True
                else:
                    """this is a lead suit but the rank is too low to win"""
                    return False
        elif self.suit == t: #this is the trump card
            """this is the trump card it is stronger than any other card and wins"""
            return True 
        
        else:
            return CardInvalid(f"Invalid card type {self}")
    
    def show(self):
        currentCard =(self.rank+self.suit)
        print(currentCard)
        return currentCard



#KS = parseCard("KS")
#JS = parseCard("JS")
# print(KS.points())
# print(KS.higher_than(JS, "S", "D"))
#parseCard("2C").show()
#parseCard("8C").show()
#parseCard("QSD").show()
#parseCard("2C").points()