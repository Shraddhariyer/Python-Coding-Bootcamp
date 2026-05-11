#to calculate and display student results
def calculate_total(s1,s2,s3,s4):
    return s1+s2+s3+s4
def calculate_percent(total):
    return (total*100)/400
def calculate_grade(percent):
    if percent>=90:
        return("A+ Grade")
    elif percent>=80:
        return("A Grade")
    elif percent>=70:
        return("B Grade")
    elif percent>=60:
        return("C Grade")
    else:
        return("Failed")
def display_result(name,s1,s2,s3,s4,total,percent,grade):
    print("\nWELCOME TO STUDENT REPORT SYSTEM")
    print("Result of ",name)
    print("Marks of subject 1:",s1)
    print("Marks of subject 2:",s2)
    print("Marks of subject 3:",s3)
    print("Marks of subject 4:",s4)
    print("Total Marks:",total)
    print("Percentage:",percent,"%")
    print("Grade earned:",grade)

name=input("Enter Your Name:") 
sub1=int(input("Enter marks of subject 1:"))
sub2=int(input("Enter marks of subject 2:"))
sub3=int(input("Enter marks of subject 3:"))
sub4=int(input("Enter marks of subject 4:"))
total_marks=calculate_total(sub1,sub2,sub3,sub4)
total_percentage=calculate_percent(total_marks)
grade_earned=calculate_grade(total_percentage)
display_result(name,sub1,sub2,sub3,sub4,total_marks,total_percentage,grade_earned)