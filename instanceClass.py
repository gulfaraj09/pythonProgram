class Employee:
    no_of_leaves = 8
    pass

gulfaraj = Employee()
rohan = Employee()

gulfaraj.name = "Gulfaraj"
gulfaraj.salary = 455
gulfaraj.role = "Instructor"
rohan.name = "Gulfaraj"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(rohan.__dict__)
print(Employee.no_of_leaves )