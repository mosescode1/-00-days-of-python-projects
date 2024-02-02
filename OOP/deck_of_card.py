from random import shuffle

class Card:
    def __init__(self, suit, value) -> None:
        self.value = value
        self.suit = suit

    
    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"
        

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]
        
    def __repr__(self) -> str:
        return f"Deck of {self.count()} cards"
        
    def count(self):
        return len(self.cards)
    
    def _deal(self, num):
        count = self.count()
        actual_num = min(count, num)
        cards = self.cards[-actual_num:]
        self.cards = self.cards[:-actual_num]
        return cards
        
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("shuffle only full card")
        shuffle(self.cards)
        return self

    def deal_hand(self):
        return self._deal(1)[0]
    
    def deal_card(self, num):
        return self._deal(num)
    

user1 = Deck()
user1.shuffle()
user1._deal(3)
