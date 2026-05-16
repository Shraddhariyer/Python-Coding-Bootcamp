#to generate tax of employee

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calculate_tax(self):
        tax=self.salary*0.10
        print("Employee name:",self.name)
        print("Salary:",self.salary)
        print("Tax:",tax)

rahul=Employee("Rahul",15000)
rahul.calculate_tax()