def count_vowels(text):
    """Return the number of vowels in text."""
    vowels = "aeiou"
    count = 0
    for character in text.lower():
        if character in vowels:
            count += 1
    return count


if __name__ == "__main__":
    value = input("Enter a string: ")
    print("Number of vowels:", count_vowels(value))
