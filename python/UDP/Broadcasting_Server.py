from socket import *

addr = ('<broadcast>',10000) # broadcast 주소

# broadcast를 위한 socket 설정
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) # broadcast 옵션 설정

while True:
	smsg = input('Broadcast Message: ')
	sock.sendto(smsg.encode(), (addr)) # broadcast 메시지 전송