def is_palindrome(number):
    """Return whether a non-negative integer reads the same forwards and backwards."""
    if number < 0:
        return False

    original = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original == reversed_number


if __name__ == "__main__":
    value = int(input("Enter an integer: "))
    if is_palindrome(value):
        print(value, "is a palindrome.")
    else:
        print(value, "is not a palindrome.")
