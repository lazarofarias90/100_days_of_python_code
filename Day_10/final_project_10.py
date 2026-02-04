# 1. Atomic Functions (Basic building blocks)
def add(n1, n2):
    """Adds two numbers and returns the sum."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts n2 from n1 and returns the difference."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers and returns the product."""
    return n1 * n2

def divide(n1, n2):
    """Divides n1 by n2 and returns the quotient. Handles division by zero."""
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

# 2. The Calculation Controller (The "Brain")
def calculate(n1, n2, operation):
    """
    Receives two numbers and a symbol string.
    Uses conditional logic to call the correct function and return the result.
    """
    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return subtract(n1, n2)
    elif operation == "*":
        return multiply(n1, n2)
    elif operation == "/":
        return divide(n1, n2)
    else:
        return "Invalid operation symbol."

# 3. Main Program (The UI)
num1 = float(input("What's the first number?: "))
symbol = input("Pick an operation (+, -, *, /): ")
num2 = float(input("What's the second number?: "))

# We capture the RETURN of the brain into a variable
result = calculate(num1, num2, symbol)

print(f"{num1} {symbol} {num2} = {result}")