# test_calculator.py
______ u__
____ app.calculator ______ Calculator


c_ TddInPythonExample?.?
    """docstring for TddInPythonExample"""

    ___ setUp
        calc _ Calculator()

    ___ test_calculator_add_method_returns_correct_result
        result _ calc.add(2, 2)
        aE..(4, result)

    ___ test_calculator_returns_error_message_if_both_args_not_numbers
        aR..(V.., calc.add, 'two', 'three')

    ___ test_calculator_returns_error_message_if_x_args_not_number
        aR..(V.., calc.add, 'two', 3)

    ___ test_calculator_returns_error_message_if_y_args_not_number
        aR..(V.., calc.add, 2, 'three')


__ _____ __ _____
    ?.?
