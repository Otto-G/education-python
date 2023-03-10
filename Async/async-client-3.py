import errno
import select
import socket
import time

def boringTask():
    i = 0
    while i < 10:
        i += 1
        print(i)
        time.sleep(0.02)
        yield

def sendDataTask(port, data):
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
    
    fds = dict(w={}, r={})
    while len(tasks) or len(fds['w']) or len(fds['r']):
        newTasks = []
        for task in tasks:
            try:
                resp = next(task)
                try:
                    iter(resp)
                    fds[resp[0]][resp[1]] = task
                except TypeError:
                    # This task has to be done since it isn't depend on any fd.
                    # Need to define what a fd is from the source info
                    newTasks.append(task)
            except StopIteration:
                # function completed
                pass
        
        if len(fds['w'].keys()) or len(fds['r'].keys()):

            # Pulling in the tasks that are now able to be read, written, or 
            # have cleared their exception.  
            readable, writeable, exceptional = select.select(fds['r'].keys(), 
                                                             fds['w'].keys(),
                                                             [],
                                                             0)

            # Adding all of the the readable tasks to the task list
            for readable_sock in readable:
                newTasks.append(fds['r'][readable_sock])
                
                # Once the task has been added to the task list, remove it from
                # the pending task dictionary
                del(fds['r'][readable_sock])

            # Adding all of the writeable tasks to the task list
            for fd in writeable:
                newTasks.append(fds['w'][fd])

                # Once the task has been added to the task list, remove it from
                # the pending task dictionary
                del(fds['w'][fd])
        
        # Loops will be made when there are only pending items left and nothing 
        # has cleared.  We need to filter those times out so that the output 
        # isn't spammed with []
        if len(newTasks) > 0:
            print("newTasks = {}".format(newTasks))
        
        tasks = newTasks
            
