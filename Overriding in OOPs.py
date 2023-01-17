class A:
    classVar1 = "I am a class variabele in class A"
    def __init__(self):
        self.var1 = "I am inside class A's Constuctor"
        self.classVar1 = "Instance var in class A"
        self.special = "Special"
class B(A):
    classVar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am inside class B's Constuctor"
        self.classVar1 = "Instance var in class B"
        super().__init__()
        print(super().classVar1)

a = A()
b = B()

print(b.special,b.var1,b.classVar1) 