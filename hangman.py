class Card:
    def __init__(self,v,s):
        self.value = v
        self.suit = s
        self.values = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.suits = ["heart","diamond","club","spade"]
    def __lt__(self,other):
        if self.value < other.value:
            return True
        elif self.value = other.value:
            if self.suit < other.suit:
                return True
        return False

    def __gt__(self,other):
        if self.value < other.value:
            return True
        elif self.value == other.value:
            if self.suit < other.suit:
                return True
        return False

    def __rept__(self,other):
        return self.suits[self.suit] + " of " + self.value[self.value]

class Player:
    def __init__(self,n):
        self.name = n
        self.wins = 0
        self.card = None

class Deck:
    cards =[]
    def __init__(self):
        
        for i in range(2,14):
            for j in range(0,3):
                cards.append(Card(i,j))
    def rm_pickup():
        return cards.pop
    
