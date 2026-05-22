class MyClass:
    def __init__(self,name,roll):
        self.n = name
        self.r = roll

    def print_some(self, name, rollno):
        print(f"Name of student is: {self.n}")    
        print(f"Roll Number of student is {self.r}")


obj1 = MyClass()
obj2 = MyClass()

obj1.print_some("sahil", 68)
print("="*32)
obj2.print_some("mukesh", 69)