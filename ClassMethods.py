class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary} and role is {rohan.role}"
    @classmethod
    def change_leaves(cls,Newleaves):
        cls.no_of_leaves = Newleaves

gulfaraj = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",546,"Student")
gulfaraj.change_leaves(34)
# print(gulfaraj.salary)
print(gulfaraj.no_of_leaves)