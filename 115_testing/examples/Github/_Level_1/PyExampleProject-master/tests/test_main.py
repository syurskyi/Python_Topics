# pylint: disable=C0111

import helloworld
from helloworld.unnecessary_math import multiply


def test_numbers_3_4():
    a__ multiply(3, 4) == 12


def test_strings_a_3():
    a__ multiply('a', 3) == 'aaa'


def test_init():
    a__ helloworld.main() == "hello world"


def test_not_swag():
    a__ helloworld.main() != "swag"
