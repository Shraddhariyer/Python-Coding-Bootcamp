#encapsulation

class Fan():
    def __init__(self):
        self.__speed=0

    def increaseSpeed(self):
        self.__speed=self.__speed+1
        print("Speed Increased..")
        print("Current speed:",self.__speed)

fan=Fan()
fan.increaseSpeed()
fan._Fan__speed=10
fan.increaseSpeed()