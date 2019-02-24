import datetime, pymongo
import TowerZoneEvacMessage

def getTime():
    return datetime.datetime.now()

def getNumPings():
    return 20000000


#Function to log each emergency into our dbs
def putCongestionInDB(timeContact,cellTower,zone,numPings):
    newDict = {'TimeOfContact' : timeContact, 'CellTower': cellTower, 'Zone': zone, 'NumPings' : numPings}
    congestionData.insert_one(newDict)


#Create mongo client and database
client = pymongo.MongoClient()
db = client['EscapeNY']

#Create Emergency Callers collection of data
congestionData = db['Congestion']


#Put congestion data in db
putCongestionInDB(getTime(),TowerZoneEvacMessage.getTower(),TowerZoneEvacMessage.getZone(),getNumPings())
