def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("factorial is not defined for negative numbers")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


if __name__ == "__main__":
    value = int(input("Enter a non-negative integer: "))
    print(f"{value}! =", factorial(value))
