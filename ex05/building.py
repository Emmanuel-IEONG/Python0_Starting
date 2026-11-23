from sys import argv


def count_characters(text):
    """
    Displays the sums of each category of characters in text.

    Args:
        text (string): string where we count the sums
    """
    print(f"The text contains {len(text)} characters:")
    upper_char = sum(1 for char in text if char.isupper())
    lower_char = sum(1 for char in text if char.islower())
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation_char = sum(1 for char in text if char in punctuations)
    digit_char = sum(1 for char in text if char.isdigit())
    space_char = sum(1 for char in text if char.isspace())

    print(f"{upper_char} upper letters")
    print(f"{lower_char} lower letters")
    print(f"{punctuation_char} punctuation marks")
    print(f"{space_char} spaces")
    print(f"{digit_char} digits")


def main():
    """
    Takes a single string argument and displays the sums of its
    upper-case characters, lower-case characters,
    punctuation characters, digits, and spaces.

    Asks for input if none or nothing is provided.

    Raises AssertionError if more than one argument is provided.
    """
    try:
        if len(argv) < 2:
            try:
                text = input("What is the text to count?\n")
                text += "\n"
            except EOFError:
                pass
        elif len(argv) != 2:
            raise AssertionError("more than one argument is provided")
        elif len(argv) == 2:
            text = argv[1]
        count_characters(text)
    except AssertionError as err:
        print(f"{AssertionError.__name__} : {err}")


if __name__ == "__main__":
    main()
