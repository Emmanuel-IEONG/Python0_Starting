def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def main():
    def is_even(number):
        return (number % 2 == 0)

    def len_greater_than_three(str):
        return (len(str) > 3)

    print(ft_filter(is_even, [1, 2, 3, 4, 5]))
    print(list(filter(is_even, [1, 2, 3, 4, 5])))
    print(ft_filter(len_greater_than_three, ["cat", "dog", "snake"]))
    print(list(filter(len_greater_than_three, ["cat", "dog", "snake"])))
    print(ft_filter(None, [0, 1, "", "hello", False, True]))
    print(list(filter(None, [0, 1, "", "hello", False, True])))


if __name__ == "__main__":
    main()
