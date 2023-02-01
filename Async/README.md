# Async

Practice for creating functions that can work without blocking the rest of the code

# Base

Some of this code is based on [Vaidik Kapoor](https://medium.com/vaidikkapoor/understanding-non-blocking-i-o-with-python-part-1-ec31a2e2db9b) writing about non-blocking code.  

# Server 1

Simple server based on socket that listens for data to be sent to it and then 
will print it out.  It will close the socket if there is a keyboard interrupt.  

This server is kept running all of the time and all of the clients will connect
to it.  When a connection is made, it will print out who it was and it will also 
print out any data that is sent to it.  

# Server 2

Just a copy of [Server 1](#server-1) with a different port to also recieve data.
The only client that will also connect to this one is [async-client-3](./async-client-3.py).  