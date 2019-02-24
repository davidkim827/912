import pymongo
import CongestionDB, TowerZoneEvacMessage

#Create fake input caller
name = 'Jane Doe'
tower = 'Tower1'
zone = 1



#Create mongo client and database
client = pymongo.MongoClient()
db = client['EscapeNY']
congestionData = db['Congestion']
emergencyCallerData = db['EmergencyCallers']
firstResponderData = db['FirstResponder']

#Analyze First Responder Data
#Block off routes based off First Responder advice (this is first priority)
def analyzeFirstResponderData():
    firstResponderString = ''
    for entry in firstResponderData.find({'Zone':zone}):
        if firstResponderString.find(entry.get('Advice'))==-1:
            if (firstResponderString!=''):
                firstResponderString += ', '
            firstResponderString += entry.get('Advice')
    return firstResponderString

#Analyze Emergency Caller Data
#Block off routes based off emergency caller feedback
def analyzeEmergencyCallerData():
    emergencyCallerString = ''
    for entry in emergencyCallerData.find({'Zone':zone}):
        if entry.get('AvoidStreet') is not None and emergencyCallerString.find(entry.get('AvoidStreet'))==-1:
            if (emergencyCallerString!=''):
                emergencyCallerString += ', '
            emergencyCallerString += ' ' + entry.get('AvoidStreet')
    return emergencyCallerString

#Analyze Congestion Data
#Look at secondary data based off how busy certain areas are
def analyzeCongestionData():
    congestionString = ''
    zoneArea = TowerZoneEvacMessage.getDangerPoint()
    for entry in congestionData.find({'Zone':zone}):
        if entry.get('NumPings') is not None and entry.get('NumPings')>100000 and congestionString.find(zoneArea)==-1:
            if (congestionString!=''):
                congestionString += ', '
            congestionString += ' ' + zoneArea
    return congestionString

#Return final string with streets to avoid
def finalAnalysis():
    if (analyzeFirstResponderData()!='' and analyzeEmergencyCallerData()!='' and analyzeCongestionData()!=''):
        return 'Avoid ' + analyzeFirstResponderData() + ', ' + analyzeEmergencyCallerData() + ', ' + analyzeCongestionData()
    elif (analyzeFirstResponderData()=='' and analyzeEmergencyCallerData()!='' and analyzeCongestionData()!=''):
        return 'Avoid ' + analyzeEmergencyCallerData() + ', ' + analyzeCongestionData()
    elif (analyzeFirstResponderData()!='' and analyzeEmergencyCallerData()=='' and analyzeCongestionData()!=''):
        return 'Avoid ' + analyzeFirstResponderData() + ', ' + analyzeCongestionData()
    elif (analyzeFirstResponderData()!='' and analyzeEmergencyCallerData()!='' and analyzeCongestionData()==''):
        return 'Avoid ' + analyzeFirstResponderData() + ', ' + analyzeEmergencyCallerData()
    elif (analyzeFirstResponderData()!='' and analyzeEmergencyCallerData()=='' and analyzeCongestionData()==''):
        return 'Avoid ' + analyzeFirstResponderData()
    elif (analyzeFirstResponderData()=='' and analyzeEmergencyCallerData()!='' and analyzeCongestionData()==''):
        return 'Avoid ' + analyzeEmergencyCallerData()
    elif (analyzeFirstResponderData()=='' and analyzeEmergencyCallerData()=='' and analyzeCongestionData()!=''):
        return 'Avoid ' + analyzeCongestionData()
    else:
        return ''



    


