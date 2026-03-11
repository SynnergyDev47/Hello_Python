### Modules ###

"""
Modules are files containing Python code. 
They can define functions, classes, and variables. 
They can also include runnable code. 
Grouping related code into a module makes the code easier to understand and use. 
It also makes it more organized and reusable.
"""

# Importing a module
import module

# Using a function from the module
module.sum(5, 10) # Output: 15

# Importing specific functions from a module
from module import sum

# Using the imported function
sum(5, 11) # Output: 16

import math

# Using a function from the math module
print(math.sqrt(16)) # Output: 4.0
print(math.pi) # Output: 3.141592653589793
print(math.pow(2, 3)) # Output: 8.0

# Importing a module with an alias
from math import sqrt as square_root

# Using the imported function with an alias
print(square_root(25)) # Output: 5.0