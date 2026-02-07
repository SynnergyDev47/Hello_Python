### Tuples in Python ###

my_tuple = tuple()  # Creating an empty tuple
my_other_tuple = ()  # Creating another empty tuple

# Checking the types
print(type(my_tuple))         # Output: <class 'tuple'>

# Tuples with different data types
my_tuple = (35, 28.5, "Hello", True, 5+3j)
print(my_tuple)               # Output: (35, 28.5, 'Hello', True, 8j)

# Accessing elements in a tuple
print(my_tuple[0])            # Output: 35  
print(my_tuple[-1])           # Output: 8j
print(my_tuple[1:4])          # Output: (28.5, 'Hello', True)
print(my_tuple[::2])          # Output: (35, 'Hello', 8j)
print(my_tuple[::-1])         # Output: (8j, True, 'Hello', 28.5, 35)

# Tuples are immutable
# my_tuple[0] = 50            # This will raise a TypeError 
print(len(my_tuple))          # Output: 5
print(my_tuple.count(28.5))   # Output: 1
print(my_tuple.index("Hello")) # Output: 2  
print(35 in my_tuple)         # Output: True
print(100 in my_tuple)        # Output: False

# Concatenation and repetition
new_tuple = my_tuple + (100, 200, 300)
print(new_tuple)              # Output: (35, 28.5, 'Hello', True, 8j, 100, 200, 300)
repeated_tuple = my_tuple * 2
print(repeated_tuple)         # Output: (35, 28.5, 'Hello, True, 8j, 35, 28.5, 'Hello', True, 8j)

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a)                      # Output: 35  
print(b)                      # Output: 28.5
print(c)                      # Output: Hello
print(d)                      # Output: True
print(e)                      # Output: 8j

# Nested tuples
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple)           # Output: (1, 2, (3, 4), (5, 6))
print(nested_tuple[2])        # Output: (3, 4)
print(nested_tuple[2][1])     # Output: 4

# Single element tuple
single_element_tuple = (42,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
print(single_element_tuple)        # Output: (42,)
not_a_tuple = (42)
print(type(not_a_tuple))          # Output: <class 'int'>
print(not_a_tuple)                # Output: 42

# Tuple with mixed data types
mixed_tuple = (1, "two", 3.0, [4, 5], (6, 7))
print(mixed_tuple)               # Output: (1, 'two', 3.0, [4, 5], (6, 7))
print(mixed_tuple[3])            # Output: [4, 5]
print(mixed_tuple[4][1])         # Output: 7

# Iterating through a tuple
for item in my_tuple:
    print(item)
# Output:
# 35
# 28.5
# Hello
# True
# 8j

# Tuple comparison
tuple1 = (1, 2, 3) 
tuple2 = (1, 2, 4)
print(tuple1 < tuple2)          # Output: True
print(tuple1 == tuple2)         # Output: False
print(tuple1 > tuple2)          # Output: False
print(tuple1 <= (1, 2, 3))      # Output: True
print(tuple2 >= (1, 2, 3))      # Output: True
print(tuple1 != tuple2)         # Output: True

# Using tuples as dictionary keys
my_dict = {
    (1, 2): "Point A",
    (3, 4): "Point B"
}
print(my_dict[(1, 2)])          # Output: Point A
print(my_dict[(3, 4)])          # Output: Point B

# Nested tuple unpacking
nested = (1, (2, 3), 4)
a, (b, c), d = nested
print(a)                      # Output: 1
print(b)                      # Output: 2
print(c)                      # Output: 3
print(d)                      # Output: 4

# Converting a list to a tuple
my_list = [10, 20, 30]
converted_tuple = tuple(my_list)
print(converted_tuple)         # Output: (10, 20, 30)
print(type(converted_tuple))   # Output: <class 'tuple'>

# Converting a string to a tuple
my_string = "Hello"
string_tuple = tuple(my_string)
print(string_tuple)            # Output: ('H', 'e', 'l', 'l', 'o')
print(type(string_tuple))      # Output: <class 'tuple'>

# Converting a tuple to a list
tuple_to_list = list(my_tuple)
print(tuple_to_list)           # Output: [35, 28.5, 'Hello', True, 8j]
print(type(tuple_to_list))     # Output: <class 'list'>

# Using tuple in functions
def sum_and_product(x, y):
    return (x + y, x * y)
result = sum_and_product(3, 4)
print(result)                  # Output: (7, 12)

sum_result, product_result = result
print(sum_result)              # Output: 7
print(product_result)          # Output: 12

# Swapping values using tuple unpacking
x = 5
y = 10
x, y = y, x
print(x)                      # Output: 10
print(y)                      # Output: 5

# Immutable nature of tuples demonstration
original_tuple = (1, 2, 3)
modified_tuple = original_tuple + (4,)
print(original_tuple)         # Output: (1, 2, 3)
print(modified_tuple)         # Output: (1, 2, 3, 4)

# Using tuples in loops with enumerate
for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: 35

# Tuple comprehension using generator expression
squared_tuple = tuple(x**2 for x in range(5))
print(squared_tuple)           # Output: (0, 1, 4, 9, 16)

# Using tuples with zip
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
print(list(zipped))            # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Finding the maximum and minimum in a tuple
num_tuple = (10, 20, 5, 30, 15)
print(max(num_tuple))          # Output: 30
print(min(num_tuple))          # Output: 5
print(sum(num_tuple))          # Output: 80

# Slicing a tuple
"""Explanation of slicing:
 slice_tuple[start:stop:step]"""

slice_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(slice_tuple[2:7])        # Output: (2, 3, 4, 5, 6)
print(slice_tuple[:5])         # Output: (0, 1, 2, 3, 4)
print(slice_tuple[5:])         # Output: (5, 6, 7, 8, 9)
print(slice_tuple[::3])        # Output: (0, 3, 6, 9)
print(slice_tuple[::-1])       # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# Using tuples in function arguments
def print_coordinates(coords):
    for coord in coords:
        print(f"X: {coord[0]}, Y: {coord[1]}")
coordinates = [(1, 2), (3, 4), (5, 6)]
print_coordinates(coordinates)
# Output:
# X: 1, Y: 2
# X: 3, Y: 4
# X: 5, Y: 6

# Facts about tuples
"""
1. Tuples are ordered collections of items.
2. Tuples are immutable, meaning their elements cannot be changed after creation.
3. Tuples can contain elements of different data types. 
4. Tuples support indexing and slicing.
5. Tuples can be nested, meaning they can contain other tuples as elements.
6. Tuples can be used as keys in dictionaries due to their immutability.
7. Tuples support various built-in methods like count() and index().
8. Tuples can be unpacked into individual variables.
9. Tuples can be created using parentheses () or the tuple() constructor.
10. Tuples are generally faster than lists for certain operations due to their immutability.
"""