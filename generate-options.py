import json

f = open("hymns2test.json", "r")
jsondata = json.load(f)
newjsondata = {}

for key in jsondata:
  name = key + ". " + jsondata[key]["title"]
  newjsondata[name] = jsondata[key]

with open("hymns-options.json", "w") as outfile:
    json.dump(newjsondata, outfile)
