#To make use of oops concepts to create a car object

class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
        self.speed=0
    
    def start(self):
        print(self.brand,self.model,"Has Started..")

    def accelerate(self):
        self.speed=self.speed+10
        print("Current speed:",self.speed)

    def brake(self):
        self.speed=self.speed-10
        if self.speed<0:
            self.speed=0
        print("Current speed:",self.speed)

car1=Car("BMW","X5")
#car2=Car("Audi","A6")
car1.start()
car1.accelerate()
car1.accelerate()
car1.brake()