import turtle
import math
import random
 
## 전역 변수 선언 부분 ##
t1, t2, t3 = [None] * 3
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6
swidth, sheight = 300, 300
 
         
## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북이 만나기')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
 
    t1 = turtle.Turtle('turtle'); t1.color('red'); t1.speed(10); t1.penup()
    t2 = turtle.Turtle('turtle'); t2.color('green'); t2.speed(10); t2.penup()
    t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.speed(10); t3.penup()
 
    t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100)
 
    while True:
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t1.left(angle); t1.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t2.left(angle); t2.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t3.left(angle); t3.forward(dist)
 
        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()
 
        ## 각 거북이가 화면 밖으로 나가면 각자의 처음 위치로 이동시키는 부분
        if not((-swidth / 2 <= t1X and t1X <= swidth / 2) and 
        (-sheight / 2 <= t1Y and t1Y <= sheight / 2)):
            t1.goto(-100, -100)
        if not((-swidth / 2 <= t2X and t2X <= swidth / 2) and 
        (-sheight / 2 <= t2Y and t2Y <= sheight / 2)):
            t2.goto(0, 0)
        if not((-swidth / 2 <= t3X and t3X <= swidth / 2) and 
        (-sheight / 2 <= t3Y and t3Y <= sheight / 2)):
            t3.goto(100, 100)
        ## y축의 +, - 부분을 넘었는지 체크해서 현재 거북이 좌표가 참이면 처음 위치로 이동시킴
 
        ## 각각 두 거북이가 만났을 때 도장을 찍는 부분 ##
        if math.sqrt(((t1X - t2X) * (t1X - t2X)) + ((t1Y - t2Y) * (t1Y - t2Y))) <= 20 :
            t1.stamp(); t2.stamp()
        elif math.sqrt(((t1X - t3X) * (t1X - t3X)) + ((t1Y - t3Y) * (t1Y - t3Y))) <= 20 :
            t1.stamp(); t3.stamp()
        elif math.sqrt(((t2X - t3X) * (t2X - t3X)) + ((t2Y - t3Y) * (t2Y - t3Y))) <= 20 :
            t2.stamp(); t3.stamp()
        ## t1-t2, t2-t3, t1-t3 경우를 모두 기재해줌
 
turtle.done()