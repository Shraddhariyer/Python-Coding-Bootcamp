def is_positive(number):
    return number > 0

if __name__=="__main__":
    num=int(input("Enter a number:"))
    if is_positive(num):
        print("The number is positive!")
    else:
        print("The number is Negative or Zero!")