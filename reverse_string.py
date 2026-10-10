def reverse_string(text):
    """Return text in reverse order without using a built-in reverse function."""
    reversed_text = ""
    for character in text:
        reversed_text = character + reversed_text
    return reversed_text


if __name__ == "__main__":
    value = input("Enter a string: ")
    print("Reversed string:", reverse_string(value))
