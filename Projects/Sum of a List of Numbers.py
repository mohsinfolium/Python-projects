# Function to calculate the sum of a list
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main program
def main():
    numbers = []  # List to store numbers
    print("Enter 5 numbers:")

    # Loop to get numbers from the user
    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Calculate the sum
    total = calculate_sum(numbers)
    print("\nNumbers:", numbers)
    print("Sum:", total)

if __name__ == "__main__":
    main()