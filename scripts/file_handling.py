# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example.\n")

# Reading from a file
print("Reading the file:")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appending new line.\n")

# Reading updated content
print("\nReading updated file:")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)