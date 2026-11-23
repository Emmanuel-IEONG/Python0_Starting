from sys import argv

args = argv
try:
    if len(args) < 2:
        exit()
    elif len(args) != 2:
        raise AssertionError("more than one argument is provided")

    try:
        number = int(args[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as err:
    print(f"{AssertionError.__name__} : {err}")
