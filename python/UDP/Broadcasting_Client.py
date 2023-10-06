from socket import *

sock = socket(AF_INET, SOCK_DGRAM) # broadcasting을 위해 UDP socket 사용
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # 주소 재사용
sock.bind(('', 10000))

while True:
    msg, addr = sock.recvfrom(1024) # receive message
    print(msg.decode())