#to store student marks using dictionary and access marks using key
marks={
    "Rahul":90,
    "Pooja":80,
    "rohan":85,
    "Preeti":95,
}
student=input("Enter the name of student:")
if student in marks:
        print("Marks :",marks[student])
else:
        print("Student marks is missing..")

    