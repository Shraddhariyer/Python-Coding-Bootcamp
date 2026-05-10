#reverse the number
#1234 -> 4321
#base-10 = 1234%10=4
#1234 (4,-> reverse)
#4,3= 4+3=7
#4*10=40(40+3=43)
#n=n//10
#while(n>0)


n=int(input("enter the no.:"))
reverse=0
 
while n>0:
    digit_place=n%10
    reverse=reverse*10+digit_place
    n=n//10
print(reverse)