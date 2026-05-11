#function define
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
addition= add(num1,num2)
substraction=substract(num1,num2)
multiplication=multiply(num1,num2)
division=divide(num1,num2)
print(addition,substraction,multiplication,division)
