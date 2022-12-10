class ValueError(Exception):
    pass        

def valid_suit(s):
    validSuits = ["H", "C", "S", "D"]
    if s in validSuits:
        return True
    else:
        return False
def valid_rank(r):
    validRanks = ["A", "2", "3", "4", "5", "6", "7", "Q", "J", "K"]
    if r in validRanks:
        return True
    else:
        return False

def suit_full_name(s):
    nameDict ={"H": "Hearts",
               "C": "Clubs",
               "S": "Spades",
               "D": "Diamonds"
                }
    if s in nameDict:
        return nameDict[s]
    else:
        raise ValueError(f"Invalid suit symbol: {s}")
def rank_points(r):
    pointsDict = {
                "A": 11,
                "7": 10,
                "K": 4,
                "J": 3,
                "Q": 2,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0
                }
    if r in pointsDict:
        return(pointsDict[r])
    else:
        raise ValueError(f"Invalid rank symbol: {r}") 

def rank_higher_than(r1,r2):
    rankDict = {"A": 11,
                "7": 10,
                "K": 9,
                "J": 8,
                "Q": 7,
                "6": 6,
                "5": 5,
                "4": 4,
                "3": 3,
                "2": 2
                }
    #print(rankDict[r1])
    #print(rankDict[r2])
    if r1 not in rankDict:
        raise ValueError(f"Invalid rank symbol: {r1}") 
    if r2 not in rankDict:
        raise ValueError(f"Invalid rank symbol: {r2}") 
    if r1 and r2 in rankDict:
        if rankDict[r1] > rankDict[r2]:
            return True
        elif rankDict[r1] < rankDict[r2]:
            return False
        elif rankDict[r1] == rankDict[r2]:
            return False    
#print(rank_higher_than("K", "J"))