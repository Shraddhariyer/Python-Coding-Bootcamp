#to split the bill amongst the people
def bill(totalBill,peoples):
    perPerson=totalBill/peoples
    return perPerson

total_bill=int(input("Enter the total amount:"))
total_people=int(input("Enter the number of people:"))
amount_per_person=bill(total_bill,total_people)
print("Amount per person is:",amount_per_person)