class Employee:
    def __init__(self,fname,lname):
        self.fname =fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gulfaraj.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname ==None or self.lname == None:
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

hindustanin_supporter = Employee("Hindustani","Supporter")
# nikhil_raj_panday =Employee("Nikhil","Raj")

print(hindustanin_supporter.explain())
print(hindustanin_supporter.print_Email)

hindustanin_supporter.fname ="US"
print(hindustanin_supporter.print_Email)
hindustanin_supporter.print_Email = "this.that@gulfaraj.com"
print(hindustanin_supporter.fname)

del hindustanin_supporter.print_Email
print(hindustanin_supporter.print_Email)