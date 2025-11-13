def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Error: Division by zero" if b == 0 else a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def main():
    print("Simple CLI Calculator")
    print("Available operations: +  -  *  /  **  %")
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operator: ")
            b = float(input("Enter second number: "))
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            elif op == '**':
                result = power(a, b)
            elif op == '%':
                result = modulus(a, b)
            else:
                print("Invalid operator")
                continue
            print(f"Result: {result}\n")
        except ValueError:
            print("Invalid input, please enter numbers.\n")
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont != 'y':
            print("Exiting calculator.")
            break

if __name__ == "__main__":
    main()
