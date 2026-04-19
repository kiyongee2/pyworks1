
import pandas as pd

# 엑셀 파일 읽기 - read_excel() 함수 사용
df = pd.read_excel('지출내역.xlsx')

print(df.head())

print('\n[지출 내역]')
print(df['지출액'])

print('\n[분류별 합계]')
print(df.groupby('분류')['지출액'].sum().sort_values(ascending=False))