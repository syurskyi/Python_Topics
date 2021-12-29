import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args):
    sequences = zip(*args)
    for row in sequences:
        num_args = len(row)
        if num_args == 1:
            yield f"{row[0]}"
        elif num_args == 2:
            yield f"{row[0]}{SEPARATOR}{row[1]}"
        elif num_args == 3:
            yield f"{row[0]}{SEPARATOR}{row[1]}{SEPARATOR}{row[2]}"
        else:
            yield f"{row[0]}{SEPARATOR}{row[1]}{SEPARATOR}{row[2]}{SEPARATOR}{row[3]}"


#if __name__ == "__main__":
    # test = generate_table(names)
    # print(next(test))
    # print(next(test))
    # generate_table(names, aliases)
    # generate_table(names, aliases, points)
    # test1 = generate_table(names, aliases, points, awake)
    # print(next(test1))
    # print(next(test1))