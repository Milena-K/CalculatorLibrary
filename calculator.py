from typing import Union


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> Union[float, None]:
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
