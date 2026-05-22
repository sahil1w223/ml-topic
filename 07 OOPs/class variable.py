'''
class vaiable are the variable which are shared by all the instances of the class.
They are also called as class variable.
They are defined inside the class but outside any method.
They are accessed by using the class name or by using the instance name.
'''

class student:
    collage_name = "ABC collage"  # This is a class variable which is shared by all the instances of the class.
    branch = ['science', 'arts', 'maths']
    def __init__(self,name,roll):
        self.n = name
        self.r = roll

    def print_some(self, name, rollno):
        print(f"Name of student is: {self.n}")    
        print(f"Roll Number of student is {self.r}")

student1 = student('sahil',101)

