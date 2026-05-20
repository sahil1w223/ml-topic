lis = [n for n in range(1, 11)]

# accessing the list
print(lis)
print(type(lis)) #list is a built in data structure in python which is used to store multiple items in a single variable. It is ordered, mutable and allows duplicate elements. 
print(lis[0]) #accessing first element
print(lis[1:5]) #slicing the list from index 1 to 4
print(len(lis)) #length of the list

#modifying the list
lis[2] = 100
print(lis)

#operations on list
lis.append(11) #adding an element to the end of the list
print(lis)
lis.insert(0, 0) #inserting an element at a specific index
print(lis)
lis.pop() #removing the last element of the list
print(lis)
lis.remove(100) #removing a specific element from the list
print(lis)
lis.sort() #sorting the list
print(lis)
print(lis.count(100)) #counting the occurrences of a specific element in the list
print(lis.index(4)) #finding the index of a specific element in the list
lis.reverse() #reversing the list
print(lis)
lis.extend([12, 13, 14]) #extending the list with another list
print(lis)

#list slicing
print(lis[2:5]) #slicing the list from index 2 to 4
print(lis[:5]) #slicing the list from the beginning to index 4
print(lis[5:]) #slicing the list from index 5 to the end
print(lis[-5:]) #slicing the list from the end to index -5
print(lis[::2]) #slicing the list with a step of 2

# iterating through the list and indexing
for index, value in enumerate(lis):
    print(f"Index: {index}, Value: {value}")

# nested list
lis1 = [n for n in range(1, 6)]
lis2 = ['a', 'b', 'c', 'd', 'e']
lis3 = [[a,b] for a in lis1 for b in lis2]
print(lis3)