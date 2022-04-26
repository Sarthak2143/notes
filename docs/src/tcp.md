# TCP Client and Server

The Transmission Control Protocol (TCP) is one of the main protocols of the Internet protocol suite. It originated in the initial network implementation in which it complemented the Internet Protocol (IP). Therefore, the entire suite is commonly referred to as TCP/IP. TCP provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating via an IP network.

## Making a basic TCP client

- First we will import `socket` library to deal with sockets.

```python
import socket
```

- Add the target IP address and Port number.

```python
target_host = '0.0.0.0'
target_port = 8000
```

> We are using our local IP '0.0.0.0' and Port `8000`. You can use any of your choice.

- Now create a socket object and add required arguments.

```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Here, we are using `AF_INET` and `SOCK_STREAM` methods because we are working with TCP.

- Now connect with target host.

```python
client.connect((target_host, target_port))
```

This method takes a tuple of target IP and Port number as an argument.

- Now send some raw bytes

```python
client.send(b'Hey there, from our TCP client.')
```

- Recieving data and saving it to a variable `response`

```python
response = client.recv(4096)
```

- Decoding the response

```python
print(response.decode('utf-8'))
```

- Closing the connection

```python
client.close()
```

That's it for our TCP client, all the above code can be updated through your choice, infact I have added some Exceptions for the client like `KeyboardInterrupt` and printing the Exception rather than big scary lines of errors.

**All code for TCP client with `exceptions`:**

```python3
#!/usr/bin/env python3                                                                                                import socket
                                                           target_host = "0.0.0.0"                                    target_port = 8000

#create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #connect the client
    client.connect((target_host, target_port))

    #sending data
    client.send(b"Hey there, from our TCP client.")

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
```

## Making our TCP server

- Importing required libraries (`socket`, `threading`)

```python3
import socket
import threading
```

- Specifying IP and PORT for our server.

```python
IP = '0.0.0.0'
PORT = 8000
```
- Creating the socket object with required arguments.

```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
```
- Listening on the desired IP and PORT

```python
server.bind((IP, PORT))
server.listen(5)
print(f"[+] Listening on {IP}:{PORT}")
```
- Accepting connections

```python
try:
    while True:
    	client, address = server.accept()
        print(f"[+] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
```
- Adding exceptions

```python
except KeyboardInterrupt:
    print('\n[!] Exiting...')

except Exception as e:
    print('[!!] Server died due to', e)
```

- Handling clients and sending response

```python
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.send(b'Hey there, from TCP server.')
```

That's it for our server.

**All code for our server:**

```python
#!/usr/bin/env python3

import socket
import threading

IP = '0.0.0.0'
PORT = 8000

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[+] Listening on {IP}:{PORT}")

    try:
        while True:
            client, address = server.accept()
            print(f"[+] Accepted connection from {address[0]}:{address[1]}")
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()

    except KeyboardInterrupt:
        print('\n[!] Exiting...')

    except Exception as e:
        print('[!!] Server died due to', e)

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.send(b'Hey there, from TCP server.')

if __name__ == '__main__':
    main()
```


## Kicking off tires

- Starting the server

```bash
./server.py
```

Output:

```bash
┌──(Shinero@Voldemort)-[~]
└─$ ./server.py
[+] Listening on 0.0.0.0:8000
```

- Starting the client

```bash
./client.py
```

Output: 

```bash
┌──(Shinero@Voldemort)-[~]
└─$ ./client.py
Hey there, from TCP server.
```

**We got response from our server, now let's see the server output.**

*Server ouput:*

```bash
┌──(Shinero@Voldemort)-[~]
└─$ ./server.py
[+] Listening on 0.0.0.0:8000
[+] Accepted connection from 127.0.0.1:52884
[*] Received: Hey there, from TCP client.
```

If you have come till here and you have successfully created your own TCP client and server, **Congratulations!!**

___

Code for both [client](https://github.com/Sarthak2143/notes/blob/master/scripts/networking/tcp_client.py) and [server](https://github.com/Sarthak2143/notes/blob/master/scripts/networking/tcp_server.py) is on my [Github](https://github.com/Sarthak2143) too.

> If you like my work, you can support it by giving stars to my projects on my Github and following me on Github and [Twitter](https://twitter.com/voldemort_shin).

