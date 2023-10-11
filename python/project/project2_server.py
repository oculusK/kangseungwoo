import socket
import threading

# 소켓 설정
HOST = '127.0.0.1'  # 서버 IP 주소
PORT = 8080  # 서버 포트 번호

# 소켓 생성 및 연결 대기
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# 클라이언트 관리를 위한 리스트
clients = []

# 클라이언트와의 연결 관리 함수
def client_handler(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            for client in clients:
                client.send(data)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# 채팅 서버 시작
print(f"서버가 {HOST}:{PORT}에서 실행 중입니다.")

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=client_handler, args=(client_socket,))
    client_thread.start()
