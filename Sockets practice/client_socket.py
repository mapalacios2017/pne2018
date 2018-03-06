import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
# now connect to the web server on port 80 (the normal http port)
s.connect(("www.urjc.es", 80))
print(s)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.es", 80))
print(s)

# I want to get the main page
# GET /index.html

s.send(str.encode("GET /index.html\n"))
print(s.recv(1024))
# Connect to our own server
PORT = 8090
SERVER = localhost

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8090))