import subprocess

source.html = ""
command = "tidy -q -asxml --numeric-entities yes "+source.html +" >file.xml"
subprocess.call(command, shell=True)
