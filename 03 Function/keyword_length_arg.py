# Keyword-length arguments, also known as keyword arguments, allow you to pass a variable number of named arguments to a function. These arguments are passed as a dictionary, where the keys are the argument names and the values are the corresponding argument values.
def print_items(**args):
    for key,value in args.items():
        print(f"{key}: {value}")

print_items(name="Alice", age=30, city="New York")
print_items(product="Laptop", price=999.99, stock=50)