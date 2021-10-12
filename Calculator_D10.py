from Calculator_logo import logo

def addition(n1, n2):
    return n1+n2

def substraction(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2


def calculator():
    print(logo)
    operation = {
                "+" : addition,
                "-" : substraction,
                "*" : multiply,
                "/" : division
                }

    continue_program = True
    number1 = float(input("Whats the first number?\n"))
    for symbol in operation:
            print(symbol)
            
    while continue_program:
        
        operation_type = input("Pick operation: ")
        number2 = float(input("Whats the next number?\n"))
        calculate = operation[operation_type]
        result = calculate(number1, number2)
        print(f" {number1} {operation_type} {number2} = {result}")
        next = (input(f"Type 'Y' to continue calculation with {result}, or type 'N' to start a new calculation: \n").lower())
        number1 = result
        
        
        if next == "n":
            continue_program = False
            calculator()
            
calculator()