#comparision operators
#>,<,>=,<=,==,!=
#conditional statements
#if-elif-else
# student_marks=85
# if(student_marks>=90):
#     print("A grade")
# elif(student_marks>=80):
#     print("B Grade")
# elif(student_marks>=70):
#     print("C grade")
# else:
#     print("Failed")
#Logical operators
# and, or, not
# raining=False
# if not raining:
#     print("Lets play")
# else:
#     print("cannot play its raining outside")

#nested conditions
citizen=False
age=25
if citizen:
    print("Citizenship checked!!")
    if age>=18:
        print("Eligible to vote")
    else:
        print("Underage, Not eligible to vote")
else:
    print("Cannot vote without citizenship")
