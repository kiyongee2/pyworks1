
import pandas as pd

df = pd.read_csv('expenses.csv')
print(df)

# 천단위 구분 쉼표 추가
def format_amount(x):
    return f"{x:,}원"

print("\n[지출 내역]")
print(df['amount'].apply(format_amount)) 

print("\n[카테고리별 합계]")
category_sum = df.groupby('category')['amount'].sum().sort_values(ascending=False)
print(category_sum.apply(format_amount))

monthly_total = df['amount'].sum()
print(f"총 지출: {monthly_total:,}원")

print("\n[절약 목표 제안]")
print(f'다음 달 목표 지출: {int(monthly_total*0.9):,}원(10% 절감)')