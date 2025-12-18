import socket
HOST = "127.0.0.1"
PORT = 5000

def caesar_encrypt(text:str,shift:int) -> str:
    result = []

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower else ord('A')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)

    return "".join(result)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((HOST,PORT))

print("UDP server is running...")

while True:
    data,addr = sock.recvfrom(1024)
    message = data.decode()

    key_str,text = message.split(";",1)
    key = int(key_str)

    encrypted = caesar_encrypt(text,key)
    sock.sendto(encrypted.encode(),addr)