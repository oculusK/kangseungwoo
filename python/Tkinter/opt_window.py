from tkinter import *

root = Tk() # Tk instance 생성

root.title("opt window") # 창 이름 설정
root.geometry("300x200+300+300") # 창 크기 + 창 좌표 설정, 띄어쓰기하면 안됨
root.resizable(False, False) # 창 크기 변경 가능 여부

root.mainloop() # Tk 화면 호출
