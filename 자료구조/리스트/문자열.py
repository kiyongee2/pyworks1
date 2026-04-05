# 문자열 다루기
my_list = ['s', 'k', 'y']
print(my_list[0]) #s
print(my_list[-1]) #y

# 슬라이싱(범위로 검색) - 끝인덱스: 끝번호-1
print(my_list[0:2]) #['s', 'k']
print(my_list[0:3]) #['s', 'k', 'y']
print(my_list[:]) #['s', 'k', 'y']

# 문자열 - 특별한 1차원 리스트
greeting = "Hello"
print(greeting[0]) #h
print(greeting[-1]) #o
print(greeting[:-1]) #hell

# 대,소문자 변환 - 대문자: upper(), 소문자: lower()
print(greeting.upper())  #HELLO
print(greeting.lower()) #hello

# split(구분기호) - 문자열을 구분기호로 분리하는 함수
csv = "apple,banana,strawberry"
print(csv) #apple,banana,strawberry

fruits = csv.split(',') #문자열이 리스트로 변환됨
print(fruits) #['apple', 'banana', 'strawberry']
print(fruits[0]) #apple
print(fruits[-1]) #strawberry

# replace(변경전 문자, 변경후 문자)
s1 = "Hello, World"
print(s1.replace('World', 'Korea')) # Hello, Korea

# find(문자열) - 문자열의 시작 위치 찾기
s2 = "Python Programming"
print(s2.find("Python")) #0
print(s2.find("Happy")) #-1 #찾는 문자가 없으면 -1 반환

if s2.find("Python") != -1:
    print("파이썬에 관련한 교재입니다.")
else:
    print("파이썬에 관련한 교재가 아닙니다.")