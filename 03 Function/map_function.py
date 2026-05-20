# Basic Syntex: map(function, iterable, ...)

def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers)) # This will print [1, 4, 9, 16, 25], as the map function applies the square function to each element in the numbers list and returns an iterator that produces the squared values.