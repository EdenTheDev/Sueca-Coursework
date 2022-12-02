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
            return "Invalid card symbol"
            
    def higher_than(self, other, s, t):
        return""
    
    def show(self):
        return""
    
class CardInvalid(Exception):
    pass
       
def parseCard(cs):
    if True:
        print("")
    else:
        raise CardInvalid(f"Invalid card symbol: {cs}")
    