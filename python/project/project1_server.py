import socket
import cv2
import threading
from UI import VideoChatUI
import tkinter as tk
from scapy.all import *

class VideoChatServer:
    def __init__(self, host, port):
        self.UI = VideoChatUI(tk.Tk(), "영상 채팅 서버")     # tkinter 연결, 프로그램 제목
        self.UI.on_send_message = self.send_message_to_clients  # 메시지를 누르면 클라이언트에게 감
        self.clients = [] # 클라이언트 list 선언

        # 웹캠 초기화
        self.cap = cv2.VideoCapture(0) # 0 = 기본카메라, 1 = 두번째 카메라, '.mp4' = 비디오 파일 읽기

        # 소켓 초기화
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(10) # 10개까지 연결 가능

        # 웹캠 영상 전송 스레드 시작
        self.webcam_thread = threading.Thread(target=self.send_webcam)
        self.webcam_thread.daemon = True
        self.webcam_thread.start()

        # 클라이언트 연결을 처리하는 스레드 시작
        self.receive_thread = threading.Thread(target=self.receive_clients)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        # 서버 GUI 시작
        tk.mainloop()

        # 패킷 분석
        while True:
            sniff(iface="Software Loopback Interface 1", prn=lambda x: x.show())

    def send_message_to_clients(self, message):
        for client in self.clients:
            client.send(message.encode())

        # 서버 UI에도 메시지 표시
        self.UI.receive_message("서버: " + message)

    def send_webcam(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                continue
            _, encoded_frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
            encoded_frame = encoded_frame.tobytes()
            for client in self.clients:
                try:
                    client.send(encoded_frame)
                except:
                    self.clients.remove(client)

            # 서버 UI에 비디오 화면 표시
            self.UI.show_frame(frame)

    def receive_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode("utf-8")
                if not message:
                    break
                self.send_message_to_clients(message)  # 받은 메시지를 다른 클라이언트에게 전송
            except:
                pass

if __name__ == "__main__":
    server = VideoChatServer('', 2323)  # 호스트 및 포트를 지정하여 서버를 시작합니다.