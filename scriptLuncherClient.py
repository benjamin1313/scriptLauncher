import socket

host = "localhost"
port = 5070
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
scripts = s.recv(2048)
print scripts
while True:
    message = raw_input("Run: ")
    s.send(message)
    if message == "!exit":
        break
    print "Awaiting reply"
    reply = s.recv(2048)
    print "Received ", repr(reply)

s.close()
