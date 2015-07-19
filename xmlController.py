import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree
from email.Utils import formatdate
tree = ET.parse('Test.xml')
root = tree.getroot()

# tree1 = ET.parse('haha.xml')

channel = root[0]


# userID should be passed in as a string with no spaces
def getFileNameForUser(userID):
    extension = ".xml"
    return userID + extension


def createNewXml(userID, action):
    newRoot = ET.Element("rss")
    newRoot.set('version', '2.0')
    channel1 = ET.SubElement(newRoot, "channel")
    makeFirstItem(channel1, action, userID)
    newnewTree = ET.ElementTree(newRoot)
    newnewTree.write(getFileNameForUser(userID), encoding="UTF-8")


def makeFirstItem(channel1, action, userID):
    newItem = ET.SubElement(channel1, "item")
    ET.SubElement(channel1, "title").text = "RSS Feed for IFTTT"
    ET.SubElement(channel1, "link").text = "http://rosexu.github.io/BattleHackRSS/" + userID
    ET.SubElement(channel1, "description").text = "Personalized RSS for user " + userID
    populateSubfields(newItem, action, "http://rosexu.github.io/BattleHackRSS/" + userID, "Personalized RSS for user " + userID, getCurrentTime(), "http://rosexu.github.io/BattleHackRSS/" + userID + "1")


def populateSubfields(item, title, link, desc, date, guid):
    ET.SubElement(item, "title").text = title
    ET.SubElement(item, "link").text = link
    ET.SubElement(item, "description").text = desc
    ET.SubElement(item, "pubDate").text = date
    ET.SubElement(item, "guid").text = guid


def handleRequest(userID, action):
    try:
        aTree = ET.parse(getFileNameForUser(userID))
        print "file exists"
    except IOError:
        createNewXml(userID)


def getCurrentTime():
    return formatdate()


def getLastChildIndex():
    index = 0
    for child in channel:
        index += 1
    return index


def getNewGuid(index):
    oldGuid = channel[index-1].find("guid")
    try:
        lastCharOfOldGuid = int(oldGuid.text[-1:])
        newGuidNum = lastCharOfOldGuid + 1
        newGuid = oldGuid.text[:-1] + str(newGuidNum)
        return newGuid
    except ValueError:
        print "error: last char is not a number"


def addNewItem(title, link, description, pubDate, guid):
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = title
    ET.SubElement(item, "link").text = link
    ET.SubElement(item, "description").text = description
    ET.SubElement(item, "pubDate").text = pubDate
    ET.SubElement(item, "guid").text = guid
    tree.write('Test.xml')

# this adds a new item to Test.xml(RSS feed) with child tags of the things you passes in.
# addNewItem("turn music off", "link", "description", getCurrentTime(), getNewGuid(getLastChildIndex()))
print getFileNameForUser("20565628")
# makes a new xml file for first time users
createNewXml("20565628", "make music")
