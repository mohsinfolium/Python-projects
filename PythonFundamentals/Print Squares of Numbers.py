# Function to calculate squares of numbers in a list
def calculate_squares(numbers):
    squares = []
    for num in numbers:
        squares.append(num ** 2)
    return squares

# Main program
def main():
    print("Enter 5 numbers:")
    numbers = []  # List to store numbers

    # Loop to get numbers from the user
    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Calculate squares of the numbers
    squares = calculate_squares(numbers)

    # Display the results
    print("\nOriginal Numbers:", numbers)
    print("Squares:", squares)

# Run the program
if __name__ == "__main__":
    main()