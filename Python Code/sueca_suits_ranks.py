class ValueError(Exception):
    pass        

def valid_suit(s):
    s=s.upper()
    validSuits = ["H", "C", "S", "D"]
    if s in validSuits:
        print(True)
    else:
        print(False)
def valid_rank(r):
    r=r.upper()
    validRanks = ["A", "2", "3", "4", "5", "6", "7", "Q", "J", "K"]
    if r in validRanks:
        print(True)
    else:
        print(False)

def suit_full_name(s):
    s=s.upper()
    nameDict ={"H": "Hearts",
               "C": "Clubs",
               "S": "Spades",
               "D": "Diamonds"
                }
    if s in nameDict:
        print(True)
    else:
        raise ValueError(f"Invalid suit symbol: {s}")
def rank_points(r):
    r =r.upper()
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
        print(pointsDict[r])
    else:
        raise ValueError(f"Invalid rank symbol: {r}") 

def rank_higher_than(r1,r2):
    r1=r1.upper()
    r2=r2.upper()
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
    if r1 not in rankDict:
        raise ValueError(f"Invalid rank symbol: {r1}") 
    if r2 not in rankDict:
        raise ValueError(f"Invalid rank symbol: {r2}") 
    if r1 and r2 in rankDict:
        if rankDict[r1] > rankDict[r2]:
            print(True)
        elif rankDict [r1] < rankDict[r2]:
            print(False)
        elif rankDict[r1] == rankDict[r2]:
            print(False)      
#print(valid_suit("C"))
#print(valid_suit("S"))
#print(valid_suit("P"))
#print(valid_rank("3"))
#print(valid_rank("7"))
#print(valid_rank("8"))
#print(rank_points("A"))
#print(rank_points("7"))
#print(rank_points("5"))
#print(rank_points("9"))
#print(rank_higher_than("3", "2"))
#rank_higher_than("6", "3")
#rank_higher_than("K", "Q")
#rank_higher_than("J", "7")
#rank_higher_than("4", "4")
#rank_higher_than("8", "7")
