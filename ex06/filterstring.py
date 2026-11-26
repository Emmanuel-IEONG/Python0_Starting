import sys
from ft_filter import ft_filter


def main():
    """
    Outputs a list of words from S (string) that have lenght greater
    than N (int).

    Raises AssertionError if the number of arguments is different from 2
    or if the type of any argument is wrong.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = s.split(' ')
        result = ft_filter(lambda word: len(word) > n, words)

        print(result)
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
