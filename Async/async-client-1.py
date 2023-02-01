import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 1234))

# Step 1 - Add line to prevent blocking by send
sock.setblocking(False)

data = "<(0_0<) <(0_0)> (>0_0)>".encode("utf8") * 10 * 1024 * 3  # Semi-large amount of data
assert sock.send(data) == len(data)  # Throws error if all data hasn't been sent

print("Finished")
