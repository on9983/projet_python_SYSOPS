import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.15.18",55300))

msg = s.recv(55300)
print(msg.decode("utf8"))