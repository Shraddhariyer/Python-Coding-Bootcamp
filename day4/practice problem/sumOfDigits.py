#to add the digits in the number
def sum_of_digits(n):
    sum=0
    for i in n:
        num=int(i)
        sum+=num  #sum=sum+num
    print(sum)

number=input("Enter a Number:")
sum_of_digits(number)