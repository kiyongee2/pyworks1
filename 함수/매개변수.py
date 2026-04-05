
# 기본 매개 변수
def greet(name, message="안녕하세요"):
    print(f"{name}님, {message}")

# 인자(매개변수)를 모두 전달한 경우
greet("민주", "반갑습니다.")

# 기본 매개변수를 생략한 경우
greet("영우")

# 버스 요금 함수
def take_bus(fare=1500):
    print(f"버스 요금은 {fare}원 입니다.")

take_bus()
take_bus(1500)
take_bus(1700)