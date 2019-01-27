import requests


volumeread = requests.get('http://10.0.0.17:15081/levels/')
initialvolumecontainer = volumeread.json()
print(initialvolumecontainer)
initialvolume = initialvolumecontainer.get('volume')
print(initialvolume)


text_file = open("initialvolume.txt", "w")
text_file.write(initialvolume)
text_file.close()

def volume_change75():
     requests.put('http://10.0.0.17:15081/levels/room?volume=75')

volume_change75()
