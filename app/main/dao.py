from app.main.model.card import Card
from random import randrange
import json

'''cards=[]
with open('app/main/database/cardsteszt.json') as json_data:
    d = json.load(json_data)
for i in range(len(d)):
    card=d[i]
    cards.append(Card(card.get('name'),card.get('top'),card.get('bottom'),card.get('left'),card.get('right')))'''

class CardService():       
    
    def initDeck(self):
        cards=[]
        with open('app/main/database/cardsteszt.json') as json_data:
            d = json.load(json_data)
        for i in range(len(d)):
            card=d[i]
            cards.append(Card(card.get('name'),card.get('top'),card.get('bottom'),card.get('left'),card.get('right')))
        return cards
        
    #def randomCard(self,cards):
    #    return cards.pop(randrange(len(cards)))

#cardService=CardService()
#print (cardService.randomCard())
