import subprocess

url = input("url: ")
command = "sudo curl -L " + url + " -o source.html"
subprocess.call(command, shell=True)
command = "tidy -q -asxml --numeric-entities yes source.html >file.xml"
subprocess.call(command, shell=True)

#remove br tags
command = "./removebr.py"
subprocess.call(command, shell=True)