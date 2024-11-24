class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self, speed):
        self.speed = speed

    def brake(self, speed):
        self.speed = speed


car = Car("Toyota", "Corolla")
car.accelerate(30)
print("Speed is ", car.speed)
car.brake(10)
print("Speed is ", car.speed)
