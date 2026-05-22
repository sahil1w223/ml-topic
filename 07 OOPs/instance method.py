# instance method are the method which are defined inside the class and they are called by using the instance of the class.
# they are used to access the instance variable and class variable.
# they are defined by using the def keyword and they take self as the first parameter.
# To create an instance method we used decorator @classmethod.

class student:
    collage_name = "ABC collage"  # This is a class variable which is shared by all the instances of the class.
    branch = ['science', 'arts', 'maths']
    def __init__(self,name,roll):
        self.n = name
        self.r = roll

    def print_some(self, name, rollno):
        print(f"Name of student  is: {self.n}")    
        print(f"Roll Number of student  is {self.r}")
    @classmethod
    def print_collage_name(cls):
        print(f"Collage name is: {cls.collage_name}")


student1 = student('sahil',101)
student1.print_some("sahil", 68)
print("="*32)
student1.print_collage_name()

student2 = student('mukesh',102)
student2.print_some("mukesh", 69)
student2.print_collage_name()
