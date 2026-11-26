import sys


def encode_to_morse(s: str) -> str:
    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
        "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
        "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ",
        "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
        "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ",
    }

    text = s.upper()
    result = ""
    for char in text:
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        result += NESTED_MORSE[char]
    return (result)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        result = encode_to_morse(sys.argv[1])
        print(result)
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
