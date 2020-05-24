import json

f = open("hymns-options.json", "r")
jsondata = json.load(f)
newjsondata = {}

for key in jsondata:
  verses = jsondata[key]['verses']
  titleslines = {}
  titles = []
  refrainJson = {}
  for verse in range(0, len(verses)):
      title = verses[verse]['verse_title']
      lines = verses[verse]['lines']
      titleslines[title] = lines
      titles.append(title)
  if 'Refrain' in titleslines:
      # print (titleslines['Refrain'])
      refrainJson = {'verse_title': 'Refrain', 'lines': titleslines['Refrain']}
  if 'Refrain' in titles:
      indexOfRefrain = titles.index('Refrain')
      # for x in range(0, len(titles), 2):
      totalTitles = len(titles)
      # titles.insert(totalTitles, 'Refrain')
      # titles.insert(totalTitles-1, 'Refrain')
      # titles.insert(totalTitles-2, 'Refrain')
      # titles.insert(totalTitles-3, 'Refrain')
      versewithrefrains = []
      for x in titles:
          newlines = titleslines[x]

          if x!='Refrain':
              verseJson = {'verse_title': x, 'lines': newlines}
              versewithrefrains.append(verseJson)
              versewithrefrains.append(refrainJson)
          # if x!='Refrain':
          #   versewithrefrains.append(verseJson)
          #   versewithrefrains.append(refrainJson)
          if titles.index(x)==0 and x=='Refrain':
              versewithrefrains.append(refrainJson)

      # print(versewithrefrains)
      jsondata[key]['verses'] = versewithrefrains

with open("hymns-refrain.json", "w") as outfile:
    json.dump(jsondata, outfile)
