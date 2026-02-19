### Dictionaries ###

"""
Docstring for 07_dictionaries
1. Dictionaries are unordered collections of key-value pairs.
2. Dictionaries are mutable, meaning their contents can be changed after creation.
3. Keys in a dictionary must be unique and immutable (e.g., strings, numbers, tuples).
4. Values in a dictionary can be of any data type and can be duplicated.
5. Dictionaries are defined using curly braces {} with key-value pairs separated by colons (:).
6. You can access, add, modify, and delete key-value pairs in a dictionary using keys.
7. Dictionaries have built-in methods for common operations, such as keys(), values(), items(), get(), and update().
8. Dictionaries are commonly used for storing and retrieving data based on unique identifiers (keys).
9. The order of key-value pairs in a dictionary is not guaranteed (prior to Python 3.7), but from Python 3.7 onwards, dictionaries maintain the insertion order.
"""

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # Output: <class 'dict'>
print(type(my_other_dict)) # Output: <class 'dict'>

my_dict = {"name": "Aurelio", "surname": "Crespo", "age": 28, 1: "Python"}
print(type(my_dict)) # Output: <class 'dict'>
print(len(my_dict)) # Output: 4
print(my_dict) # Output: {'name': 'Aurelio', 'surname': 'Crespo', 'age': 28, 1: 'Python'}

my_other_dict = {
    "name": "Aurelio",
    "surname": "Crespo",
    "age": 28,
    "language": {"Python", "JavaScript", "Go"}
}

print(my_dict)
print(my_other_dict)

print(my_dict["name"]) # Output: Aurelio
print(my_other_dict["language"]) # Output: {'Python', 'JavaScript', 'Go'}

#Changing values in a dictionary
my_dict["name"] = "Synnergy"
my_dict["surname"] = "Dev"
my_dict["country"] = "Cuba" #Adding a new key-value pair to the dictionary
print(my_dict) # Output: {'name': 'Synnergy', 'surname': 'Dev', 'age': 28, 1: 'Python', 'country': 'Cuba'}

#Deleting key-value pairs from a dictionary
del my_dict["age"] #Deleting a key-value pair from the dictionary
print(my_dict) # Output: {'name': 'Synnergy', 'surname': 'Dev', 1: 'Python', 'country': 'Cuba'}

del my_dict[1] #Deleting a key-value pair from the dictionary
print(my_dict) # Output: {'name': 'Synnergy', 'surname': 'Dev', 'country': 'Cuba'}

del my_dict #Deleting the entire dictionary
# print(my_dict) # This will raise a NameError since my_dict has been deleted

print("Synnergy" in my_other_dict) # Output: False, because "Synnergy" is a value in the dictionary, not a key
print("name" in my_other_dict) # Output: True, because "name" is a key in the dictionary
print(my_other_dict.items()) # Output: dict_items([('name', 'Aurelio'), ('surname', 'Crespo'), ('age', 28), ('language', {'Python', 'JavaScript', 'Go'})])
print(my_other_dict.keys()) # Output: dict_keys(['name', 'surname', 'age', 'language'])
print(my_other_dict.values()) # Output: dict_values(['Aurelio', 'Crespo', 28, {'Python', 'JavaScript', 'Go'}])

#Creating a dictionary using fromkeys() method
my_dict_from_keys = dict.fromkeys(my_other_dict)
print(my_dict_from_keys) # Output: {'name': None, 'surname': None, 'age': None, 'language': None}

#Adding a default value to the dictionary created with fromkeys()
my_dict_from_keys_with_value = dict.fromkeys(my_other_dict, "default_value")
print(my_dict_from_keys_with_value) # Output: {'name': 'default_value', 'surname': 'default_value', 'age': 'default_value', 'language': 'default_value'}

# Creating a dictionary from a list of keys using dict.fromkeys()
my_list = ["name", "surname", "age", "language"]
my_dict_from_list = dict.fromkeys(my_list)
print(my_dict_from_list) # Output: {'name': None, 'surname': None, 'age': None, 'language': None}

# Converting dictionary views to other data types
print(tuple(my_other_dict.values())) # Output: ('Aurelio', 'Crespo', 28, {'Python', 'JavaScript', 'Go'})
print(set(my_other_dict.keys())) # Output: {'name', 'surname', 'age', 'language'}
print(list(my_other_dict.items())) # Output: [('name', 'Aurelio'), ('surname', 'Crespo'), ('age', 28), ('language', {'Python', 'JavaScript', 'Go'})]