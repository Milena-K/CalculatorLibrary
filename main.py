def add(x: float, y: float):
    return x + y

def sub(x: float, y: float):
    return x - y

def mult(x: float, y: float):
    return x * y

def div(x: float, y: float):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
