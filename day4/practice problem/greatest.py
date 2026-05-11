#to find the greatest of three numbers
def greatest(a,b,c):
    if a>b and a>c:
        print(a," is the greatest number.")
    elif b>a and b>c:
        print(b," is the greatest number.")
    else:
        print(c," is the greatest number.")

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))
greatest(num1,num2,num3)