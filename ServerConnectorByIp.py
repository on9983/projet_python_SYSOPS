import socket, json
from serverCommands.MakeScanCommand import MakeScanCommand


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()),9999))
s.listen(5)
while True:
    SVR, address = s.accept()
    print("Connexion à "+str(address)+" réussie.")

    for i in range(2):
        msg = SVR.recv(9999).decode("utf8")
        print(msg)

        if(msg == "MakeScan"):
            data = MakeScanCommand.startScan()
            SVR.send(bytes(json.dumps(data), "utf-8"))
        i-=1







