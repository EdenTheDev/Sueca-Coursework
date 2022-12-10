from sueca_suits_ranks import *

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
        raise CardInvalid(f"Card {cs} is invalid!\n Invalid rank symbol: {cs[0]}")
    
class Card:
    rank: str
    suit: str
    def __init__(self, rank, suit): 
        """initialize class with attributes rank and suit"""
        self.rank= rank
        self.suit= suit
        
    def points(self): 
        return rank_points(self.rank)
        
    def higher_than(self, other, s, t):
        if self.suit == t:
            return True
        elif other.suit == t:
            return False
        if self.suit == s and other.suit == s:
            return rank_higher_than(self.rank, other.rank)
               
        elif self.suit != s and self.suit != t and other.suit == s:
            return False
        
        elif self.suit == s and other.suit != s:
            return True
        elif self.suit != s and self.suit != t and other.suit != s and other.suit != t:
            return rank_higher_than(self.rank, other.rank)
        #    if rank_higher_than(self.rank, other.rank):
         #       return True
          #  else:
           #     return False
    
    def show(self):
        return(self.rank+self.suit)

#parseCard("2C").show()
#parseCard("8C").show()
#parseCard("QSD").show()
#parseCard("7S").points()
#parseCard("KS").points()

#print(parseCard("2C").show())
#parseCard("7H").higher_than(parseCard("2C"), "C", "D")

#print (parseCard("7S").higher_than(parseCard("2C"), "C", "D"))
