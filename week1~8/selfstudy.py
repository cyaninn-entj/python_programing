import turtle
 
## 전역 변수 부분 ##
num1, num2, res = 0, 0, 0
swidth, sheight = 1000, 500
curX, curY = 0, 0
 
## 2진수를 거북이로 표현하는 함수 ##
def binaryToTurtle(binary, num):    # 10진수 num과 num을 2진수로 바꾼 binary를 인자로 받음
    curX = swidth / 2
 
    # main 부분에서 실제 거북이를 찍는 부분만 따로 가져옴
    for i in range(len(binary) - 2) :
        turtle.goto(curX, curY)
        if num & 1:
            turtle.color('red')
            turtle.turtlesize(2)
            turtle.stamp()
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
            turtle.stamp()
        curX -= 50
        num >>= 1 
 
## 메인 코드 부분 ##
if __name__ == "__main__":
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)
 
    ## 두 개의 숫자를 입력받음 ##
    num1, num2 = map(int, input("숫자를 2개 입력하세요 : ").strip().split(' '))
    curY = 0        # 첫 번째 숫자 출력할 Y축 위치
    binaryToTurtle(bin(num1), num1)
    curY = -50       # 두 번째 숫자 출력할 Y축 위치
    binaryToTurtle(bin(num2), num2)
    curY = -100      # 결과 값 출력할 Y축 위치
    res = num1 & num2 
    binaryToTurtle(bin(res), res)   # 입력받은 두 숫자를 &연산 해 인자로 넘김
 
 
turtle.done()



