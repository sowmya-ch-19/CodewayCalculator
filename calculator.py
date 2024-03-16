def main():
    print("Welcome to the simple calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose the operation (+, -, *, /): ").strip()

            if operation == '+':
                result = num1 + num2
                print("The result is: ", result)
            elif operation == '-':
                result = num1 - num2
                print("The result is: ", result)
            elif operation == '*':
                result = num1 * num2
                print("The result is: ", result)
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print("The result is: ", result)
            else:
                print("Invalid operation. Please choose from +, -, *, /.")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another_calculation != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
