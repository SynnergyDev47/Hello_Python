### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set)) # Output: <class 'set'>
print(type(my_other_set)) # Output: <class 'dict'>

my_other_set = {"Aurelio", "Crespo", 28}
print(type(my_other_set)) # Output: <class 'set'>
print(len(my_other_set)) # Output: 3

my_other_set.add("Synnergy Dev")
print(my_other_set) # Output: {'Aurelio', 'Crespo', 28, 'Synnergy Dev'}

my_other_set.add("Synnergy Dev")
print(my_other_set) # Output: {'Aurelio', 'Crespo', 28, 'Synnergy Dev'}
# Sets do not allow duplicate values, so adding "Synnergy Dev" again does not change the set.

print("Aurelio" in my_other_set) # Output: True
print("Python" in my_other_set) # Output: False

my_other_set.remove("Crespo")
print(my_other_set) # Output: {'Aurelio', 28, 'Synnergy Dev'}

my_other_set.clear()
print(my_other_set) # Output: set()
print(len(my_other_set)) # Output: 0

del my_other_set
# print(my_other_set) # This will raise a NameError since my_other_set has been deleted.

my_set = {1, 2, 3, 4, 5}
print(my_set) # Output: {1, 2, 3, 4, 5}
my_list = list(my_set)
print(my_list) # Output: [1, 2, 3, 4, 5]
print(type(my_list)) # Output: <class 'list'>

my_other_set = {"Python", "Javascript", "Java", "C++"}
print(my_other_set) # Output: {'Python', 'Javascript', 'Java', 'C++'}

my_other_set.add(1)
my_other_set.add(2)
my_other_set.add(3)
my_other_set.add(4)
my_other_set.add(5)

print(my_other_set) # Output: {1, 2, 3, 4, 5, 'Python', 'Javascript', 'Java', 'C++'}

my_new_set = my_set.union(my_other_set)
print(my_new_set) # Output: {1, 2, 3, 4, 5, 'Python', 'Javascript', 'Java', 'C++'}
# The union of two sets combines all unique elements from both sets.

print(my_set.union(my_other_set).union({"C#", "Java"})) 
# Output: {1, 2, 3, 4, 5, 'Python', 'Javascript', 'Java', 'C++', 'C#'}
# We can chain the union method to combine multiple sets together.

print(my_new_set.difference(my_set))
# Output: {'Python', 'Javascript', 'Java', 'C++'}