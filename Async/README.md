# Async

Practice for creating functions that can work without blocking the rest of the code

# Base

Some of this code is based on [Vaidik Kapoor](https://medium.com/vaidikkapoor/understanding-non-blocking-i-o-with-python-part-1-ec31a2e2db9b) writing about non-blocking code.  

# Server 1

Simple server based on socket that listens for data to be sent to it and then 
will print it out.  It will close the socket if there is a keyboard interrupt.  

![Async Server 1](./async-server-1.py)

# Server 2

Just a copy of [Server 1](#server-1) with a different port to also recieve data