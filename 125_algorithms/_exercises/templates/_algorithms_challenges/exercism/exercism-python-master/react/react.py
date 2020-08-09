CELLS = []

class InputCell(object
    ___ __init__(self, initial_value
        self._value = initial_value
        CELLS.append(self)

    @property
    ___ value(self
        r_ self._value

    @value.setter
    ___ value(self, value
        __ self._value != value:
            self._value = value
            ___ cell in CELLS:
                cell._update()

    ___ _update(self
        r_ self._value


class ComputeCell(object
    ___ __init__(self, inputs, compute_function
        self._function = lambda: compute_function([i.value ___ i in inputs])
        self._callbacks = {}
        self._value = self._function()
        CELLS.append(self)

    @property
    ___ value(self
        r_ self._value

    ___ _update(self
        new_val = self._function()
        __ new_val != self._value:
            self._value = new_val
            ___ c in self._callbacks.values(
                c(new_val)
        r_ new_val

    ___ add_callback(self, callback
        self._callbacks[callback] = callback
        r_ callback

    ___ remove_callback(self, callback
        try:
            del self._callbacks[callback]
        except KeyError:
            pass
