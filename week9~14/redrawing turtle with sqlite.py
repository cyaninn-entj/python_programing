import turtle
import random
import sqlite3

con, cur, row = None, None, None
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0]*7
con=sqlite3.connect("D:/SQLite/naverDB")
cur=con.cursor()

cur.execute("CREATE TABLE turtleTB3 (Line_ID int(6), R float(8), G float(8), B float(5), Turn INT(6), X int(6), Y int(6))")
con.commit()


turtle.title("201616043성연우")
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth, sheight)

lind_ID=1
turn=1
while True : 
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor((r,g,b))
    

    angle=random.randrange(0,360)
    dist=random.randrange(1,100)
    turtle.left(angle)
    turtle.forward(dist)
    curX=round(turtle.xcor())
    curY=round(turtle.ycor())
    mystr="INSERT INTO turtleTB3 VALUES('"+str(lind_ID)+"','"+str(r)+"','"+str(g)+"','"+str(b)+"','"+str(turn)+"','"+str(curX)+"','"+str(curY)+"')"
    turn+=1

    if (-swidth/2 <= curX and curX <= swidth/2) and (-sheight/2 <= curY and curY <= sheight/2) :
        pass
    else : 
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        turn=1
        lind_ID+=1

        exitCount+=1
        if exitCount >= 5 :
            break

    cur.execute(mystr)

con.commit()
turtle.clear()

for i in range(lind_ID-1, -1, -1):
    sql = "SELECT * FROM turtleTB3 WHERE Line_ID = ('" + str(i) + "')"
    cur.execute(sql)
    rows = cur.fetchall()
    turtle.penup()
    for g in range(len(rows)-1, -1, -1):
        turtle.goto(rows[g][5], rows[g][6])
        turtle.down()
        turtle.pencolor((rows[g][1], rows[g][2], rows[g][3]))

    turtle.goto(0, 0)


turtle.done()