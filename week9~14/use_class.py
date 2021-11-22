class Car : 
    color=""
    speed=0

    def upSpeed(self, value) :
        if value>150 :
            value=150
            self.speed+=value
        else :
            self.speed+=value
    def downSpeed(self, value) : 
        self.speed-=value

myCar1=Car()
myCar1.color="빨강"
myCar1.speed=0

myCar2=Car()
myCar2.color="파랑"
myCar2.speed=0

myCar3=Car()
myCar3.color="노랑"
myCar3.speed=0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(200)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar3.color, myCar3.speed))