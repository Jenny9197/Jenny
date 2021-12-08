import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#make a socket for internet
mysock.connect(('data.pr4e.org', 80))
#make a phone call & make a protocol
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
#info what to send to the network
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
        #when stream is done
    print(data.decode(),end="")
mysock.close()
