def calculate(f_number):
    operation = input("Pick an operation (+, -, *, /): ")
    s_number = int(input("What's the next number?: "))

    if operation == '+':
        result = f_number + s_number
        print(f"{f_number} + {s_number} = {result}")
    elif operation == '-':
        result = f_number - s_number
        print(f"{f_number} - {s_number} = {result}")
    elif operation == '*':
        result = f_number * s_number
        print(f"{f_number} * {s_number} = {result}")
    elif operation == '/':
        if s_number == 0:
            print("Error: Division by zero.")
            return f_number  # Return the current number unchanged
        result = f_number / s_number
        print(f"{f_number} / {s_number} = {result}")
    else:
        print("Invalid operation.")
        return f_number  # Return the current number unchanged

    return result


# Main calculator loop
while True:
    f_number = int(input("What's the first number?: "))
    result = calculate(f_number)

    while True:
        cont = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
        if cont == 'y':
            result = calculate(result)
        elif cont == 'n':
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")
