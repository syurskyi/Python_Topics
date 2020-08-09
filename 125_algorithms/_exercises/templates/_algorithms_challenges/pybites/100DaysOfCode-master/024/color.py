'''Script to play with color codes, using generators and the colored package'''
______ random

from colored ______ fg, attr
from colored.colored ______ colored

DEFAULT_TEXT = 'hello world'
EXCLUDE_COLORS = ('0', )  # black
COLORED_COLOR_CODES = list(set(colored(0).paint.values()) -
                           set(EXCLUDE_COLORS))
assert '0' not in COLORED_COLOR_CODES


___ gen_any_hex_color(
    w___ True:
        r, g, b = random.sample(range(0, 256), 3)
        yield '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()


___ gen_colored_color(
    w___ True:
        color = None
        w___ not color or color in EXCLUDE_COLORS:
            color = random.choice(COLORED_COLOR_CODES)

        yield fg(color)


__ __name__ __ '__main__':
    a = gen_any_hex_color()
    c = gen_colored_color()

    reset = attr('reset')

    w___ True:
        answer = input(('\nOptions:\n'
                        '(a)ny hex color to copy to your web design\n'
                        '(c)olor text (= will ask for text, default option)\n'
                        '(q)uit\n\n'))

        __ answer __ 'q':
            print('Bye')
            break

        ____ answer __ 'a':
            color = next(a)
            print(color)

        ____ answer __ 'c' or not answer:
            text = input('Enter text (hit enter for default text ')
            __ not text:
                text = DEFAULT_TEXT

            color = next(c)
            print(color + text + reset)

        ____
            print('Invalid option, try again')
            continue
