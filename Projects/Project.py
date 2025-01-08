# Function to count even and odd numbers in a list
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Main program
def main():
    numbers = []  # List to store numbers
    print("Enter 5 numbers:")

    # Loop to get numbers from the user
    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Count even and odd numbers
    even_count, odd_count = count_even_odd(numbers)
    print("\nNumbers:", numbers)
    print(f"Even Numbers: {even_count}")
    print(f"Odd Numbers: {odd_count}")

if __name__ == "__main__":
    main()
