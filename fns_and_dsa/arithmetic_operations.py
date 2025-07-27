
def perform_operation(num1,num2,operation):

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    else:
        return "Error: Unsupported operation. Please choose add, subtract, multiply, or divide."