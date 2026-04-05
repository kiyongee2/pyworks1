
import random

# 1~100 사이 랜덤 숫자 생성
target = random.randint(1, 100)

count = 0  # 시도 횟수

print("🎯 숫자 맞히기 게임 시작!")
print("1 ~ 100 사이의 숫자를 맞혀보세요.")

while True:
    try:
        guess = int(input("숫자를 입력하세요: "))
        count += 1

        if guess < target:
            print("↑ 더 큰 숫자입니다!")
        elif guess > target:
            print("↓ 더 작은 숫자입니다!")
        else:
            print(f"🎉 정답입니다! {count}회 만에 맞추셨습니다!")
            break

    except ValueError:
        print("⚠️ 숫자를 입력해주세요!")