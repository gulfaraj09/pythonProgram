class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary} and role is {rohan.role}"

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

class Programmer(Employee):
    no_of_hoidays = 56
    def __init__(self, aname, asalary, arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printProg(self):
        return f"The programmer's name is {self.name}.Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

gulfaraj = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 546, "Student")

subham = Programmer("Subham",555,"Programmer",["python"])
karan = Programmer("Karan",777,"Programmer",["python","C++"])

# print(karan.printProg())
print(karan.no_of_hoidays)