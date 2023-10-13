import socket
import cv2
import threading
import tkinter as tk
from UI import VideoChatUI


class VideoChatClient:
    def __init__(self, host, port):
        self.UI = VideoChatUI(tk.Tk(), "영상 채팅 클라이언트") # tkinter 연결, 프로그램 제목
        self.UI.on_send_message = self.send_message_to_server   # 서버에게 메시지 보내기

        # 소켓 초기화
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 연결
        self.client_socket.connect((host, port))

        # 웹캠 초기화
        self.cap = cv2.VideoCapture(1) # 0 = 기본카메라, 1 = 두번째 카메라, '.mp4' = 비디오 파일 읽기

        # 비디오 프레임 송신 스레드 시작
        self.video_thread = threading.Thread(target=self.send_webcam)
        self.video_thread.daemon = True
        self.video_thread.start()

        # 메시지 수신 스레드 시작
        self.receive_thread = threading.Thread(target=self.receive_message)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        # 클라이언트 GUI 시작
        self.UI.start()

    def send_webcam(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                continue
            _, encoded_frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
            encoded_frame = encoded_frame.tobytes()
            self.client_socket.send(encoded_frame)

    def send_message_to_server(self, message):
        self.client_socket.send(message.encode())

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.UI.receive_message("클라이언트 : " + message)
            except Exception as e:
                print("메시지 수신 오류:", e)
                break


if __name__ == "__main__":
    client = VideoChatClient('localhost', 2323)  # 서버의 IP 주소와 포트 번호를 지정하세요
