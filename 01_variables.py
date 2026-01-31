# Variables in Python
my_string_variable = "My string variable"
print(my_string_variable) # Output: My string variable

my_integer_variable = 42
print(my_integer_variable) # Output: 42

my_boolean_variable = True
print(my_boolean_variable) # Output: True

# Concatenation of different variable types
print(my_string_variable, str(my_integer_variable), my_boolean_variable) # Output: My string variable 42 True
print("This is the value of my_integer_variable:", my_integer_variable) # Output: This is the value of my_integer_variable: 42

my_int_to_string_variable = str(my_integer_variable)
print(my_int_to_string_variable) # Output: 42
print(type(my_int_to_string_variable)) # Output: <class 'str'>

# System functions
print(len(my_string_variable)) # Output: 18

# Variables in one line
var1, var2, var3 = "Hello", 100, False
print(var1) # Output: Hello
print(var2) # Output: 100
print(var3) # Output: False


# User inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Your full name is:", first_name, last_name) # Output: Your full name is: [first_name] [last_name]

# Type annotations
address: str = "Main Street 123" 