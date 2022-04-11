_______ unittest

_______ m__

____ complex_numbers _______ ComplexNumber


c_ ComplexNumbersTest(unittest.TestCase

    ___ test_real_part_of_a_purely_real_number
        input_number ComplexNumber(1, 0)
        assertEqual(input_number.real, 1)

    ___ test_real_part_of_a_purely_imaginary_number
        input_number ComplexNumber(0, 1)
        assertEqual(input_number.real, 0)

    ___ test_real_part_of_a_number_with_real_and_imaginary_part
        input_number ComplexNumber(1, 2)
        assertEqual(input_number.real, 1)

    ___ test_imaginary_part_of_a_purely_real_number
        input_number ComplexNumber(1, 0)
        assertEqual(input_number.imaginary, 0)

    ___ test_imaginary_part_of_a_purely_imaginary_number
        input_number ComplexNumber(0, 1)
        assertEqual(input_number.imaginary, 1)

    ___ test_maginary_part_of_a_number_with_real_and_imaginary_part
        input_number ComplexNumber(1, 2)
        assertEqual(input_number.imaginary, 2)

    ___ test_add_purely_real_numbers
        first_input ComplexNumber(1, 0)
        second_input ComplexNumber(3, 0)
        assertEqual(first_input.add(second_input).real, 4)
        assertEqual(first_input.add(second_input).imaginary, 0)

    ___ test_add_purely_imaginary_numbers
        first_input ComplexNumber(0, 1)
        second_input ComplexNumber(0, 3)
        assertEqual(first_input.add(second_input).real, 0)
        assertEqual(first_input.add(second_input).imaginary, 4)

    ___ test_add_numbers_with_real_and_imaginary_part
        first_input ComplexNumber(1, 2)
        second_input ComplexNumber(4, 6)
        assertEqual(first_input.add(second_input).real, 5)
        assertEqual(first_input.add(second_input).imaginary, 8)

    ___ test_subtract_purely_real_numbers
        first_input ComplexNumber(1, 0)
        second_input ComplexNumber(-1, 0)
        assertEqual(first_input.sub(second_input).real, 2)
        assertEqual(first_input.sub(second_input).imaginary, 0)

    ___ test_substract_numbers_with_real_and_imaginary_part
        first_input ComplexNumber(1, 2)
        second_input ComplexNumber(-2, -2)
        assertEqual(first_input.sub(second_input).real, 3)
        assertEqual(first_input.sub(second_input).imaginary, 4)

    ___ test_multiply_purely_real_numbers
        first_input ComplexNumber(1, 0)
        second_input ComplexNumber(2, 0)
        assertEqual(first_input.mul(second_input).real, 2)
        assertEqual(first_input.mul(second_input).imaginary, 0)

    ___ test_multiply_numbers_with_real_and_imaginary_part
        first_input ComplexNumber(1, 2)
        second_input ComplexNumber(-5, 10)
        assertEqual(first_input.mul(second_input).real, -5)
        assertEqual(first_input.mul(second_input).imaginary, 20)

    ___ test_divide_purely_real_numbers
        input_number ComplexNumber(1.0, 0.0)
        e.. ComplexNumber(0.5, 0.0)
        divider ComplexNumber(2.0, 0.0)
        assertEqual(e...real, input_number.div(divider).real)
        assertEqual(e...imaginary,
                         input_number.div(divider).imaginary)

    ___ test_divide_purely_imaginary_numbers
        input_number ComplexNumber(0, 1)
        e.. ComplexNumber(0.5, 0)
        divider ComplexNumber(0, 2)
        assertEqual(e...real, input_number.div(divider).real)
        assertEqual(e...imaginary,
                         input_number.div(divider).imaginary)

    ___ test_divide_numbers_with_real_and_imaginary_part
        input_number ComplexNumber(1, 2)
        e.. ComplexNumber(0.44, 0.08)
        divider ComplexNumber(3, 4)
        assertEqual(e...real, input_number.div(divider).real)
        assertEqual(e...imaginary,
                         input_number.div(divider).imaginary)

    ___ test_absolute_value_of_a_positive_purely_real_number
        assertEqual(ComplexNumber(5, 0).a..(), 5)

    ___ test_absolute_value_of_a_negative_purely_real_number
        assertEqual(ComplexNumber(-5, 0).a..(), 5)

    ___ test_absolute_value_of_imaginary_number_negative_imaginary_part
        assertEqual(ComplexNumber(0, -5).a..(), 5)

    ___ test_absolute_value_of_imaginary_number_positive_imaginary_part
        assertEqual(ComplexNumber(0, 5).a..(), 5)

    ___ test_absolute_value_of_a_number_with_real_and_imaginary_part
        assertEqual(ComplexNumber(3, 4).a..(), 5)

    ___ test_conjugate_a_purely_real_number
        input_number ComplexNumber(5, 0)
        e.. ComplexNumber(5, 0)
        assertEqual(e...real, input_number.conjugate().real)
        assertEqual(e...imaginary,
                         input_number.conjugate().imaginary)

    ___ test_conjugate_a_purely_imaginary_number
        input_number ComplexNumber(0, 5)
        e.. ComplexNumber(0, -5)
        assertEqual(e...real, input_number.conjugate().real)
        assertEqual(e...imaginary,
                         input_number.conjugate().imaginary)

    ___ conjugate_a_number_with_real_and_imaginary_part
        input_number ComplexNumber(1, 1)
        e.. ComplexNumber(1, -1)
        assertEqual(e...real, input_number.conjugate().real)
        assertEqual(e...imaginary,
                         input_number.conjugate().imaginary)

    ___ test_eulers_identity_formula
        input_number ComplexNumber(0, m__.pi)
        e.. ComplexNumber(-1, 0)
        assertEqual(e...real, input_number.exp().real)
        assertEqual(e...imaginary, input_number.exp().imaginary)

    ___ test_exponential_of_0
        input_number ComplexNumber(0, 0)
        e.. ComplexNumber(1, 0)
        assertEqual(e...real, input_number.exp().real)
        assertEqual(e...imaginary, input_number.exp().imaginary)

    ___ test_exponential_of_a_purely_real_number
        input_number ComplexNumber(1, 0)
        e.. ComplexNumber(m__.e, 0)
        assertEqual(e...real, input_number.exp().real)
        assertEqual(e...imaginary, input_number.exp().imaginary)


__ _____ __ _____
    unittest.main()
