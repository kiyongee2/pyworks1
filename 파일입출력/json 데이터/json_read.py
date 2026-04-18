# json 데이터 읽기
import json
import os

# 현재 파일의 디렉터리 경로(path) 가져옴
# 절대 경로
base_dir = os.path.dirname(os.path.abspath(__file__))
print("디렉터리 이름:", base_dir)
file_path = os.path.join(base_dir, "products.json")
print("파일 경로:", base_dir) #파일 경로: c:\pyworks\파일입출력\json 데이터

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        # json.load(데이터)로 데이터 가져옴
        data = json.load(f)
        print(data)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 제품 정보 출력
print("첫번째 제품 정보")
print(f"ID: {data[0]['id']}") #ID: 1
print(f"Name: {data[0]['name']}") #Name: 무선 마우스
print(f"Price: {data[0]['price']}") #Price: 32000
print(f"Description: {data[0]['description']}") #Description: 무선 마우스에 대한 설명입니다.

print("\n제품 목록")
print('=' * 50)
for product in data:
    print(f"Id: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"Description: {product['description']}")
    print('-' * 50)
