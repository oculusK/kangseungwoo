import tkinter as tk
import cv2
import socket
import threading
import numpy as np

# GUI 초기화
window = tk.Tk()
window.title("웹캠 채팅 클라이언트")

# 웹캠 초기화
cap = cv2.VideoCapture(0)

# 소켓 설정
HOST = '127.0.0.1'  # 서버 IP 주소
PORT = 8080  # 서버 포트 번호
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# 메시지 입력 필드
message_entry = tk.Entry(window, width=30)
message_entry.grid(row=1, column=30, padx=10, pady=5, sticky="sw")

# 메시지 창 (리스트 박스)
message_listbox = tk.Listbox(window, width=35, height=15)
message_listbox.grid(row=0, column=30, padx=10, pady=10, sticky="w")

# 웹캠 영상 표시 레이블
video_label = tk.Label(window)
video_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

# 웹캠 영상 업데이트 함수
def update_video():
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            video_label.img = img
            video_label.config(image=img)
            video_label.after(10, update_video)

# 메시지 수신 함수
def receive_message():
    while True:
        try:
            data = s.recv(1024)
            if not data:
                break
            message_listbox.insert(tk.END, "상대방: " + data.decode())
        except:
            break

# 메시지 전송 함수
def send_message():
    message = message_entry.get()
    s.send(message.encode())
    message_listbox.insert(tk.END, "나: " + message)
    message_entry.delete(0, tk.END)

# 스레드 시작
video_thread = threading.Thread(target=update_video)
video_thread.start()

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# 전송 버튼
send_button = tk.Button(window, text="전송", command=send_message)
send_button.grid(row=1, column=31, padx=10, pady=5, sticky="sw")

# GUI 실행
window.mainloop()
