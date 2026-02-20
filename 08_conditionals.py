### Conditionals ###

# If statement
print("If statement")
my_condition = False

if my_condition:
    print("The condition is True") # Output: The condition is True (this will not be printed since my_condition is False)

print("The condition is still True") # Output: The condition is still True

my_condition = 5 * 2

if my_condition == 10:
    print("The condition is True") # Output: The condition is True

# If-else statement
print("If-else statement")

my_condition = 5 * 2

if my_condition == 10:
    print("The condition is True") # Output: The condition is True
else:
    print("The condition is False")

my_condition = 5 * 3
if my_condition == 10:
    print("The condition is True")
else:
    print("The condition is False") # Output: The condition is False

# Elif statement
print("Elif statement")

my_condition = 5 * 3

if my_condition == 10:
    print("The condition is True")
elif my_condition == 15:
    print("The condition is 15") # Output: The condition is 15
else:
    print("The condition is False")

# Combining conditions with logical operators
print("Combining conditions with logical operators")

my_condition_a = True
my_condition_b = False

if my_condition_a and my_condition_b:
    print("Both conditions are True")
elif my_condition_a or my_condition_b:
    print("At least one condition is True") # Output: At least one condition is True

if not my_condition_b:
    print("my_condition_b is False") # Output: my_condition_b is False

my_string = ""

if my_string:
    print("The string is not empty") # Output: The string is not empty (this will not be printed since my_string is empty)
else:
    print("The string is empty") # Output: The string is empty

if len(my_string) == 0:
    print("The string is empty") # Output: The string is empty
else:
    print("The string is not empty")