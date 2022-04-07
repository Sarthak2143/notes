#!/usr/bin/env python3

import socket

target_host = "0.0.0.0"
target_port = 9998

#create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #connect the client
    client.connect((target_host, target_port))

    #sending data
    client.send(b"Never gonna give you up.")

    #receive data
    response = client.recv(4096)

    print(response.decode())
    client.close()

# keyboard interrupt

except KeyboardInterrupt:
    print("\nExiting...")

# throw the error
except Exception as e:
    print(e)
