#abstraction

from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def makeCoffee(self):
        pass

class Latte(Coffee):
    def makeCoffee(self):
        print("Making Latte")

class Mocha(Coffee):
    def makeCoffee(self):
        print("Making Mocha")


coffee1=Latte()
coffee2=Mocha()

coffee1.makeCoffee()
coffee2.makeCoffee()






