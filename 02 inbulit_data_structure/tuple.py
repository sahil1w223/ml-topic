tup = tuple([i for i in range(5)])

print(tup)  # a tuple is a built-in data structure in python which is used to store multiple items in a single variable. It is ordered, immutable and allows duplicate elements.
print(type(tup))  # tuple is a built-in data structure in python which is used to store multiple items in a single variable. It is ordered, immutable and allows duplicate elements.
print(tup[0])  # accessing first element
print(tup[1:4])  # slicing the tuple from index 1 to
print(len(tup))  # length of the tuple

print(tup.index(3))  # finding the index of a specific element in the tuple
print(tup.count(3))  # counting the occurrences of a specific element in the tuple

print(max(tup))  # finding the maximum element in the tuple
print(min(tup))  # finding the minimum element in the tuple
print(sum(tup))  # finding the sum of all elements in the tuple
print(sorted(tup))  # sorting the tuple

# nested tuple
tup1 = ((1,2,3), (4,5,6), (7,8,9))
print(tup1[1][1:3])  # accessing the first element of the second tuple in the nested tuple

for sub_ele in tup1:
    for element in sub_ele:
        print(element)  # iterating through the nested tuple and printing each element