# static methods are methods that belong to a class rather than an instance of the class.
# They can be called on the class itself, without needing to create an instance of the class.
# Static methods are defined using the @staticmethod decorator and do not take the self parameter.


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

    @staticmethod
    def print_branch():
        print(f"Branches available are: {student.branch}")

student1 = student('sahil',101)
student1.print_some("sahil", 68)    
print("="*32)
student1.print_collage_name()
student1.print_branch()
