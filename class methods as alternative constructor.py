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

    @classmethod
    def from_dash(cls,string):
        # param = string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return  cls(*string.split("-"))

gulfaraj = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",546,"Student")
karan = Employee.from_dash("Karan-480-Student")


# gulfaraj.change_leaves(34)
print(karan.salary)
# print(rohan.no_of_leaves)
# print(gulfaraj.no_of_leaves)