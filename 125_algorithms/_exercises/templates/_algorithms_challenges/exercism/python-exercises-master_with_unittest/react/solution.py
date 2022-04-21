c_ Cell(o..
    ___ -
        _watchers    # list
        _value N..
        counter 0

    ___ add_watcher  cell
        _watchers.a..(cell)

    $
    ___ value
        r.. _value

    @value.setter
    ___ value  new_value
        _value new_value
        counter += 1
        ___ cell __ _watchers:
            cell.compute()


c_ InputCell(Cell
    ___ - , initial_value
        super(InputCell, self).__init__()
        _value initial_value


c_ ComputeCell(Cell
    ___ - , inputs, compute_function
        super(ComputeCell, self).__init__()
        inputs inputs
        func compute_function
        callbacks s..()
        compute()
        _register_inputs()

    ___ _register_inputs
        ___ inp __ inputs:
            inp.add_watcher(self)

    ___ compute
        # Only compute this cell when all inputs have same counters
        __ l..(s..([inp.counter ___ inp __ inputs] > 1:
            r..
        new_val func([inp.v.. ___ inp __ inputs])
        __ new_val !_ _value:
            value new_val
            ___ cb __ callbacks:
                cb(new_val)

    ___ add_callback  callback
        callbacks.add(callback)

    ___ remove_callback  callback
        __ callback __ callbacks:
            callbacks.remove(callback)
