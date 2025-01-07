# Function to find the largest number in a list
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Main program
def main():
    numbers = []  # List to store numbers
    print("Enter 5 numbers:")

    # Loop to get numbers from the user
    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Find the largest number
    largest = find_largest(numbers)
    print("\nNumbers:", numbers)
    print("Largest Number:", largest)

if __name__ == "__main__":
    main()