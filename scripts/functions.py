# Function definition
def greet(name):
    return f"Hello, {name}!"

# Using the function
print(greet("Alice"))

# Function with multiple arguments
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

# Function with default arguments
def describe_person(name, age=30):
    return f"{name} is {age} years old."

print(describe_person("Bob"))
print(describe_person("Charlie", 25))
