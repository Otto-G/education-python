import errno
import select
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 1234))
sock.setblocking(False)

data = "<(0_0<) <(0_0)> (>0_0)>".encode("utf8") * 10 * 1024 * 35  # Data to send
dataSize = len(data)
print("Bytes to send: %s" %(dataSize))

totalSent = 0
while len(data):
    try:
        sent = sock.send(data)
        totalSent += sent
        data = data[sent:]
        print("sending data")
    except socket.error as e:
        if e.errno != errno.EAGAIN:
            raise e
        print("Blocking with %s data remaining" % (len(data)))
        select.select([], [sock], [])  # Blocking until all data sent

assert sock.send(data) == len(data)  # Throws error if all data hasn't been sent

print("Finished")
