import xml.etree.ElementTree as ET
from email.Utils import formatdate
tree = ET.parse('Test.xml')
root = tree.getroot()

channel = root[0]


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
addNewItem("turn music off", "link", "description", getCurrentTime(), getNewGuid(getLastChildIndex()))
