import socket
import cv2
import numpy as np

# socket에서 수신한 버퍼를 반환하는 함수
def recvall(sock, count):
    # 바이트 문자열
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def handler(s): # 클라이언트와 연결을 관리하는 함수(핸들러 함수)
    while True:
        try:
            # 클라이언트로부터 데이터 수신
            data = s.recv(1024)
            if not data:
                break

            # 수신 데이터를 모든 클라이언트에게 전송
            for client in clients:
                client.send(data)
        except:
            # 오류 발생시 클라이언트 종료
            clients.remove(s)
            s.close()
            break

# 서버 설정
HOST = ''
PORT = 8080

# 클라이언트 저장을 위한 리스트
clients = []

# TCP 사용
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created')

# 서버의 아이피와 포트번호 지정
s.bind((HOST, PORT))
print('Socket bind complete')
# 클라이언트의 접속을 기다린다. (클라이언트 연결을 10개까지 받는다)
s.listen(10)
print('Socket now listening')

# 연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
conn, addr = s.accept()

while True:
    # client에서 받은 stringData의 크기 (==(str(len(stringData))).encode().ljust(16))
    length = recvall(conn, 16)
    stringData = recvall(conn, int(length))
    data = np.frombuffer(stringData, dtype='uint8')

    # data를 디코딩한다.
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imshow('ImageWindow', frame)
    cv2.waitKey(1)

# 클라이언트 연결 수락 및 스레드 생성
while True:
    client_socket, addr = s.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handler, args=(client_socket,))
    client_thread.start()