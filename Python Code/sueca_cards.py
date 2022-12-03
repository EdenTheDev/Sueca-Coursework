class card:
    def __init__(self, rank, suit):
        self.rank= rank
        self.suit= suit
        
    def points(self):
        self= self.upper()
        if self.rank == "A":
            return "11"
        if self.rank == "7":
            return "10"
        if self.rank == "K":
            return "4"
        if self.rank == "J":
            return "3"
        if self.rank == "Q":
            return "2"
        if self.rank == "8" or "9" or "10":
            return "0"
        else:
            raise CardInvalid(f"Invalid suit symbol {self}")

            
    def higher_than(self, other, s, t):
        if self.suit == other.suit:
            if self.rank > other.rank:
                return True
            else:
                return False

        elif self.suit != other.suit:
            return "different suits"
            
    
    def show(self):
        card =(self.rank+self.suit)
        return card
    
class CardInvalid(Exception):
    pass
       
def parseCard(cs: str):
    cardList = ["2H","3H","4H","5H","6H","7H","QH","JH","KH","AH",
                "2C","3C","4C","5C","6C","7C","QC","JC","KC","AC",
                "2S","3S","4S","5S","6S","7S","QS","JS","KS","AS",
                "2D","3D","4D","5D","6D","7D","QD","JD","KD", "AD"
                ]

    if cs in cardList:
        print("test")
        return card(cs[0],cs[1])
    elif len(cs) != 2:
        raise CardInvalid(f"Invalid card length {cs}")
    else:
        raise CardInvalid(f"Invalid card symbol: {cs}")
    


print(parseCard("KS"))                  