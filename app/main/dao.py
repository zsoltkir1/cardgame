from model.card import Card
from random import randrange
import json

cards=[]
with open('database/cardsteszt.json') as json_data:
    d = json.load(json_data)
for i in range(len(d)):
    card=d[i]
    cards.append(Card(card.get('name'),card.get('top'),card.get('bottom'),card.get('left'),card.get('right')))

class CardService():
    
    def randomCard(self):
        return cards.pop(randrange(len(cards)))

cardService=CardService()
print (cardService.randomCard())
