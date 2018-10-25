from pymongo import MongoClient
import json

def storeDeck():
    client = MongoClient("192.168.125.231", 27017)
    db = client.cardGame
    #db.decks.insert_one({"owner":"dyntell","cards":['hegedAtty', 'zsoltkir1', 'PinterUr', 'Kriszegy..', 'Pitor', 'LosTibi', 'Jabba', 'unlucky', 'ZSAAAA', 'Partner', 'Danika', 'Rostas', 'Rip', 'NolifeMari', 'Dual', 'GTX1080TI', 'CsicskaBalint', 'anyad']})
    #db.decks.insert_one({"owner":"forex","cards:":['hegedAtty', 'zsoltkir1', 'PinterUr', 'Kriszegy..','Pitor','Long', 'DNZS', 'Short', 'Soybeans', 'Bollinger', 'Arima', '-400EUR', 'Reketye', 'Threadripper', 'BorosB', 'KWszunet', 'theMemeLord', 'Tesla', 'Venti']})
    #db.decks.insert_one({"owner":"wow","cards:":['UndeadMage', 'BloodElfPala', 'TaurenShaman', 'PandarenMonk', 'HumanLock', 'GnomeMage', 'TrollHunter', 'Warlock', 'Ilidian', 'BlackTemple', 'Horde', 'Alliance', 'Orgrimmar', 'OrcWarrior', 'DeathKnight', 'UndeadPriest', 'TaurenDruid', 'BloodElfRogue', 'Karazhan', 'ZulFarrak', 'GruulsLair', 'Nexus']})
    #db.decks.insert_one({"owner":"balint","cards:":['Laptop', 'Szekreny', 'Idojaras', 'Munka', 'Konferencia', 'NincsIdom', 'NemErdekel', 'SzopjatokLe', 'CsicskaVagyok', 'Papirok', 'LatnomKellene', 'Ensemble', 'Hawkes', 'TitanX', 'Google', 'NemHallottam', 'SzaraSkype', 'NemErekRa', 'Boston', 'USA', 'KPMG', 'JustBalint', 'IKEA']})
    #db.decks.insert_one({"owner":"barca","cards:":['Pique', 'Ronaldinho', 'Messi', 'Puyol', 'Xavi', 'Iniesta', 'Dembele', 'Suarez', 'Rakitic', 'Alba', 'Stegen', 'Alves', 'Kutinnyo', 'Umtiti', 'Turan', 'Gomes', 'Munir', 'Rafinha', 'Guardiola', 'Ronaldo', 'Neymar', 'Paco', 'Tito', 'CR7']})
    print("Deck stored")
    
def readDeck():
    client = MongoClient("192.168.125.231", 27017)
    db = client.cardGame
    db.decks.insert_one({"cardname":"teszt"})

def readData():
    client = MongoClient("192.168.125.231", 27017)
    db = client.cardGame
    #print(db.cards.find_one())
    collection=db['cards']
    cursor = collection.find({})
    for document in cursor:
        print(document)
    
def importDeck(jsonfile="test.json"):
    client = MongoClient("192.168.125.231", 27017)
    db = client.cardGame
    cards = db.cards
    page = open(jsonfile, 'r')
    parsed = json.loads(page.read())
    for card in parsed["Cards"]:
        cards.insert(card)
    print("Deck imported")
    
def printCards(jsonfile="test.json"):
    page = open(jsonfile, 'r')
    parsed = json.loads(page.read())
    cardNames=[]
    for card in parsed["Cards"]:
        cardNames.append(card["name"])
    print(cardNames)
    
if __name__ == "__main__":
    #storeData()
    #readData()
    #importDeck("database/dyntell.json")
    #importDeck("database/forex.json")
    #importDeck("database/wow.json")
    importDeck("database/scram.json")
    importDeck("database/tactical.json")
    #printCards("database/wow.json")
    #printCards("database/balint.json")
    #printCards("database/barca.json")
    storeDeck()
    
    