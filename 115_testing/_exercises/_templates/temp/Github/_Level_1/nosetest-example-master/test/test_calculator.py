"""Tests For a simple Calculator App."""
______ u__
____ app.calculator ______ Calculator


c_ TddPythonExample?.?
    """The Test Class."""

    ___ setUp
        """The setUp Method put things in place before each test case."""
        calc _ Calculator()

    ___ test_calculator_add_method_returns_correct_result
        """Test For Add Method."""
        result _ calc.add(2, 2)
        aE..(4, result)

    ___ test_calculator_returns_error_if_both_args_not_numbers
        """Test that raises ValueError when Strings are passed in."""
        aR..(V.., calc.add, 'two', 'three')

    ___ test_calculator_returns_error_message_if_x_arg_not_number
        """Test that raises ValueError when x arg isn't a number."""
        aR..(V.., calc.add, 'two', 3)

    ___ test_calculator_returns_error_message_if_y_arg_not_number
        """Test that raises ValueError when y arg isn't a number."""
        aR..(V.., calc.add, 2, 'three')


__ _____ __ _____
    ?.?
