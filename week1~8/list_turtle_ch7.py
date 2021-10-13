import turtle
import random

#전역변수
myTurtle, tX, tY, tColor, tSize, tShape = [None]*6
shapeList=[]
PlayerTurtles=[]
swidth, sheight = 500, 500

#main
if __name__ == "__main__" :
    turtle.title('거북이 리스트 활용')
    turtle.setup(width=swidth+50, height=swidth+50)
    turtle.screensize(swidth,sheight)

    shapeList=turtle.getshapes()
    for i in range(0,10) :
        random.shuffle(shapeList)
        myTurtle=turtle.Turtle(shapeList[0])
        tX=random.randrange(-swidth/2, sheight/2)
        tY=random.randrange(-swidth/2, sheight/2)
        r = random.random(); g=random.random(); b=random.random()
        tSize = random.randrange(1,3)
        xy_sum=tX+tY
        PlayerTurtles.append([myTurtle, tX, tY, tSize, r, g, b, xy_sum])

    #PlayerTurtles.sort(key=lambda x : x[1]+x[2])
    re_tur = sorted(PlayerTurtles, key=lambda turtles : turtles[7] ,reverse = True)
    #print(PlayerTurtles)
    
    for index, tList in enumerate(PlayerTurtles[0:]) :
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])
        if index == 0 :
            myTurtle.goto(tList[1], tList[2])
            continue
        myTurtle.goto(re_tur[index-1][1], re_tur[index-1][2]) # 선을 그을 거북이를 이 전의 거북이 위치로 이동
        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2])   #설정된 거북이의 좌표로 이동하면서 선 긋기
    
    turtle.done()