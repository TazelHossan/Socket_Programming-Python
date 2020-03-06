import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port =12345
s.bind((host,port))
print("This is The Server...")
s.listen(5)
socketClient , address =s.accept()
print("Got connection from",address)

con = True
while con:
    msg = socketClient.recv(1023)
    msg = msg.decode("utf-8")
    print(msg)
    msg = input("Server,write message::")
    socketClient.send(msg.encode("utf-8"))
    if(msg=="exit"):
        con=False
        s.close()


