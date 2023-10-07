import socket
#port = int(input("Port No: "))
PORT = 2500
HOST = 'localhost'
#address = ("localhost", port)
address = (HOST, PORT) # 주소는 항상 (ip, port) 튜플
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address) # 서버 연결 요청
while True:
    msg = input("Message to send: ")

    if not msg:
        continue
    try:
        s.send(msg.encode()) # 메시지 서버로 보내기
    except:
        print("연결 종료")
        break

    #data = s.recv(BUFSIZE)
    #print("Received message: %s" %data.decode())