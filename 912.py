#!/usr/bin/env python3

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
	return(zones)

#This function needs input of a tower data that wireless phone is calling from, and looks up the zone that the tower belongs to
def getZone(towerData):
	for zone, tower in zoneDict.items():
		if towerData in tower:
			return zone[4:]

#This function requires a zone number input of the tower that the phone call was picked up from, and returns the evac location from a database/dictionary...
def getEvacPoint(zoneNumber):
	zoneNumber = int(zoneNumber)
	for evacLoc, zone in evacPoints.items():
		if zone == zoneNumber:
			return evacLoc

#compiles information to push the message out via text
def getMessageToSend():
	msg = f"Hello. You just messaged us.\
			We recommend going to {getEvacPoint(int(getZone(r)))} \
			Avoid {analytics()}"



r = random.randint(1,20)
evacPoints = {"Pier 62": 1, "Citi Field": 2, "Manhattan Bridge": 3,"Brooklyn Bridge": 4, "Pier 40": 5}
zoneDict = createRandomZoneData()
print(getEvacPoint(getZone(r)))
