import errno
import select
import socket
import time

def boringTask():
    i = 0
    while i < 20:
        i += 1
        print(i)
        time.sleep(0.02)
        yield

def sendDataTask(port, data)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", port))
    sock.setblocking(False)

    data = data.encode("utf8") * 10 * 1024 * 50
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
            yield('w', sock)
    
    print('Bytes sent: %s' % totalSent)


if __name__ == '__main__':
    tasks = [
        boringTask(), 
        sendDataTask(port=1234, data='<(0_0<) <(0_0)> (>0_0)>'),
        sendDataTask(port=5678, data='foobar')
    ]

    