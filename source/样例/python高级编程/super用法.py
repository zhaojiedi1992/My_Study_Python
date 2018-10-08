class Car():
    def say(self):
        print("car")
class HongQiCar(Car):
    def say(self):
        Car.say(self)
        print("HongqiCar")

class HongQiCar2(Car):
    def say(self):
        super().say()
        print("HongqiCar")
#HongQiCar().say()
HongQiCar2().say()
