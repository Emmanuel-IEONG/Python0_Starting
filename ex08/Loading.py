from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = get_terminal_size().columns
    bar_length -= 41

    for index, elem in enumerate(lst):
        done = index + 1
        percent = int(done * 100 / total)
        filled = int(done * bar_length / total)
        bar = chr(0x2588) * filled + ' ' * (bar_length - filled)
        print(f"\r{percent:3d}%|{bar}| {done}/{total}", end='', flush=True)
        yield elem
    print()
