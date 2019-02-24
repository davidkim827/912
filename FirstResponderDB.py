import datetime
import pymongo


#Dummy input data (would come dynamically from external source)
thisZone = 1
advice = 'State St'

#Functions to retrieve first responder data to input
def getZone():
    return thisZone

def getTime():
    return datetime.datetime.now()

def getAdvice():
    return advice

#Function to log each first responder advice into our dbs
def putFirstResponderInDB(timeContact,zone,advice):
    newDict = {'TimeOfContact' : timeContact, 'Zone': zone, 'Advice' : advice}
    firstResponderData.insert_one(newDict)

#Create mongo client and database
client = pymongo.MongoClient()
db = client['EscapeNY']

#Create First Responder collection of data
firstResponderData = db['FirstResponder']

#Put test data in db
putFirstResponderInDB(getTime(),getZone(),getAdvice())

    #for document in firstResponderData.find({}):
#print(document)
