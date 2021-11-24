from tkinter import *
import math
import random

#슈퍼클래스
class Shape : 
    color, width = "", 0
    shX1, shY1, shX2, shY2 = [0]*4
    def drawShape(self) :
        raise NotImplementedError()

#사각형 서브클래스
class Rectangle(Shape) :
    object = None
    def __init__(self, x1, y1, x2, y2, c, w) :
        self.shX1=x1
        self.shY1=y1
        self.shX2=x2
        self.shY2=y2
        self.color=c
        self.width=w
        self.drawShape()

    def __del__(self) : #사각형의 선분 4개를 삭제
        for obj in self.object :
            canvas.delete(obj)

    def drawShape(self) : #사각형 그리기로 오버라이딩
        sx1=self.shX1
        sy1=self.shY1
        sx2=self.shX2
        sy2=self.shY2
        squreList=[]
        squreList.append(canvas.create_line(sx1,sy1,sx1,sy2, fill=self.color, width=self.width))
        squreList.append(canvas.create_line(sx1,sy2,sx2,sy2, fill=self.color, width=self.width))
        squreList.append(canvas.create_line(sx2,sy2,sx2,sy1, fill=self.color, width=self.width))
        squreList.append(canvas.create_line(sx2,sy1,sx1,sy1, fill=self.color, width=self.width))
        self.object=squreList #선분 리스트(사각형)를 objects 에 넣음

#원 서브 클래스
class Circle(Shape) :
    objects=None
    def __init__(self, x1, y1, x2, y2, c, w) :
        self.shX1=x1
        self.shY1=y1
        self.shX2=x2
        self.shY2=y2
        self.color=c
        self.width=w
        self.drawShape()

    def __del__(self) : #원은 객체 1개만 삭제
        canvas.delete(self.objects)

    def drawShape(self): #원형 그리기로 오버라이딩
        sx1=self.shX1
        sy1=self.shY1
        sx2=self.shX2
        sy2=self.shY2
        self.objects=canvas.create_oval(sx1,sy1,sx2,sy2, 
                                        outline=self.color, width=self.width)

#색상 선택 함수
def getColor() :
    r=random.randrange(16,256)
    g=random.randrange(16,256)
    b=random.randrange(16,256)
    return "#"+hex(r)[2:]+hex(g)[2:]+hex(b)[2:] # '#rrggbb' 형태

#임의의 펜 두께 선택
def getWidth() :
    return random.randrange(1,9)

#사각형 이벤트 함수
def startDrawRect(event):
    global x1, y1, x2, y2, shapes_rect
    x1=event.x
    y1=event.y
def endDrawRect(event) :
    global x1, y1, x2, y2, shapes_rect
    x2=event.x
    y2=event.y
    rect=Rectangle(x1,y1,x2,y2,getColor(),getWidth()) #사각형 생성
    shapes_rect.append(rect) #전체 도형 리스트에 추가

#원 이벤트 함수
def startDrawCircle(event) :
    global x1, y1, x2, y2, shapes_cir
    x1=event.x
    y1=event.y
def endDrawCircle(event) :
    global x1, y1, x2, y2, shapes_cir
    x2=event.x
    y2=event.y
    cir=Circle(x1,y1,x2,y2,getColor(),getWidth()) #원 생성
    shapes_cir.append(cir) #전체 도형 리스트에 추가

'''
#마지막에 그린 도형 제거
def deleteShape(event) :
    global shapes
    if len(shapes) != 0 :
        shp = shapes.pop()
        del(shp)
'''

#마지막에 그린 사각형 제거
def delete_rect(event) :
    global shapes_rect
    if len(shapes_rect) != 0 :
        shp = shapes_rect.pop()
        del(shp)

#마지막에 그린 원 제거
def delete_cir(event) :
    global shapes_cir
    if len(shapes_cir) != 0 :
        shp = shapes_cir.pop()
        del(shp)




#shapes=[]
shapes_rect=[]
shapes_cir=[]
window=None
canvas=None
x1, y1, x2, y2 = None, None, None, None

#main
if __name__ == "__main__" :
    window=Tk()
    window.title("201616043성연우")
    canvas=Canvas(window, height=300, width=300)
    canvas.bind("<Button-1>", startDrawRect)
    canvas.bind("<ButtonRelease-1>", endDrawRect)
    #canvas.bind("<Button-2>", deleteShape)
    #최근 사각형 제거
    canvas.bind("<Double-Button-1>", delete_cir)
    #최근 원 제거
    canvas.bind("<Double-Button-2>", delete_rect)
    canvas.bind("<Button-3>", startDrawCircle)
    canvas.bind("<ButtonRelease-3>", endDrawCircle)

canvas.pack()
window.mainloop()

