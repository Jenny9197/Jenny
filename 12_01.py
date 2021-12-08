import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connec(('data.pr4e.org', 80))