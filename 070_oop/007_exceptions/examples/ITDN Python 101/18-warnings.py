import warnings


def input_body_parameter(name, unit, supposed_maximum):
    parameter = float(input('Enter your {} (in {}): '.format(name, unit)))
    if parameter <= 0:
        raise ValueError(name + ' cannot be negative')
    if parameter > supposed_maximum:
        warnings.warn('suspiciously large value of ' + name)
    return parameter


def input_mass():
    return input_body_parameter(name='mass', unit='kg', supposed_maximum=100)


def input_height():
    return input_body_parameter(name='height', unit='m', supposed_maximum=2)


def calculate_bmi(mass, height):
    return mass / (height ** 2)


def main():
    mass = input_mass()
    height = input_height()
    bmi = calculate_bmi(mass, height)
    print('Your body mass index is', bmi)


if __name__ == '__main__':
    main()
