def find_largest(numbers):
    """Return the largest number in a non-empty list without using max()."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


if __name__ == "__main__":
    values = input("Enter numbers separated by commas: ")
    numbers = [int(value.strip()) for value in values.split(",")]
    print("Largest number:", find_largest(numbers))
