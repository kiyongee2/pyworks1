# 컴퓨터 용어 사전 만들기 (단어 등록 기능 추가)
from tkinter import *
from tkinter import messagebox

dict = {
    "알고리즘": "문제를 해결하기 위한 절차나 방법",
    "함수": "특정 작업을 수행하는 코드 블록",
    "변수": "데이터를 저장하는 공간",
    "이진수": "0과 1로 이루어진 수 체계",
}

# 검색 함수 정의
def search():
    word = search_entry.get().strip()
    meaning = dict.get(word, "해당 용어가 사전에 없습니다.")
    output.delete(1.0, END)
    output.insert(END, meaning)

# 단어 등록 함수 정의
def register():
    word = reg_word_entry.get().strip()
    meaning = reg_meaning_entry.get().strip()

    if not word:
        messagebox.showwarning("입력 오류", "단어를 입력해주세요.")
        return
    if not meaning:
        messagebox.showwarning("입력 오류", "뜻을 입력해주세요.")
        return
    if word in dict:
        messagebox.showwarning("등록 오류", f"'{word}'은(는) 이미 사전에 등록된 단어입니다.")
        return

    dict[word] = meaning
    reg_word_entry.delete(0, END)
    reg_meaning_entry.delete(0, END)
    messagebox.showinfo("등록 완료", f"'{word}' 단어가 등록되었습니다.")

window = Tk()
window.title("컴퓨터 용어 사전")

# ── 검색 영역 ──────────────────────────────────────────
Label(window, text='컴퓨터 용어 사전', font=('', 12, 'bold')) \
    .grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky=W)

Label(window, text='검색어:') \
    .grid(row=1, column=0, padx=10, pady=5, sticky=W)

search_entry = Entry(window, width=30)
search_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

Button(window, text='검색', command=search) \
    .grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=W)

output = Text(window, width=45, height=8)
output.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=W)

# ── 구분선 ──────────────────────────────────────────────
Frame(window, height=2, bd=1, relief=SUNKEN, bg='gray') \
    .grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=EW)

# ── 단어 등록 영역 ──────────────────────────────────────
Label(window, text='단어 등록', font=('', 11, 'bold')) \
    .grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 5), sticky=W)

Label(window, text='단어:') \
    .grid(row=6, column=0, padx=10, pady=5, sticky=W)

reg_word_entry = Entry(window, width=30)
reg_word_entry.grid(row=6, column=1, padx=10, pady=5, sticky=W)

Label(window, text='뜻:') \
    .grid(row=7, column=0, padx=10, pady=5, sticky=W)

reg_meaning_entry = Entry(window, width=30)
reg_meaning_entry.grid(row=7, column=1, padx=10, pady=5, sticky=W)

Button(window, text='등록', command=register) \
    .grid(row=8, column=0, columnspan=2, padx=10, pady=(5, 15), sticky=W)

window.mainloop()
