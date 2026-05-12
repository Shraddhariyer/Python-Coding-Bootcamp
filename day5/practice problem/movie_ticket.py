#create a  record system for movie tickets
movie=input("Enter movie name:")
seat=int(input("Enter seat name:"))
price=float(input("Enter price name:"))

ticket=(movie,seat,price)
print("Movie:",movie)
print("Seat:",seat)
print("Price:",price)

choice=input("want to change seat(yes-no):")
if choice=="yes":
    print("Cannot Change the seat!!")
else:
    print("Seat remained unchanged")
