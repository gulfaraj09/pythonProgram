class Employee:
    no_of_leaves = 8
    var =8

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


class player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printDetails(self):
        return f"The Name is {self.name}.Game is {self.game}"


class coolProgrammer(Employee, player):
    language = "c++"
    var = 10
    def printLanguage(self):
        print(self.language)


gulfaraj = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 546, "Student")

subham = player("Subham", ["Cricket"])
karan = coolProgrammer("karan", 899, "CoolProgrammer")
# det = karan.printdetails()
# karan.printLanguage()
# print(det)
print(karan.var)
