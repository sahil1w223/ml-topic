# “Iterator is an object in Python that allows us to traverse elements one by one using the next() function.”

lis = [1, 2, 3, 4, 5]
# To create an iterator from a list, you can use the iter() function:
my_iterator = iter(lis)
# Now, you can use the next() function to get the next item from the iterator:

try:
    print(next(my_iterator))  # Output: 1
    print(next(my_iterator))  # Output: 2
    print(next(my_iterator))  # Output: 3
    print(next(my_iterator))  # Output: 4
    print(next(my_iterator))  # Output: 5
    print(next(my_iterator))  # This will raise StopIteration as there are no more items

except StopIteration:
    print("No more items to iterate.")


name = "Python"
name_iterator = iter(name)
try:
    while True:
        print(next(name_iterator))  # Output: P, y, t, h, o, n
except StopIteration:
    print("No more characters to iterate.")

