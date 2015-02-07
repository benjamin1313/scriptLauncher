import socket, os

if os.path.isdir("scripts") == False:
    os.mkdir("scripts")

host = ""
port = 5070

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print str(e)

try:
    s.listen(1)
except:
    print "seems like this port is allready taken"

def main(conn):
    scripts = os.listdir("scripts")
    conn.sendall(str(scripts))
    while True:
        data = conn.recv(2048)
        if data in scripts:
            os.system("start scripts/" + data)
            conn.sendall("runnnig scripts "+data)
        elif data == "scripts":
            conn.sendall(str(scripts))
        elif data == "!exit":
            conn.close()
            break
        else:
            conn.sendall("no file")
    conn.close()

while True:
    conn, addr = s.accept()
    main(conn)

