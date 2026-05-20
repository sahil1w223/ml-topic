dic = {'name':'sahil', 'age': 24, 'city': 'pune'}

print(dic['name'])  # Output: sahil
print(dic['age'])   # Output: 24
print(dic['city'])  # Output: pune
print(type(dic))  # Output: <class 'dict'>, a dictionary is a built-in data structure in python which is used to store multiple items in a single variable. It is unordered, mutable and does not allow duplicate elements.

# modifying the dictionary
dic['age'] = 25
print(dic)  # Output: {'name': 'sahil', 'age': 25, 'city': 'pune'}  
dic['country'] = 'India'  # adding a new key-value pair to the dictionary
print(dic)  # Output: {'name': 'sahil', 'age': 25, 'city': 'pune', 'country': 'India'}
del dic['city']  # removing a key-value pair from the dictionary
print(dic)  # Output: {'name': 'sahil', 'age': 25, 'country': 'India'}

# operations on dictionary
print(dic.keys())  # Output: dict_keys(['name', 'age', 'country']), returns a view object that displays a list of all the keys in the dictionary
print(dic.values())  # Output: dict_values(['sahil', 25, 'India']), returns a view object that displays a list of all the values in the dictionary
print(dic.items())  # Output: dict_items([('name', 'sahil'), ('age', 25), ('country', 'India')]), returns a view object that displays a list of dictionary's key-value tuple pairs
print(dic.get('name'))  # Output: sahil, returns the value for the specified key if the key is in the dictionary, else returns None
print(dic.get('city', 'Not Found'))  # Output: Not Found, returns the

# not a good way to copy a dictionary as it creates a reference to the original dictionary, so modifying the copy will affect the original dictionary
id_copy = dic
id_copy['age'] = 30
print(dic)  # Output: {'name': 'sahil', 'age': 30, 'country': 'India'}
print(id_copy)  # Output: {'name': 'sahil', 'age': 30, 'country': 'India'}, both dic and id_copy point to the same dictionary in memory, so modifying one will affect the other

# a good way to copy a dictionary is to use the copy() method, which creates a shallow copy of the dictionary, so modifying the copy will not affect the original dictionary
copy_dic = dic.copy()
copy_dic['age'] = 35
print(dic)  # Output: {'name': 'sahil', 'age': 30, 'country': 'India'}
print(copy_dic)  # Output: {'name': 'sahil', 'age': 35, 'country': 'India'}, copy_dic is a separate dictionary in memory, so modifying it will not affect dic

# Nested dictionary
nested_dic = {
    'person1': {'name': 'sahil', 'age': 24},
    'person2': {'name': 'john', 'age': 30}
}

print(nested_dic['person1']['name'])  # Output: sahil, accessing the name of person1 in the nested dictionary
print(nested_dic['person2']['age'])  # Output: 30, accessing the age of person2 in the nested dictionary
print(nested_dic) # Output: {'person1': {'name': 'sahil', 'age': 24}, 'person2': {'name': 'john', 'age': 30}}, a nested dictionary is a dictionary that contains another dictionary as a value, it allows us to store complex data structures in a single variable.
