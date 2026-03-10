### Classes ###

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This method is added to demonstrate that we can have methods in a class.
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # This method is added to demonstrate that we can have multiple methods in a class.
    def walk(self):
        print(f"{self.name} is walking.")

# Create an instance of the Person class
person1 = Person("Alice", 30)
print(person1.name) # Output: Alice
print(person1.age)  # Output: 30

# Call the say_hello method
person1.say_hello() # Output: Hello, my name is Alice and I am 30 years old.


# Create another instance of the Person class
person2 = Person("Bob", 25)
print(person2.name) # Output: Bob
print(person2.age)  # Output: 25

# Call the say_hello method
person2.say_hello() # Output: Hello, my name is Bob and I am 25 years old.

# Call the walk method
person2.walk()      # Output: Bob is walking.