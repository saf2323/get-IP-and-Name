import socket 

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(ip)
print(host)