### Functions ###

def my_function():
    print("Hello from a function")

my_function() # Output: Hello from a function

def sum_two_numbers(a, b):
    return a + b

result = sum_two_numbers(3, 5)
print(result) # Output: 8

def sum(a, b):
    print(a + b)

sum(3, 5) # Output: 8

def greet(name):
    print(f"Hello, {name}!")

greet("Aurelio") # Output: Hello, Aurelio!

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Aurelio") # Output: Hello, Aurelio!
greet("Aurelio", "Hi") # Output: Hi, Aurelio!

# Functions with external variables
my_greeting = "Hello"
my_second_greeting = "Hi"

def greet(greeting):
    print(greeting)

greet(my_greeting) # Output: Hello
greet(my_second_greeting) # Output: Hi

# Nested functions
def outer_function():
    print("This is the outer function")
    
    def inner_function():
        print("This is the inner function")
    
    inner_function() # This will call the inner function from within the outer function 

outer_function() # Output: This is the outer function
                 #         This is the inner function

# Calling a function from another function
def function_a():
    print("This is function A")

def function_b():
    print("This is function B")
    function_a() # This will call function_a from within function_b

function_b() # Output: This is function B
             #         This is function A

# Functions with variable number of arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result) # Output: 15

# Lambda functions
add = lambda x, y: x + y
result = add(3, 5)
print(result) # Output: 8

"""What is a lambda function?
A lambda function is a small anonymous function that can take any number of arguments, 
but can only have one expression. It is often used for short, 
simple functions that are not worth defining with a full function definition. 
Lambda functions are defined using the lambda keyword, followed by the arguments, 
a colon, and the expression. For example:
add = lambda x, y: x + y
This creates a lambda function that takes two arguments, x and y, and returns their sum.
Lambda functions can be used in various contexts, such as in higher-order functions like map(), 
filter(), and reduce(), or as a quick way to define a function for a specific task without needing to give it a name. 
For example:
squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
This will create a new list of squared numbers from the original list.
"""