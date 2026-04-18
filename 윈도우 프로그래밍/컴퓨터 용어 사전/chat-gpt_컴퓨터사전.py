
import tkinter as tk
from tkinter import messagebox

# 컴퓨터 용어 사전 데이터
computer_dict = {
    "CPU": "컴퓨터의 중앙처리장치로 연산과 제어를 담당합니다.",
    "RAM": "실행 중인 프로그램 데이터를 임시 저장하는 메모리입니다.",
    "SSD": "데이터를 저장하는 반도체 기반 저장장치입니다.",
    "HDD": "자기 디스크 방식의 저장장치입니다.",
    "GPU": "그래픽 처리 장치로 영상 및 게임 연산을 담당합니다.",
    "OS": "운영체제로 컴퓨터 자원을 관리하는 시스템 소프트웨어입니다.",
    "Python": "쉽고 강력한 프로그래밍 언어입니다.",
    "Java": "객체지향 프로그래밍 언어입니다.",
    "HTML": "웹 페이지 구조를 만드는 마크업 언어입니다.",
    "CSS": "웹 페이지 디자인을 담당하는 스타일 언어입니다.",
    "JavaScript": "웹 페이지 동작을 구현하는 프로그래밍 언어입니다.",
    "Database": "데이터를 저장하고 관리하는 시스템입니다.",
    "Network": "컴퓨터끼리 연결하여 데이터를 주고받는 시스템입니다.",
    "Server": "요청을 처리하고 서비스를 제공하는 컴퓨터입니다.",
    "Client": "서버에 요청을 보내 서비스를 이용하는 사용자 측 장치입니다."
}

# 검색 기능
def search_word():
    word = entry.get().strip()

    if word in computer_dict:
        result_label.config(text=f"[{word}] 뜻:\n{computer_dict[word]}")
    else:
        result_label.config(text="해당 단어가 사전에 없습니다.")

# 전체 단어 보기
def show_all_words():
    words = "\n".join(computer_dict.keys())
    messagebox.showinfo("전체 단어 목록", words)

# GUI 창 생성
root = tk.Tk()
root.title("컴퓨터 용어 사전")
root.geometry("500x400")
root.resizable(False, False)

# 제목
title_label = tk.Label(root, text="컴퓨터 용어 사전", font=("맑은 고딕", 18, "bold"))
title_label.pack(pady=15)

# 입력창
entry = tk.Entry(root, font=("맑은 고딕", 14), width=25)
entry.pack(pady=10)

# 검색 버튼
search_btn = tk.Button(root, text="검색", font=("맑은 고딕", 12), width=12, command=search_word)
search_btn.pack(pady=5)

# 전체 단어 보기 버튼
all_btn = tk.Button(root, text="전체 단어 보기", font=("맑은 고딕", 12), width=12, command=show_all_words)
all_btn.pack(pady=5)

# 결과 출력
result_label = tk.Label(root, text="", font=("맑은 고딕", 12), wraplength=450, justify="left")
result_label.pack(pady=20)

# 실행
root.mainloop()