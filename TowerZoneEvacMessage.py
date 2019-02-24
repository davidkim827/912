import random

#Creates a random zone data set with random unique towers in each zone. There are 5 zones with 4 towers in each.
def createRandomZoneData():
	zones = dict()
	rTowerUsed = list()
	while len(rTowerUsed) != 20:
		r = random.randint(1,20)
		if r in rTowerUsed:
			r = random.randint(1,20)
		else:
			rTowerUsed.append(r)
	for i in range(len(rTowerUsed)):
		key = f"zone{i%5+1}"
		zones.setdefault(key,[]).append(rTowerUsed[i])
	return zones

def getRandomZoneData():
	zone = zoneDict()
	return zone

#random tower numbers used as towerIDs
def makeRandomTower():
	r = random.randint(1,20)
	return r

def getTower():
	return towerInfo

#This function needs input of a tower data that wireless phone is calling from, and looks up the zone that the tower belongs to
def getZoneNumber(towerData):
	for zone, tower in zoneDict.items():
		if towerData in tower:
			return int(zone[4:])

def getZone():
	zone = zoneInfo
	return zone

#This function requires a zone number input of the tower that the phone call was picked up from, and returns the evac location from a database/dictionary...
def getEvacPointLocation(zoneNumber):
	for evacLoc, zone in evacPoints.items():
		if zone == zoneNumber:
			return evacLoc

def getEvacPoint():
	evacPoint = evacInfo
	return evacPoint

def getDangerPoint():
	r = random.randint(1,5)
	if r == getZone():
		r += 1
		if r == 6:
			r = 1
	for evacLoc, zone in evacPoints.items():
		if zone == r:
			return evacLoc

def mapLink(zoneNumber):
	for zone, link in evacLinks.items():
		if zone == getZone():
			print (link)
			return link

def getMapLink():
	link = mapLink
	return link

	

evacPoints = {"Pier 62": 1, "Citi Field": 2, "Manhattan Bridge": 3,"Brooklyn Bridge": 4, "Pier 40": 5}
evacLinks = {1: "https://goo.gl/maps/Eu89ZEys4xG2", 2: "https://goo.gl/maps/EEZgAx6XjTo", 3: "https://goo.gl/maps/Vi3F4RK9UDu",4: "https://goo.gl/maps/xFRrnnbdXRm",5: "https://goo.gl/maps/m9PCTBXXBcF2"}
zoneDict = createRandomZoneData()
towerInfo = makeRandomTower()
zoneInfo = getZoneNumber(towerInfo)
evacInfo = getEvacPointLocation(zoneInfo)
dangerPoint = getDangerPoint()
mapLink = mapLink(zoneInfo)
print(dangerPoint)