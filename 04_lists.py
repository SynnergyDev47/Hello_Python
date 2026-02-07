# Lists in Python

my_list = list()  # Creating an empty list
my_other_list = []  # Creating another empty list

print(len(my_list))  # Output: 0
print(len(my_other_list))  # Output: 0

my_list = [1, 2, 3, 4, 5]
my_other_list = ["a", "b", "c", True, 23, 45.67] 

print(len(my_list))  # Output: 5
print(len(my_other_list))  # Output: 6

print(my_list)  # Output: [1, 2, 3, 4, 5]
print(my_other_list)  # Output: ['a', 'b', 'c', True, 23, 45.67]
print(type(my_list))  # Output: <class 'list'>

# Accessing elements
print(my_list[0])  # Output: 1
print(my_other_list[3])  # Output: True
print(my_list[-1])  # Output: 5
print(my_list[-9]) # Output: IndexError 

# Unpacking lists
user_data = ["Alice", 28, "Engineer", False]
name, age, profession, is_student = user_data

print(name)  # Output: Alice
print(age)  # Output: 28
print(profession)  # Output: Engineer
print(is_student)  # Output: False

# List Methods
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]                            
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5, 6]
my_list.insert(2, 3)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
popped_element = my_list.pop()
print(popped_element)  # Output: 6
print(my_list)  # Output: [1, 2, 3, 4, 5]
my_list.reverse()   
print(my_list)  # Output: [5, 4, 3, 2, 1]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5]
my_list.extend([6, 7, 8])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(4 in my_list)  # Output: True
print(10 not in my_list)  # Output: True    
print(my_list.index(5))  # Output: 4
print(my_list.count(3))  # Output: 1
my_pop_element = my_list.pop(1)
print(my_pop_element)  # Output: 2
del my_list[2]
print(my_list)  # Output: [1, 3, 5, 6, 7, 8]
my_list.clear()
print(my_list)  # Output: []

### Methods Summary ###
# append(item) - Adds an item to the end of the list
# remove(item) - Removes the first occurrence of an item
# del list[index] - Removes an item at a specific index
# insert(index, item) - Inserts an item at a specific index
# pop([index]) - Removes and returns an item at a specific index (default is last)
# reverse() - Reverses the list in place
# sort() - Sorts the list in place
# extend(iterable) - Adds elements from another iterable to the end of the list
# clear() - Removes all elements from the list
# index(item) - Returns the index of the first occurrence of an item
# count(item) - Returns the number of occurrences of an item

### Other List Operations ###
# slicing - accessing a range of elements
# copying - creating a copy of a list
# concatenation - combining two lists
# membership testing - checking if an item is in a list

### Examples of other methods ###

# Slicing
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4]
print(my_list[:3])  # Output: [1, 2, 3]
print(my_list[3:])  # Output: [4, 5]

# Copying
my_list_copy = my_list.copy()
print(my_list_copy)  # Output: [1, 2, 3, 4, 5]

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Membership Testing
print(3 in my_list)  # Output: True 
print(10 in my_list)  # Output: False

### Advanced Methods ###

# List Comprehensions
squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]