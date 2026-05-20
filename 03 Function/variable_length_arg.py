# Variable-length arguments allow a function to accept an arbitrary number of arguments.
def print_val(*args):
    for arg in args:
        print(arg)

print_val(1, 2, 3)
print_val('a', 'b', 'c', 'd')