#to make a grocery list manager

#add items to grocery list
def add_item(a,c):
    for i in a:
        c.append(i) #c=c+a[i] - wrong
    print("Your cart after adding items:",c)

#remove items from grocery list
def remove_item(r,c):
    for i in r:
        if i in c:
            c.remove(i)
            break
        else:
            print("Its not in your cart..")
    print("Cart after removing item:",c)


#display items in the grocery list
def display_item(c):
    if len(c)==0:
        print("Your cart is empty..")
    else:
        print("Your cart",c)

cart=["apple", "banana"]
print("WELCOME TO GROCERY MANAGER ")
print("1. Add items")
print("2. Remove items")
print("3. Display items")
choice=int(input("Enter your choice[1-3]:"))
if choice<1 and choice>3:
    print("Invalid choice..")
elif choice==1:
    add=input("Enter items separated by space:").split()
    add_item(add,cart)
elif choice==2:
    remove=input("Enter items separated by space:").split()
    remove_item(remove,cart)
else:
    display_item(cart)