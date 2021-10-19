import turtle
import random
import math
from tkinter.simpledialog import *

#전역변수
inStr=" "
swidth, sheight=300, 300
tX, tY, txtSize=[0]*3

#main
turtle.title("거북이 글자쓰기")
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr=askstring('문자열입력', '거북이 쓸 문자열을 입력')

for i, ch in enumerate(inStr) :
    radian=math.radians(360/len(inStr))*i
    if i == 0 :
        tX=100
        tY=0
    else :
        tX=100*math.cos(radian)
        tY=100*math.sin(radian)
        
    
    r=random.random(); g=random.random(); b=random.random()
    txtSize=20

    turtle.goto(tX,tY)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))

turtle.done()
