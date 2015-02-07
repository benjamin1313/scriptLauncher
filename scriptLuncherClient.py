import socket

HOST = "localhost"
PORT = 5070
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
scripts = s.recv(2048)
print scripts
while True:
    message = raw_input("Run: ")
    s.send(message)
    if message == "!exit":
        break
    print "Awaiting reply"
    reply = s.recv(1024)
    print "Received ", repr(reply)

s.close()
