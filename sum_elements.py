# A refactored program to sum user-provided integers with improved error handling and structure.

MAX = 100

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def get_number_of_elements():
    """Prompt the user for the number of elements to sum."""
    while True:
        try:
            n = int(input("Enter the number of elements (1-100): "))
            if 1 <= n <= MAX:
                return n
            else:
                print("Invalid input. Please provide a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n):
    """Prompt the user to input `n` integers."""
    numbers = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        while True:
            try:
                number = int(input())
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return numbers

def main():
    try:
        n = get_number_of_elements()
        numbers = get_elements(n)
        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
