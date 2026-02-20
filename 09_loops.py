### Loops ###

# While loops
my_condition = 0

while my_condition < 10: # This is the condition that will be checked before each iteration of the loop
    print(my_condition)
    my_condition += 1 # This is the code that will be executed in each iteration of the loop. In this case, we are incrementing my_condition by 1 in each iteration.
else:
    print("my_condition is no longer less than 10")
    
# Output: 0
#         1 
#         2
#         3
#         4
#         5
#         6
#         7
#         8
#         9
#         my_condition is no longer less than 10

print(f"my_condition is now: {my_condition}") # Output: my_condition is now: 10
print("Finished while loop") # Output: Finished while loop

while my_condition < 20:
    print(my_condition)
    my_condition += 2 # This is the code that will be executed in each iteration of the loop. In this case, we are incrementing my_condition by 2 in each iteration.
    if my_condition == 14: # This is a condition that will be checked in each iteration of the loop. If this condition is true, the loop will be terminated.    
        print("my_condition is now 14, breaking the loop")
        break # This will terminate the loop if my_condition is equal to 14.
    print(my_condition) # This will print the value of my_condition after it has been incremented by 2 in each iteration of the loop.
else:
    print("my_condition is no longer less than 20")

print(f"my_condition is now: {my_condition}") # Output: my_condition is now: 14
print("Finished while loop") # Output: Finished while loop

# For loops
my_list = [1, 2, 3, 4, 5]

for i in my_list: # This is the syntax for a for loop. We are iterating over each i in my_list and assigning it to the variable item in each iteration of the loop.
    print(i) # This will print the value of i in each iteration of the loop.
# Output: 1
#         2
#         3
#         4
#         5

my_tuple = ("Aurelio", "Crespo", "Python", "Developer", 28)
my_set = {"Aurelio", "Crespo", "Python", "Developer", 28}
my_dict = {"name": "Aurelio", "surname": "Crespo", "language": "Python", "job": "Developer", "age": 28}

for i in my_tuple:
    print(i) # Output: Aurelio
             #         Crespo   
             #         Python
             #         Developer
             #         28

for i in my_set:
    print(i) # Output: 28
             #         Developer
             #         Python
             #         Crespo
             #         Aurelio

for key, value in my_dict.items():
    print(f"{key}: {value}") # Output: name: Aurelio
                             #         surname: Crespo
                             #         language: Python
                             #         job: Developer
                             #         age: 28

# Continue statement
for i in range(10):
    if i % 2 == 0: # This is a condition that will be checked in each iteration of the loop. If this condition is true, the loop will skip the rest of the code in the current iteration and move on to the next iteration.
        continue # This will skip the rest of the code in the current iteration if i is even.
    print(i) # This will print the value of i in each iteration of the loop, but only if i is odd.
# Output: 1
#         3
#         5
#         7
#         9

# Do While loops
my_condition = 0

while True: # This is the syntax for a do while loop. The code inside the loop will be executed at least once, and then the condition will be checked after the first iteration.
    print(my_condition) # This will print the value of my_condition in each iteration of the loop.
    my_condition += 1 # This is the code that will be executed in each iteration of the loop. In this case, we are incrementing my_condition by 1 in each iteration.
    if my_condition > 10: # This is a condition that will be checked after the first iteration of the loop. If this condition is true, the loop will be terminated.
        print("my_condition is now greater than 10, breaking the loop")
        break # This will terminate the loop if my_condition is greater than 10.

print(f"my_condition is now: {my_condition}") # Output: my_condition is now: 11
print("Finished do while loop") # Output: Finished do while loop

# Nested loops
for key in range(3):
    for value in range(3):
        print(f"key: {key}, value: {value}") # Output: key: 0, value: 0
                                             #         key: 0, value: 1
                                             #         key: 0, value: 2
                                             #         key: 1, value: 0
                                             #         key: 1, value: 1
                                             #         key: 1, value: 2
                                             #         key: 2, value: 0
                                             #         key: 2, value: 1
                                             #         key: 2, value: 2

# List comprehension
my_list = [1, 2, 3, 4, 5]

my_list_squared = [i**2 for i in my_list] # This is the syntax for a list comprehension. We are creating a new list called my_list_squared that contains the squares of the elements in my_list.
print(my_list_squared) # Output: [1, 4, 9, 16, 25]