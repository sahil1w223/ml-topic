# “A generator is a special function in Python that generates values one at a time using the yield keyword.”
# Generators can't store all the values in memory at once, making them more memory-efficient than lists or other collections.
lis = [1, 2, 3, 4, 5]

def my_generator(lst):
    for item in lst:
        yield item

# To create a generator object, you can call the generator function:
gen = my_generator(lis)

# method 1: using a for loop to iterate through the generator
# for i in gen:
#     print(i)  # Output: 1, 2, 3, 4, 5



# `method 2: using the next() function to get the next item from the generator:`
try:
    print(next(gen))  # Output: 1
    print(next(gen))  # Output: 2
    print(next(gen))  # Output: 3
    print(next(gen))  # Output: 4
    print(next(gen))  # Output: 5
    print(next(gen))  # This will raise StopIteration as there are no more items
except StopIteration:
    print("No more items to generate.")

# you can create a multiple yield generator that generates multiple values at once. For example:
def multiple_yield_generator(lst):
    for item in lst:
        yield item, item ** 2

gen2 = multiple_yield_generator(lis)
try:
    print(next(gen2))  # Output: (1, 1)
    print(next(gen2))  # Output: (2, 4)
    print(next(gen2))  # Output: (3, 9)
    print(next(gen2))  # Output: (4, 16)
    print(next(gen2))  # Output: (5, 25)
    print(next(gen2))  # This will raise StopIteration as there are no more items
except StopIteration:
    print("No more items to generate.")


# you can also create a generator that have multiple yield statements. For example:
def multiple_yield_statements(lst):
    for item in lst:
        yield item
        yield item ** 2
    
gen3 = multiple_yield_statements(lis)
try:
    print(next(gen3))  # Output: 1
    print(next(gen3))  # Output: 1
    print(next(gen3))  # Output: 2
    print(next(gen3))  # Output: 4
    print(next(gen3))  # Output: 3
    print(next(gen3))  # Output: 9
    print(next(gen3))  # Output: 4
    print(next(gen3))  # Output: 16
    print(next(gen3))  # Output: 5
    print(next(gen3))  # Output: 25
    print(next(gen3))  # This will raise StopIteration as there are no more items
except StopIteration:
    print("No more items to generate.")


# opening a file and using a generator to read it line by line

def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


file_generator = read_file_line_by_line('08 Advanced Python/file.txt')
try:
    while True:
        print(next(file_generator))  # Output: lines from the file
except StopIteration:
    print("No more lines to read.")