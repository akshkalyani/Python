import socket

s = socket.socket()
print("socket created succesfully")

s.bind(('localhost',9997))
s.listen(3)
print("waiting for connection")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connection estab lished with", addr, name)

    c.send(bytes("Welcome to ABABSD",'utf-8'))
