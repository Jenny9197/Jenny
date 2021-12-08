#make an URLLIB in python
#make a connection and transmit requesting of get
#send a new line and get the data and clear for header
#no header and keep the data
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())