set_element = {1, 2, 3, 4, 5}
empty_set = set()  # creating an empty set

print(empty_set)  # printing the empty set
print(set_element)  # a set is a built-in data structure in python which is used to store multiple items in a single variable. It is unordered, mutable and does not allow duplicate elements.
print(type(set_element))  # set is a built-in data structure in python which is used to store multiple items in a single variable. It is unordered, mutable and does not allow duplicate elements.
print(len(set_element))  # length of the set

# operations on set
set_element.add(6)  # adding an element to the set
print(set_element)
set_element.remove(3)  # removing a specific element from the set
print(set_element)
set_element.discard(10)  # discarding an element from the set (if it exists)
print(set_element)
set_element.pop()  # removing and returning an arbitrary element from the set
print(set_element)
set_element.clear()  # removing all elements from the set
print(set_element)
set_element.update({7, 8, 9})  # updating the set with another set
print(set_element)
set_element.union({10, 11, 12})  # returning the union of two sets
print(set_element.union({10, 11, 12}))
set_element.intersection({7, 8, 9, 10})  # returning the intersection of two sets
print(set_element.intersection({7, 8, 9, 10}))
set_element.difference({7, 8, 9, 10})  # returning the difference of two sets
print(set_element.difference({7, 8, 9, 10}))
set_element.symmetric_difference({7, 8, 9, 10})  # returning the symmetric difference of two sets
print(set_element.symmetric_difference({7, 8, 9, 10}))
set_element.issubset({7, 8, 9})  # checking if the set is a subset of another set
print(set_element.issubset({7, 8, 9}))
set_element.issuperset({7, 8})  # checking if the set is a superset of another set
print(set_element.issuperset({7, 8}))  
set_element.isdisjoint({10, 11, 12})  # checking if the set is disjoint with another set
print(set_element.isdisjoint({10, 11, 12}))
set_element.copy()  # creating a copy of the set
print(set_element.copy())
set_element.pop()  # removing and returning an arbitrary element from the set
print(set_element)
set_element.clear()  # removing all elements from the set
print(set_element)
set_element.update({1, 2, 3, 4, 5})  # updating the set with another set
print(set_element)
