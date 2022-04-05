_______ r__

names = 'Julian Bob PyBites Dante Martin Rodolfo'.s..
aliases = 'Pythonista Nerd Coder'.s..  * 2
points = r__.s.. r..(81, 101), 6)
awake = [T.., F..] * 3
SEPARATOR = ' | '


___ generate_table(*args
    sequences = z..(*args)
    ___ row __ sequences:
        num_args = l..(row)
        __ num_args __ 1:
            y.. f"{row[0]}"
        ____ num_args __ 2:
            y.. f"{row[0]}{SEPARATOR}{row[1]}"
        ____ num_args __ 3:
            y.. f"{row[0]}{SEPARATOR}{row[1]}{SEPARATOR}{row[2]}"
        ____
            y.. f"{row[0]}{SEPARATOR}{row[1]}{SEPARATOR}{row[2]}{SEPARATOR}{row[3]}"


#if __name__ == "__main__":
    # test = generate_table(names)
    # print(next(test))
    # print(next(test))
    # generate_table(names, aliases)
    # generate_table(names, aliases, points)
    # test1 = generate_table(names, aliases, points, awake)
    # print(next(test1))
    # print(next(test1))