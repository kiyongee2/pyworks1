# 파일을 읽기

# 파일 열기 - open(경로, 읽기모드)
try:
    f = open("C:/pyfile/file1.txt", 'r')

    # 파일 읽기 - read()
    content = f.read()
    print(content)
    # 파일 닫기
    f.close()
except FileNotFoundError as e:
    print(e)

