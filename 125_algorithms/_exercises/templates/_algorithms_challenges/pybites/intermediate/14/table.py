_______ random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.s..
aliases = 'Pythonista Nerd Coder'.s..  * 2
points = random.sample(r..(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


___ generate_table(*args):
    sequences = zip(*args)
    ___ row __ sequences:
        num_args = l..(row)
        __ num_args __ 1:
            yield f"{row[0]}"
        ____ num_args __ 2:
            yield f"{row[0]}{SEPARATOR}{row[1]}"
        ____ num_args __ 3:
            yield f"{row[0]}{SEPARATOR}{row[1]}{SEPARATOR}{row[2]}"
        ____:
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