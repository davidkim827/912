import datetime
import pymongo

#Dictionary of all towers to each corresponding zone and location
zone = {'Tower1' : 1, 'Tower2' : 2, 'Tower3' : 3}
zoneLocation = {1 : 'Brooklyn Bridge', 2 : 'Prospect Park', 3 : 'Empire State Building' }

#Test data to be dynamically returned based off input from external source
def getTower():
    return 'Tower1'

def getZone():
    return zone.get(getTower())

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
putCongestionInDB(getTime(),getTower(),getZone(),getNumPings())

    #for document in congestionData.find({}):
#print(document)
