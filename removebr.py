#!/usr/bin/python3

import subprocess
import re

f = open("file.xml", "r")
string = f.readlines()
xmldata = ""
for line in string:
  line = re.sub('<br \/>','[br]', line)
  #print(line)
  xmldata = xmldata +line

print(xmldata)
xmlbytes = bytes(xmldata.encode())
with open("file2.xml", "wb") as outfile:
  outfile.write(xmlbytes)
