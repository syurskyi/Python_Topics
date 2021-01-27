def concat(x, y):
    return '{} {}'.format(x, y)


def sum_3_elem(a, b, c):
    return a + b + c


def multiply_3_elem(a, b, c):
    return a * b * c


def test_concat():
    a__ concat(1, 2) == '1 2'
    a__ concat(10, 20) == '10 20'


def test_sum_3_elem():
    a__ sum_3_elem(0, 2, 3) == 5
    a__ sum_3_elem(1, 2, 3) == 6
    a__ sum_3_elem(1, 3, 7) == 11


def test_multiply_3_elem():
    a__ multiply_3_elem(1, 2, 3) == 6
    a__ multiply_3_elem(2, 3, 4) == 24


test_functions = [
    test_concat,
    test_sum_3_elem,
    test_multiply_3_elem
]

if __name__ == '__main__':
    for func in test_functions:
        try:
            func()
        except Exception as e:
            print('Failed: {} => {}: {}'.format(func, type(e), e))
