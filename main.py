import Analytics, TowerZoneEvacMessage
#compiles information to push the message out via text
def getMessageToSend():
	msg = f"Hello. You just messaged us. \nWe recommend going to {TowerZoneEvacMessage.getEvacPoint()} \n{Analytics.finalAnalysis()} \n{TowerZoneEvacMessage.getMapLink()} "
	print(msg)

getMessageToSend()