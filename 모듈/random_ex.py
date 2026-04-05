import random 

# 0.0 이상 1.0 미만의 실수 난수 생성
# print(random.random())

# 시드 설정 - 처음 한 번만 난수가 생성됨
# random.seed(12)
# print(random.random())

# 1 ~ 10 사이의 정수 난수 생성 - randint(시작, 끝)
# print(random.randint(1, 10))

# 주사위 눈 
# dice = random.randint(1, 6)
# print("주사위 눈:", dice)

# 주사위 10번 굴리기
for i in range(10):
    dice = random.randint(1, 6)
    # print(dice)

# 리스트에서 요소 랜덤 선택 - choice()
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

# 동전 던지기
coin = random.choice(["앞면", "뒷면"])
print(coin)

# 로또 번호 생성 - 6개의 고유한 숫자 선택 : sample()
lotto = random.sample(range(1, 46), 6)
print(lotto)

