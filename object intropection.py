class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gulfaraj.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set.\nPlease set it using setter"
        return f"{self.fname}.{self.lname}@gulfaraj.com"

    @email.setter
    def email(self, string):
        print("Setting Now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("skill", "f")
# print(skillf.email)

# print(id("this is a string"))
# print(id("that that"))

# o = "This is a string"
# print(dir(skillf))

import inspect

print(inspect.getmembers(skillf))
