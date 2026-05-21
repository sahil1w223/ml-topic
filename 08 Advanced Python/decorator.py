# Decorator is a function that takes another function as input and adds extra functionality without modifying the original function.

# function copy
def copy():
    return "wellcome to my page."

copy_func = copy()
del copy
print(copy_func)  # Output: "wellcome to my page."

# closure

def outer_func():
    message = "Hello, World!"
    
    def inner_func():
        print("This is the inner function.")
        print(message)
        print("This is the end of the inner function.")
    
    return inner_func()

outer_func()


def OuterFunc(func,args):
    
    def InnerFunc():
        print("This is the inner function.")
        print("length of the list is:", func(args))
        print("This is the end of the inner function.")
    
    return InnerFunc()

OuterFunc(len,[1,2,3,4,5]) 

# decorator
def main(func):
    def weapper():
        print("This is the main function.")
        func()
        print("This is the end of the main function.")
    return weapper()


@main
def my_func():
    print("This is my function.")
    
    


