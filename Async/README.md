# Async

Practice for creating functions that can work without blocking the rest of the
code

## Base

Some of this code is based on [Vaidik
Kapoor](https://medium.com/vaidikkapoor/understanding-non-blocking-i-o-with-python-part-1-ec31a2e2db9b)
writing about non-blocking code.  

## [Server 1](./async-server-1.py)

Simple server based on socket that listens for data to be sent to it and then
will print it out.  It will close the socket if there is a keyboard interrupt.  

This server is kept running all of the time and all of the clients will connect
to it.  When a connection is made, it will print out who it was and it will also
print out any data that is sent to it.  

## [Server 2](./async-server-2.py)

Just a copy of [Server 1](#server-1) with a different port to also recieve data.
The only client that will also connect to this one is
[async-client-3](./async-client-3.py).  

## [Client 1](./async-client-1.py)

This is the first program and also the most basic.  When it was first made,
`sock.setblocking` wasn't included and would cause the program to hang while the
server was processing data.  

Adding in `sock.setblocking(False)` caused the socket to drop the connection if
the server was busy.  This would cause an error to be thrown before it could
print finished since we were checking to see if all of the data was being sent.

## [Client 2](./async-client-2.py)

This improves on [client 1](./async-client-1.py) by adding in a method to retry
sending all of the data.  The client will send all of the data that it can and
add up all of the data sent and remove the what has been sent from the data
object.  

If the server is busy and causes the socket to error, it will print that the
server is blocking and then try again so long as there is still data to be sent.

## [Client 3](./async-client-3.py)

This takes what was learned from [client 2](./async-client-2.py) and adds in
connecting to a second server as well as running a local function.  

`boringTask` is a simple function that will just print out numbers every so many
seconds to show that it is still running.  To keep from hogging up all of the
function time, it will `yield` every loop while it waits. The yielding nothing
after every loop is important to make sure that the other functions can be run
in the mean time.  Since there isn't anything else blocking this function, it
would normally run until finished.  

The `sendDataTask` is the function that is used to connect to the two servers.  
It is very similar to the code used in [Client 2](./async-client-2.py) but has
been turned into a general function that takes two inputs of a port and the data
to be sent.  When there is an error from the server, it will `yield` and return
to the `__main__` function to be called again later.  When it yields, it returns
the current sock object so that it can be continued later on when it is no
longer blocked.  

The main function starts by defining 3 tasks to run: `boring task`, and 2 sets
of `sendDataTask` sending different text to the two ports that we set our
[async-server-1](./async-server-1.py) and [async-server-2](./async-server-2.py)
to listen on.  From there it initializes `fds` which is a dictionary containing
the tasks that `select` will monitor and run.  

The while loop is set to run so long as there are either tasks to do (starting
with the initial tasks), or tasks that are ready for `'w'` writing or `'r'`
reading by the select function.
