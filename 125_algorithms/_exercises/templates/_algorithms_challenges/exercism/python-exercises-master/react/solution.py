class Cell(object
    ___ __init__(self
        self._watchers =   # list
        self._value = None
        self.counter = 0

    ___ add_watcher(self, cell
        self._watchers.append(cell)

    @property
    ___ value(self
        r_ self._value

    @value.setter
    ___ value(self, new_value
        self._value = new_value
        self.counter += 1
        ___ cell __ self._watchers:
            cell.compute()


class InputCell(Cell
    ___ __init__(self, initial_value
        super(InputCell, self).__init__()
        self._value = initial_value


class ComputeCell(Cell
    ___ __init__(self, inputs, compute_function
        super(ComputeCell, self).__init__()
        self.inputs = inputs
        self.func = compute_function
        self.callbacks = set()
        self.compute()
        self._register_inputs()

    ___ _register_inputs(self
        ___ inp __ self.inputs:
            inp.add_watcher(self)

    ___ compute(self
        # Only compute this cell when all inputs have same counters
        __ le.(set([inp.counter ___ inp __ self.inputs])) > 1:
            r_
        new_val = self.func([inp.value ___ inp __ self.inputs])
        __ new_val != self._value:
            self.value = new_val
            ___ cb __ self.callbacks:
                cb(new_val)

    ___ add_callback(self, callback
        self.callbacks.add(callback)

    ___ remove_callback(self, callback
        __ callback __ self.callbacks:
            self.callbacks.remove(callback)
