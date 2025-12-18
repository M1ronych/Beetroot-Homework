import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

def main():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        message = input("Enter a message (exit to quit): ")

        if message.lower() == "exit":
            break

        client_socket.sendto(
            message.encode(),
            (SERVER_HOST,SERVER_PORT)
        )

        data, _ = client_socket.recvfrom(1024)
        print("Answer from server:",data.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
