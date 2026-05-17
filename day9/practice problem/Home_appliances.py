#to demonstrate the working of all 4 advanced oops concepts
from abc import ABC, abstractmethod
class Appliances(ABC):

    def __init__(self):
        self.__power_status="Off"  #encapsulation

    def turnOn(self):
        self.__power_status="On" 
        print("Machine is turned ",self.__power_status)  #inheritance

    @abstractmethod
    def work():
        pass   #abstraction

class Refrigirator(Appliances):
    def work(self): #polymorphism
        print("Refrigirator is Working!!")

class WashingMachine(Appliances):
    def work(self):  #polymorphism
        print("Washing Machine is working")

app1=Refrigirator()
app2=WashingMachine()
app1.turnOn()
app2.turnOn()
app1.work()
app2.work()