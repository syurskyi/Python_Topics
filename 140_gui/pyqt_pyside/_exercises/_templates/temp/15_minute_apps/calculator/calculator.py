____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *

______ operator

____ MainWindow ______ Ui_MainWindow

# Calculator state.
READY _ 0
INPUT _ 1


c_ MainWindow(QMainWindow, Ui_MainWindow):
    ___  -   *args, **kwargs):
        super(MainWindow, self). - (*args, **kwargs)
        setupUi

        # Setup numbers.
        ___ n __ range(0, 10):
            getattr  'pushButton_n%s' % n).pressed.c..(lambda v_n: input_number(v))

        # Setup operations.
        pushButton_add.pressed.c..(lambda: operation(operator.add))
        pushButton_sub.pressed.c..(lambda: operation(operator.sub))
        pushButton_mul.pressed.c..(lambda: operation(operator.mul))
        pushButton_div.pressed.c..(lambda: operation(operator.truediv))  # operator.div for Python2.7

        pushButton_pc.pressed.c..(operation_pc)
        pushButton_eq.pressed.c..(equals)

        # Setup actions
        actionReset.t__.c..(reset)
        pushButton_ac.pressed.c..(reset)

        actionExit.t__.c..(close)

        pushButton_m.pressed.c..(memory_store)
        pushButton_mr.pressed.c..(memory_recall)

        memory _ 0
        reset()

        s..

    ___ display
        lcdNumber.display(stack[-1])

    ___ reset
        state _ READY
        stack _ [0]
        last_operation _ N..
        current_op _ N..
        display()

    ___ memory_store
        memory _ lcdNumber.value()

    ___ memory_recall
        state _ INPUT
        stack[-1] _ memory
        display()

    ___ input_number  v):
        __ state == READY:
            state _ INPUT
            stack[-1] _ v
        ____
            stack[-1] _ stack[-1] * 10 + v

        display()

    ___ operation  op):
        __ current_op:  # Complete the current operation
            equals()

        stack.ap..(0)
        state _ INPUT
        current_op _ op

    ___ operation_pc
        state _ INPUT
        stack[-1] *_ 0.01
        display()

    ___ equals
        # Support to allow '=' to repeat previous operation
        # if no further input has been added.
        __ state == READY and last_operation:
            s, current_op _ last_operation
            stack.ap..(s)

        __ current_op:
            last_operation _ stack[-1], current_op

            try:
                stack _ [current_op(*stack)]
            except Exception:
                lcdNumber.display('Err')
                stack _ [0]
            ____
                current_op _ N..
                state _ READY
                display()


__ ______ __ ______
    app _ ?
    app.sAN..("Calculon")

    window _ MainWindow()
    app.e..
