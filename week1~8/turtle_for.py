import turtle
import random
#전역 변수
swidth, sheight, pSize = 500, 500, 3
#각도 - 30
r, g, b, angle, dist, = 0, 0, 0, 30, 5
 
#메인 함수
turtle.title('거북이로 소라 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth, sheight)
 
for i in range(80) :
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
 
    dist += 1   #그리는 선의 길이를 1씩 증가
    turtle.forward(dist)
    turtle.left(angle)  #왼쪽으로 30도 씩 회전
 
turtle.done()