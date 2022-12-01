class card:
    def __init__(self, rank, suit):
        self.rank= rank
        self.suit= suit
        
    def points(self):
        self= self.upper()
        
        if self.rank == "Q":
            return "2 Points"
        if self.rank == ""
        
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
    