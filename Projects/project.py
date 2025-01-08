# Function to write data to a text file
def write_data(data, filename="data.txt"):
    with open(filename, "a") as file:  # Open file in append mode
        file.write(data + "\n")  # Write data followed by newline

# Function to read and display data from a text file
def read_data(filename="data.txt"):
    with open(filename, "r") as file:  # Open file in read mode
        content = file.read()  # Read all content from the file
        print("Data in file:")
        print(content)  # Display the content

# Sample usage
if __name__ == "__main__":
    data = input("Enter data to store: ")
    write_data(data)  # Store data in the file
    read_data()  # Retrieve and display data