import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = {}
lock = threading.Lock()

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            pass

def handle_client(client_socket):
     with (lock):
         clients[client_socket] = f"client{len(clients) + 1}"
         name = clients[client_socket]

     broadcast(f"[SERVER] {name} joined the chat\n")

     try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode().strip()

            if message.startswith("/name "):
                new_name = message.split(" ", 1)[1]
                with lock:
                    old_name = clients[client_socket]
                    clients[client_socket] = new_name
                broadcast(f"[SERVER] {old_name} is now {new_name}\n")
            else:
                name = clients[client_socket]
                broadcast(f"[{name}]: {message}\n")

     except:
        pass
     finally:
        with lock:
            name = clients.pop(client_socket,"unknown")
        broadcast(f"[SERVER] {name} left the chat\n")
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()

    print(f"Server started on {HOST}: {PORT}")

    while True:
        client_socket, _ = server.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket,),
            daemon=True
        )
        thread.start()

if __name__ == "__main__":
    start_server()





