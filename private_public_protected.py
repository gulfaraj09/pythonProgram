# Public - Access publically
# Protected - only class and inherited class access
# Private - only class access no on access it

class Employee:
    no_of_leaves = 8
    var =8
    _protect = 3
    __private = 38

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, Newleaves):
        cls.no_of_leaves = Newleaves

    @classmethod
    def from_dash(cls, string):
        # param = string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print(f"This is a {string}")

emp = Employee("Gulfaraj",543,"Programmer")
print(emp._protect)
print(emp._Employee__private) # (._Employee__private) is called name mangling