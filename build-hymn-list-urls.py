import requests
import re
import json
urlslist = []
#get all the group number urls
import re
import xml.etree.ElementTree as ET
groupurls = []
import subprocess
def getGroupUrls():
    tree = ET.parse("file.xml")
    root = tree.getroot()
    head = root[0]
    body = root[1][0][1][0][0][1][0]
    #get all the urls in each group

    for child in body:
        for a in child:
            # print(a.attrib.get("href"))
            json_data = {"name": a.text, "href": a.attrib.get("href")}
            groupurls.append(json_data)

def getHymnURL(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    head = root[0]
    body = root[1][0][1][0][1][0][0][1]
    for child in body:
        for h2 in child.findall('{http://www.w3.org/1999/xhtml}h2'):
            for a in h2:
                #print(a.attrib.get("href"))
                urlslist.append(a.attrib.get("href"))

#will fetch urls from each group number range
def downloadHTMLtoXML(url, name):
    command = "sudo curl -L " + url + " -o source.html"
    subprocess.call(command, shell=True)
    command = "tidy -q -asxml --numeric-entities yes source.html >"+name+".xml"
    subprocess.call(command, shell=True)
    getHymnURL(name+".xml")

getGroupUrls()
#print(groupurls)

for item in groupurls:
   downloadHTMLtoXML(item["href"], item["name"])


#add all the urls from each group to the ultimate list of urls



print(urlslist)
with open("hymnlinks.json", "w") as outfile:
    json.dump({"list": urlslist}, outfile)