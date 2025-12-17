import socket
from multiprocessing import Process

HOST = "127.0.0.1"
PORT = 5000

def handle_client(conn,addr):
    print(f"Connected client {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            print(f"Taken from {addr}:{data.decode()}")
            conn.sendall(data)

    finally:
        conn.close()
        print(f"Client {addr} closed")

def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((HOST,PORT))
    server_socket.listen()

    print(f"Echo server is open on {HOST}:{PORT}")

    while True:
        conn,addr = server_socket.accept()

        process = Process(
            target=handle_client,
            args=(conn,addr)
        )
        process.start()

        conn.close()

if __name__ == "__main__":
    main()

    



