import socket, json
from serverCommands.MakeScanCommand import MakeScanCommand



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.15.18",1519))



msg = s.recv(55300).decode("utf8")
print(msg)

if(msg == "MakeScan"):
    data = MakeScanCommand.startScan()
    s.send(bytes(json.dumps(data), "utf-8"))

s.close()






