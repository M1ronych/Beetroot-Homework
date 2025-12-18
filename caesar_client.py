import socket

HOST = "127.0.0.1"
PORT = 5000

key = int(input("Enter Caesar key: "))
message = input("Enter message: ")

payload = f"{key};{message}"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(payload.encode(),(HOST,PORT))

#with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    #client.connect((HOST,PORT))
    #client.sendall(payload.encode())

    #response = client.recv(1024).decode()

data, _ = sock.recvfrom(1024)
print("Encrypted response:",data.decode())