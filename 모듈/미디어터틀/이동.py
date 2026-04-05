import turtle

turtle.shape("turtle")

'''
turtle.forward(100) #100 픽셀만큼 직진
turtle.right(90) #오른쪽 90도 방향
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
'''

"""
turtle.color('blue')
# 반복문 사용
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.color('red')
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
"""
turtle.color('blue')
turtle.pensize(2)
n = 4  #변의 개수
d = 150 #거리(distance)
# 사각형
for i in range(n):
    turtle.forward(d)
    turtle.right(360/n)

turtle.color('red')
turtle.pensize(3)
n = 3  #변의 개수
d = 75 #거리(distance)
# 삼각형
for i in range(n):
    turtle.forward(d)
    turtle.right(360/n)
# 원
turtle.color('black')
turtle.circle(50) #반지름 - 50픽셀

turtle.mainloop() #윈도우(창) 계속 유지