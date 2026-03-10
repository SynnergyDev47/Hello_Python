# Exceptions
n1, n2 = 5, "2"

"""print(n1 - n2) # TypeError: unsupported operand type(s) for -: 'int' and 'str'"""

# Handling exceptions using try-except block
try:
    print(n1 - n2)
    print("This will not be printed if an exception occurs.")
except TypeError as e:
    print("You can't subtract a string from an integer.")
    print("Error message:", e)

# Handling multiple exceptions
try:    result = n1 / 0
except ZeroDivisionError as e:
    print("You can't divide by zero.")
    print("Error message:", e)
else:    print("The result is:", result)

# Finally block
a = [1, 2, 3]

try:
    print(a[2])  # This will raise an IndexError
    print("It has been printed successfully.")

except IndexError as e:
    print("Index out of range.")
    print("Error message:", e)

finally:
    print("This will always be executed, regardless of exceptions.")