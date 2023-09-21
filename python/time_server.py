# time_server.py
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5000)
s.bind(address)
s.listen(5)
client, addr = s.accept()

while True:
    #client, addr = s.accept()
    print("Connection requested from ", addr)
    if client:
        time.sleep(1)
        client.send(time.ctime(time.time()).encode())
    #client.close() # 소켓 종료