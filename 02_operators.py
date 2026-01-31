# Operators in Python

# Arithmetic Operators
print(10 + 5)  # Addition: Output: 15
print(10 - 5)  # Subtraction: Output: 5
print(10 * 5)  # Multiplication: Output: 50
print(10 / 5)  # Division: Output: 2.0
print(10 // 3) # Floor Division: Output: 3
print(10 % 3)  # Modulus: Output: 1
print(10 ** 2) # Exponentiation: Output: 100

print("Hola " + "Python")  # String Concatenation: Output: Hola Python
print("Hola" - "Python")   # This will raise an error
print(int("4" ) + 5)  # Output: 9
print("4" * 3)  # String Repetition: Output: 444

# Comparison Operators
print(10 == 5)  # Equal to: Output: False
print(10 != 5)  # Not equal to: Output: True
print(10 > 5)   # Greater than: Output: True
print(10 < 5)   # Less than: Output: False
print(10 >= 5)  # Greater than or equal to: Output: True
print(10 <= 5)  # Less than or equal to: Output: False

# Logical Operators
print(True and False)  # Logical AND: Output: False
print(True or False)   # Logical OR: Output: True
print(not True)        # Logical NOT: Output: False

# Assignment Operators
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15
x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 12
x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 24
x /= 4  # Equivalent to x = x / 4
print(x)  # Output: 6.0
x //= 2  # Equivalent to x = x // 2
print(x)  # Output: 3.0
x %= 2  # Equivalent to x = x % 2
print(x)  # Output: 1.0
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 1.0

# Bitwise Operators
print(5 & 3)  # Bitwise AND: Output: 1
print(5 | 3)  # Bitwise OR: Output: 7
print(5 ^ 3)  # Bitwise XOR: Output: 6
print(~5)     # Bitwise NOT: Output: -6
print(5 << 1) # Bitwise Left Shift: Output: 10
print(5 >> 1) # Bitwise Right Shift: Output: 2

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)    # Membership test: Output: True
print(6 not in my_list) # Membership test: Output: True

# Identity Operators
a = [1, 2, 3]
b = a
print(a is b)      # Identity test: Output: True
print(a is not b)  # Identity test: Output: False
c = [1, 2, 3]
print(a is c)      # Identity test: Output: False
print(a is not c)  # Identity test: Output: True
print(id(a))  # Output: Memory address of a
print(id(b))  # Output: Memory address of b
print(id(c))  # Output: Memory address of c
print(type(a))  # Output: <class 'list'>

# Operator Precedence
result = 10 + 5 * 2  # Multiplication has higher precedence than addition
print(result)  # Output: 20
result = (10 + 5) * 2  # Parentheses change the precedence
print(result)  # Output: 30
result = 10 + 5 > 12 and 3 < 5  # Comparison and logical operators
print(result)  # Output: True
result = not (10 + 5 > 12)  # Using NOT operator
print(result)  # Output: False

# Combined Example
a = 10
b = 5
c = 2
final_result = (a + b) * c - (a / b)  # Combined operations
print(final_result)  # Output: 28.0
print(type(final_result))  # Output: <class 'float'>
print("Final result is:", final_result)  # Output: Final result is: 28.0
print(f"Final result is: {final_result}")  # Using f-string for formatted output

# End of operators.py