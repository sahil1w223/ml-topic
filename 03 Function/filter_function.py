# Basic Syntax: filter(function, iterable)
# The filter function takes a function and an iterable as arguments and returns an iterator that produces only the elements of the iterable for which the function returns True.
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers)) # This will print [2, 4, 6, 8, 10], as the filter function applies the is_even function to each element in the numbers list and returns an iterator that produces only the even values.