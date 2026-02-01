# Strings 

my_string = "My string"
my_other_string = "My other string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "This is a string\nwith a new line"
print(my_new_line_string)

my_tab_string = "\tThis is a string with a tab"
print(my_tab_string)

my_scape_string = "This is a string with a backslash \\"
print(my_scape_string)

# Formatted strings (f-strings)
name = "John"
surname = "Doe"
age = 30

print(f"My name is {name} {surname} and I am {age} years old.") # Output: My name is John Doe and I am 30 years old.

# Unpacking characters
a, b, c, d, e, f, g, h, i, j = "ABCDEFGHIJ"
print(a) # Output: A
print(e) # Output: E
print(j) # Output: J

# Division of strings
string_to_divide = "HelloWorld"
first_part = string_to_divide[:5]  # 'Hello'
second_part = string_to_divide[5:] # 'World'

# Reversing a string
reversed_string = string_to_divide[::-1]
print(reversed_string) # Output: dlroWolleH

# String methods
sample_string = "  Hello, World! Welcome to Python programming.  "
print(sample_string.upper())          # Output: "  HELLO, WORLD! WELCOME TO PYTHON PROGRAMMING.  "
print(sample_string.lower())          # Output: "  hello, world! welcome to python programming.  "
print(sample_string.strip())         # Output: "Hello, World! Welcome to Python programming."
print(sample_string.replace("World", "Universe")) # Output: "  Hello, Universe! Welcome to Python programming.  "
print(sample_string.split(" "))      # Output: ['','', 'Hello,', 'World!', 'Welcome', 'to', 'Python', 'programming.','']
print("World" in sample_string)      # Output: True
print("Python" not in sample_string)  # Output: False
print(sample_string.find("Welcome"))  # Output: 14
print(sample_string.count("o"))      # Output: 4
print(sample_string.startswith("  Hello")) # Output: True
print(sample_string.endswith("programming.  ")) # Output: True
print(sample_string.capitalize())    # Output: "  hello, world! welcome to python programming.  "
print(sample_string.title())         # Output: "  Hello, World! Welcome To Python Programming.  "
print(sample_string.isalpha())      # Output: False
print(sample_string.isdigit())      # Output: False
print(sample_string.isalnum())      # Output: False
print(sample_string.index("Python"))  # Output: 25
print(sample_string.center(50, "-")) # Output: "----------  Hello, World! Welcome to Python programming.  ----------"