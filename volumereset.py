import requests

initialvolumeb = open("initialvolume.txt", "r").read()

print(initialvolumeb)

apicommandpart1 = 'http://10.0.0.17:15081/levels/room?volume='
apicommand = apicommandpart1 + initialvolumeb

print(apicommand)

def volume_changeiv():
     requests.put(apicommand)

volume_changeiv()