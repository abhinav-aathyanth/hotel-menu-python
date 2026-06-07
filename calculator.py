def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    while True:
        num1 = get_number("Enter the first number: ")
        operator = input("Enter an operator (+, -, *, /): ").strip()
        num2 = get_number("Enter the second number: ")

        try:
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue

            print(f"Result: {result}")
        except ValueError as error:
            print(error)

        choice = input("Do you want to calculate again? (y/n): ").strip().lower()
        if choice != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
