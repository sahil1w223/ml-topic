# creating a class

class MyClass:
    def print_some(self, name, rollno):
        print(f"Name of student is: {name}")    
        print(f"Roll Number of student is {rollno}")

# creating a object 
obj1 = MyClass()
obj2 = MyClass()

obj1.print_some("sahil", 68)
print("="*32)
obj2.print_some("mukesh", 69)
