import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5678 if len(sys.argv) == 1 else int(sys.argv[1])
sock.bind(("localhost", port))
sock.listen(5)

try:
    i = 0
    while True:
        conn, info = sock.accept()
        print("connection from: " + str(info))

        data = conn.recv(1024).decode()
        while data:
            i += 1
            print("Data #%s: " % (i) + str(data))

            data = conn.recv(1024).decode()

except KeyboardInterrupt:
    sock.close
