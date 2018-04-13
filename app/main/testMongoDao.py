from pymongo import MongoClient

def storeData():
    client = MongoClient("192.168.125.231", 27017)
    db = client.cardGame
    db.cards.insert_one({"cardname":"teszt"})

def readData():
    client = MongoClient("192.168.125.231", 27017)
    db = client.cardGame
    print(db.cards.find_one())
    
if __name__ == "__main__":
    #storeData()
    readData()
    