class Car : 
    speed=0
    def upSpeed(self, value) :
        self.speed+=value
        print("현재 최고 속도(슈퍼클래스) : %d" % self.speed)

class Sedan(Car) :
    def upSpeed(self, value):
        self.speed+=value
        if self.speed>150 :
            self.speed=150
        print("현재 속도(서브클래스) : %d" % self.speed)

class Truck(Car) :
    pass

class Sonata(Sedan) :
    pass

sedan1, truck1 = None, None

truck1=Truck()
sedan1=Sedan()
sonata=Sonata()

print("트럭 ->", end="")
truck1.upSpeed(200)
print("승용차 ->", end="")
sedan1.upSpeed(200)
print("소나타 ->", end="")
sonata.upSpeed(200)
        