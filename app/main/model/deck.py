class Deck():
    
    def __init__(self,owner,cards):
        self.owner=owner
        self.cards=cards

    def __str__(self):
        return "owner: "+self.owner