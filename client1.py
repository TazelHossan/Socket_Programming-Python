import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port =12345
s.connect((host,port))
print("This is The Client...")


con = True
while con:
    msg  =input("Client,write message::")
    s.send(msg.encode("utf-8"))
    msg = s.recv(1023)
    msg = msg.decode("utf-8")
    print(msg)
    if(msg=="exit"):
        con = False
        s.close()
