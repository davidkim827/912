import datetime
import pymongo

#Dictionary of all towers to each corresponding zone
zone = {'Tower1' : 1, 'Tower2' : 2, 'Tower3' : 3}


#Test data to be dynamically returned based off input from external source
def getTower():
    return 'Tower1'

def getZone():
    return zone.get(getTower())

def getTime():
    return datetime.datetime.now()

def getAvoidStreet():
    return 'Wall St'

def getTypeEvent():
    return 'Active Shooter'


#Function to log each emergency into our dbs
def putEmergencyInDB(timeContact,cellTower,zone,avoidSt,typeEvent):
    newDict = {'TimeOfContact' : timeContact, 'CellTower': cellTower, 'Zone': zone, 'AvoidStreet' : avoidSt, 'EventType' : typeEvent}
    emergencyCallerData.insert_one(newDict)


#Create mongo client and database
client = pymongo.MongoClient()
db = client['EscapeNY']

#Create Emergency Callers collection of data
emergencyCallerData = db['EmergencyCallers']


#Put test data in db
putEmergencyInDB(getTime(),getTower(),getZone(),getAvoidStreet(),getTypeEvent())

    #for document in emergencyCallerData.find({}):
#print(document)
