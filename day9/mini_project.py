#ticket booking system
from abc import ABC,abstractmethod
class Ticket(ABC):
    def __init__(self,movie_name,quantity):
        self.movie_name=movie_name
        self._price=200    #encapsulation
        self.quantity=quantity

    def showDetails(self):
        print("Movie name:",movie_name)
        print("Number of tickets:",quantity)

    @abstractmethod
    def calculate_price():
        pass

class RegularTicket(Ticket):
    def calculate_price(self):
        self._price=self._price*quantity
        print("Total Price:",self._price)

class VIPTicket(Ticket):
    def calculate_price(self):
        self._price=self._price*quantity+200
        print("Total Price:",self._price)


movie_name=input("Enter Movie Name:")
quantity=int(input("Enter number of tickets required:") )
type=input("Enter type of your Ticket[regular/vip]:")
if type.lower()=="regular":
    ticket=RegularTicket(movie_name,quantity)

elif type.lower()=="vip":
    ticket=VIPTicket(movie_name,quantity)

else:
    print("Invalid choice..")
    exit()

ticket.showDetails()
ticket.calculate_price()