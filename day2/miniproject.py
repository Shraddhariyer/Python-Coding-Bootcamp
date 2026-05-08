#create a atm menu system
#check balance, withdraw, deposit, exit
balance=5000
print("ATM MENU SYSTEM")
print("Select any 1 option")
print("1.Check Balance")
print("2.Withdraw")
print("3.Deposit")
print("4.Exit")
choice=int(input("Enter your choice(1-4):"))
if choice==1:
    print(balance,"Rs")
elif choice==2:
    amount=int(input("Enter the amount to withdraw:"))
    if amount>balance:
        print("Insufficient Balance")
    else:
        balance=balance-amount
        print(amount,"Debited, available balance is:", balance)
elif choice==3:
    amount=int(input("Enter the amount to withdraw:"))
    if amount<0:
        print("Invalid amount!!")
    else:
        balance=balance+amount
        print(amount,"Rs Credited, available balance is:", balance)
elif choice==4:
    print("Thank you for banking with us!!")
else:
    print("Invalid option")