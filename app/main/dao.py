from app.main.model.card import Card
from app.main.model.deck import Deck
from random import randrange
import json
from pymongo import MongoClient

'''cards=[]
with open('app/main/database/cardsteszt.json') as json_data:
    d = json.load(json_data)
for i in range(len(d)):
    card=d[i]
    cards.append(Card(card.get('name'),card.get('top'),card.get('bottom'),card.get('left'),card.get('right')))'''

class UserService():
    def register(self):
        pass
        
    def login(self):
        pass
        
    def logout(self):
        pass
    
class CardService():       
    
    def readDeckfromJson(self):
        cards=[]
        with open('app/main/database/cards.json') as json_data:
            d = json.load(json_data)
        for i in range(len(d)):
            card=d[i]
            cards.append(Card(card.get('name'),card.get('top'),card.get('bottom'),card.get('left'),card.get('right')))
        return cards
        
    def readDeckfromMongoDB(self,owner):
        client = MongoClient("192.168.125.231", 27017)
        db = client.cardGame
        cards=[]
        decks=db['decks']
        deck = decks.find({"owner": owner})
        cardNames=deck[0]["cards"]
        for name in cardNames:
            cursor = db.cards.find({"name": name})
            card = cursor[0]
            cards.append(Card(card.get('name'),card.get('top'),card.get('bottom'),card.get('left'),card.get('right')))
        print("------------------------------------------------------------------------------------------------------------------")
        print(cards)
        return cards
        
    #def randomCard(self,cards):
    #    return cards.pop(randrange(len(cards)))

#cardService=CardService()
#print (cardService.randomCard())
    
