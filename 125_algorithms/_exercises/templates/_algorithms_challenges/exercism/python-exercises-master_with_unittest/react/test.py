_______ unittest
____ functools _______ partial

____ react _______ InputCell, ComputeCell


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class ReactTest(unittest.TestCase):

    ___ test_input_cells_have_a_value(self):
        input_ = InputCell(10)
        self.assertEqual(input_.value, 10)

    ___ test_can_set_input_cell_value(self):
        input_ = InputCell(4)
        input_.value = 20
        self.assertEqual(input_.value, 20)

    ___ test_compute_cells_calculate_initial_value(self):
        input_ = InputCell(1)
        output = ComputeCell([input_], l.... inputs: inputs[0] + 1)
        self.assertEqual(output.value, 2)

    ___ test_compute_cells_take_inputs_in_right_order(self):
        one = InputCell(1)
        two = InputCell(2)
        output = ComputeCell(
            [one, two],
            l.... inputs: inputs[0] + inputs[1]*10
        )
        self.assertEqual(output.value, 21)

    ___ test_compute_cells_update_value_when_dependencies_are_changed(self):
        input_ = InputCell(1)
        output = ComputeCell([input_], l.... inputs: inputs[0] + 1)

        input_.value = 3
        self.assertEqual(output.value, 4)

    ___ test_compute_cells_can_depend_on_other_compute_cells(self):
        input_ = InputCell(1)
        times_two = ComputeCell([input_], l.... inputs: inputs[0] * 2)
        times_thirty = ComputeCell([input_], l.... inputs: inputs[0] * 30)
        output = ComputeCell(
            [times_two, times_thirty],
            l.... inputs: inputs[0] + inputs[1]
        )

        self.assertEqual(output.value, 32)
        input_.value = 3
        self.assertEqual(output.value, 96)

    ___ test_compute_cells_fire_callbacks(self):
        input_ = InputCell(1)
        output = ComputeCell([input_], l.... inputs: inputs[0] + 1)

        observer    # list
        callback1 = self.callback_factory(observer)

        output.add_callback(callback1)
        input_.value = 3
        self.assertEqual(observer[-1], 4)

    ___ test_callbacks_only_fire_on_change(self):
        input_ = InputCell(1)
        output = ComputeCell(
            [input_],
            l.... inputs: 111 __ inputs[0] < 3 ____ 222
        )

        observer    # list
        callback1 = self.callback_factory(observer)

        output.add_callback(callback1)
        input_.value = 2
        self.assertEqual(observer, [])
        input_.value = 4
        self.assertEqual(observer[-1], 222)

    ___ test_callbacks_do_not_report_already_reported_values(self):
        input_ = InputCell(1)
        output = ComputeCell([input_], l.... inputs: inputs[0] + 1)

        observer    # list
        callback1 = self.callback_factory(observer)

        output.add_callback(callback1)
        input_.value = 2
        self.assertEqual(observer[-1], 3)
        input_.value = 3
        self.assertEqual(observer[-1], 4)

    ___ test_callbacks_can_fire_from_multiple_cells(self):
        input_ = InputCell(1)
        plus_one = ComputeCell([input_], l.... inputs: inputs[0] + 1)
        minus_one = ComputeCell([input_], l.... inputs: inputs[0] - 1)

        cb1_observer, cb2_observer    # list, []
        callback1 = self.callback_factory(cb1_observer)
        callback2 = self.callback_factory(cb2_observer)

        plus_one.add_callback(callback1)
        minus_one.add_callback(callback2)
        input_.value = 10

        self.assertEqual(cb1_observer[-1], 11)
        self.assertEqual(cb2_observer[-1], 9)

    ___ test_callbacks_can_be_added_and_removed(self):
        input_ = InputCell(11)
        output = ComputeCell([input_], l.... inputs: inputs[0] + 1)

        cb1_observer, cb2_observer, cb3_observer    # list, [], []
        callback1 = self.callback_factory(cb1_observer)
        callback2 = self.callback_factory(cb2_observer)
        callback3 = self.callback_factory(cb3_observer)

        output.add_callback(callback1)
        output.add_callback(callback2)
        input_.value = 31
        self.assertEqual(cb1_observer[-1], 32)
        self.assertEqual(cb2_observer[-1], 32)

        output.remove_callback(callback1)
        output.add_callback(callback3)
        input_.value = 41
        self.assertEqual(cb2_observer[-1], 42)
        self.assertEqual(cb3_observer[-1], 42)

        # Expect callback1 not to be called.
        self.assertEqual(l..(cb1_observer), 1)

    ___ test_removing_a_callback_multiple_times(self):
        """Guard against incorrect implementations which store their
        callbacks in an array."""
        input_ = InputCell(1)
        output = ComputeCell([input_], l.... inputs: inputs[0] + 1)

        cb1_observer, cb2_observer    # list, []
        callback1 = self.callback_factory(cb1_observer)
        callback2 = self.callback_factory(cb2_observer)

        output.add_callback(callback1)
        output.add_callback(callback2)
        output.remove_callback(callback1)
        output.remove_callback(callback1)
        output.remove_callback(callback1)
        input_.value = 2

        self.assertEqual(cb1_observer, [])
        self.assertEqual(cb2_observer[-1], 3)

    ___ test_callbacks_should_only_be_called_once(self):
        """Guard against incorrect implementations which call a callback
        function multiple times when multiple dependencies change."""
        input_ = InputCell(1)
        plus_one = ComputeCell([input_], l.... inputs: inputs[0] + 1)
        minus_one1 = ComputeCell([input_], l.... inputs: inputs[0] - 1)
        minus_one2 = ComputeCell([minus_one1], l.... inputs: inputs[0] - 1)
        output = ComputeCell(
            [plus_one, minus_one2],
            l.... inputs: inputs[0] * inputs[1]
        )

        observer    # list
        callback1 = self.callback_factory(observer)

        output.add_callback(callback1)
        input_.value = 4
        self.assertEqual(observer[-1], 10)

    ___ test_callbacks_not_called_so_long_as_output_not_changed(self):
        """Guard against incorrect implementations which call callbacks
        if dependencies change but output value doesn't change."""
        input_ = InputCell(1)
        plus_one = ComputeCell([input_], l.... inputs: inputs[0] + 1)
        minus_one = ComputeCell([input_], l.... inputs: inputs[0] - 1)
        always_two = ComputeCell(
            [plus_one, minus_one],
            l.... inputs: inputs[0] - inputs[1]
        )

        observer    # list
        callback1 = self.callback_factory(observer)

        always_two.add_callback(callback1)
        input_.value = 2
        input_.value = 3
        input_.value = 4
        input_.value = 5
        self.assertEqual(observer, [])

    # Utility functions.
    ___ callback_factory(self, observer):
        ___ callback(observer, value):
            observer.a..(value)
        r.. partial(callback, observer)


__ __name__ __ '__main__':
    unittest.main()
