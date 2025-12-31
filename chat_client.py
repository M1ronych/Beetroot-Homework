import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message, end="")
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to server")
    print("Commands:")
    print("/name <your_name>")
    print("/quit")

    thread = threading.Thread(
        target=receive_messages,
        args=(client,),
        daemon=True
    )
    thread.start()

    while True:
        msg = input()
        if msg == "/quit":
            client.close()
            break
        client.send(msg.encode())

if __name__ == "__main__":
    start_client()

