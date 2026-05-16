#To make a bank account class and create an object of that class

class BankAccount:
    def __init__(self,name,ac_no,balance):
        self.name=name
        self.ac_no=ac_no
        self.balance=balance

    def check_balance(self):
        print("Current Balance:",self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Money Deposited Successfully. Current Balance is:",self.balance)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Money Withdrawn Successfully. Current Balance:",self.balance)
        else:
            print("Insufficient Balance")

name=input("Enter name:")
ac_no=input("Enter account No:")
balance=int(input("Enter Balance:"))
ac1=BankAccount(name,ac_no,balance)
d=int(input("Enter amount to deposit"))
ac1.deposit(d)
w=int(input("Enter amount to withdraw"))
ac1.withdraw(w)
ac1.check_balance()