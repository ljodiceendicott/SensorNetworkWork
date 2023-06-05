# simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen

# this is the client

import socket
import sys

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
host = sys.argv[1] # server address
port = int(sys.argv[2]) # server port
s.connect((host, port))


# read echo
i = 0
while(1):
    data = s.recv(20) # read up to 1000000 bytes
    #data = data.decode()
    int_val = int.from_bytes(data, "big")
    #data = int(data, 16)
    print(int_val)
    # i += 1
    # if (i < 5): # look only at the first part of the message
    #     print(data)
    # if not data: # if end of data, leave loop
    #     break
    # print('received', len(data), 'bytes')
# close the connection
#s.close()
