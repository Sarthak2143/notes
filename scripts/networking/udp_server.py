import socket
import threading

IP = "0.0.0.0"
PORT = 8000

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((IP, PORT))
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target = handle_client, args = (client, ))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recvfrom(4096)
        print(f"[+] Recieved: {request.decode('utf-8')}")
        sock.sendto(b'Never gonna let you down.', (addr[0], addr[1]))


if __name__ == "__main__":
    main()

