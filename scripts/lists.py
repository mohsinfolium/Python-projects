# List creation
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("date")
print("After append:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Iterating over a list
print("\nIterating through the list:")
for fruit in fruits:
    print(fruit)

# Slicing a list
print("\nSliced list:", fruits[1:3])
