import json
import re
import xml.etree.ElementTree as ET
#f = open("file.xml", "r")
#string = f.read()
#nobr = string.replace("<br //>", "[br]")
tree = ET.parse("file2.xml")
root = tree.getroot()
#print(root.tag)
head = root[0]
body = root[1]
hymns_json = {}
#for child in body:
   #print(child.tag)
def getLyrics():
 verses = []
 aVerse = {}
 divelement = body[0][1][0][2][0]
 headings = divelement.findall('{http://www.w3.org/1999/xhtml}h2') 
 lines =  divelement.findall('{http://www.w3.org/1999/xhtml}p')
 for x in range(0, len(headings)):
  h2 = headings[x].text
  p = lines[x].text
  #print(h2)
  p_split = p.split("[br]")
  verselines = []
 
  for i in p_split:
    verselines.append(i.strip())
  aVerse = {"verse_title": h2, "lines": verselines}
  verses.append(aVerse)


 return verses


def getNumber():
  titlemain = head.find('{http://www.w3.org/1999/xhtml}title')
  title_split = titlemain.text.split("\\\\")
  numbertitle = title_split[0]
  #print(numbertitle)
  number = re.findall(r'[0-9]*', numbertitle)
  #print(number[0])
  return number[0]

def getTitle():
  title = ""
  meta = head.findall('{http://www.w3.org/1999/xhtml}meta')
  for child in meta:
     property = child.attrib.get("property")
     if property=="og:title":
        title = child.attrib.get("content")
        #print(title)
  return title

def getAuthor():
  authors = []
  try:
      div = body[0][1][0][2][1][2]
      dd = div.findall('{http://www.w3.org/1999/xhtml}dd')
      for child in dd:
        classvalue = child.attrib.get("class")
        if classvalue=="hymn-author":
            author_name = child[0].text
            jsondata = {"name": author_name, "date": ""}
            authors.append(jsondata)
  except:
      authors = []
  return authors

def getTopic():
    topic = []
    try:
          div = body[0][1][0][2][1][2]
          dd = div.findall('{http://www.w3.org/1999/xhtml}dd')
          for child in dd:
            classvalue = child.attrib.get("class")
            if classvalue=="hymn-topic":
                topic_name = child[0].text.replace("\n", " ")
                topic.append(topic_name)
    except:
          topic = []
    return topic

def getCopyRight():
    copyright = ""
    try:
          div = body[0][1][0][2][1][2]
          dd = div.findall('{http://www.w3.org/1999/xhtml}dd')
          for child in dd:
            classvalue = child.attrib.get("class")
            if classvalue=="hymn-copyright":
                copyright = child[0].text.replace("\n", " ")

    except:
          copyright = ""
    return copyright

def getMeter():
    meter = ""
    try:
          div = body[0][1][0][2][1][2]
          dd = div.findall('{http://www.w3.org/1999/xhtml}dd')
          for child in dd:
            classvalue = child.attrib.get("class")
            if classvalue=="hymn-meter":
                meter = child[0].text.replace("\n", " ")

    except:
          meter = ""
    return meter

def getComposer():
    composer = {}
    try:
          div = body[0][1][0][2][1][2]
          dd = div.findall('{http://www.w3.org/1999/xhtml}dd')
          for child in dd:
            classvalue = child.attrib.get("class")
            if classvalue=="hymn-composer":
                name = child[0].text.replace("\n", " ")
                # date = dd.text()
                composer = {"name": name, "date": ""}


    except:
          composer = ""
    return composer


def getTune():
    tune = ""
    try:
          div = body[0][1][0][2][1][2]
          dd = div.findall('{http://www.w3.org/1999/xhtml}dd')
          for child in dd:
            classvalue = child.attrib.get("class")
            if classvalue=="hymn-tune":
                tune = child[0].text.replace("\n", " ")

    except:
          tune = ""
    return tune

title = getTitle()
number = getNumber()
print(title)
print(number)
lyrics = getLyrics()
print(lyrics)
authors = getAuthor()
topic = getTopic()
copyright = getCopyRight()
meter = getMeter()
composer = getComposer()
tune = getTune()
hymns_json[number] = {"number": number, "title": title, "topic": topic, "hymn_info": {"authors": authors, "composer": composer, "tune": tune, "meter": meter, "copyright": copyright, }, "verses": lyrics}
print(hymns_json)


