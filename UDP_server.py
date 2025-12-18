import socket
HOST = "127.0.0.1"
PORT = 5000

def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((HOST,PORT))

    print(f"UDP stver run on {HOST}:{PORT}")

    while True:
        data,client_address = server_socket.recvfrom(1024)

        print(f"Received from {client_address}:{data.decode()}")

        server_socket.sendto(data,client_address)

if __name__ == "__main__":
    main()