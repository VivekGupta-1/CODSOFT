# Simple Calculator Program

def calculator():
    # Prompt user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt user to input an operation choice
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2!= 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Error: Invalid operation!")
        return

    # Display the result
    print("Result:", result)

# Call the calculator function
calculator()