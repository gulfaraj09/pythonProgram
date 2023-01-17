class Employee:
    no_of_leaves = 8

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

    def __add__(self,other):
        return self.salary+other.salary

    def __truediv__(self,other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee ('{self.name}', {self.salary}, '{self.role})'"

    def __str__(self):
        return f"Name is {self.name}.Salary is {self.salary} and role is {self.role}"

emp1 = Employee("Gulfaraj",877,"Programmer")
# emp2 = Employee("Rohan",87,"Cleaner")
# print(emp1/emp2)
print(str(emp1))

# Mapping Operators to functions