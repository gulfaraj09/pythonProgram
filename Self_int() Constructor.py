class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary} and role is {rohan.role}"

gulfaraj = Employee("Harry",455,"Instructor")
# rohan = Employee()

# gulfaraj.name = "Gulfaraj"
# gulfaraj.salary = 455
# gulfaraj.role = "Instructor"
#
# rohan.name = "rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(rohan.printdetails())
print(gulfaraj.salary)