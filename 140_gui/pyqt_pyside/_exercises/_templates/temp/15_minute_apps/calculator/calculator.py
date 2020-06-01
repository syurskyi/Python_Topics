____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *

______ operator

____ MainWindow ______ Ui_MainWindow

# Calculator state.
READY _ 0
INPUT _ 1


c_ MainWindow(QMainWindow, Ui_MainWindow):
    ___ __init__  *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Setup numbers.
        for n in range(0, 10):
            getattr  'pushButton_n%s' % n).pressed.c..(lambda v_n: self.input_number(v))

        # Setup operations.
        self.pushButton_add.pressed.c..(lambda: self.operation(operator.add))
        self.pushButton_sub.pressed.c..(lambda: self.operation(operator.sub))
        self.pushButton_mul.pressed.c..(lambda: self.operation(operator.mul))
        self.pushButton_div.pressed.c..(lambda: self.operation(operator.truediv))  # operator.div for Python2.7

        self.pushButton_pc.pressed.c..(self.operation_pc)
        self.pushButton_eq.pressed.c..(self.equals)

        # Setup actions
        self.actionReset.t__.c..(self.reset)
        self.pushButton_ac.pressed.c..(self.reset)

        self.actionExit.t__.c..(self.close)

        self.pushButton_m.pressed.c..(self.memory_store)
        self.pushButton_mr.pressed.c..(self.memory_recall)

        self.memory _ 0
        self.reset()

        self.s..

    ___ display(self):
        self.lcdNumber.display(self.stack[-1])

    ___ reset(self):
        self.state _ READY
        self.stack _ [0]
        self.last_operation _ N..
        self.current_op _ N..
        self.display()

    ___ memory_store(self):
        self.memory _ self.lcdNumber.value()

    ___ memory_recall(self):
        self.state _ INPUT
        self.stack[-1] _ self.memory
        self.display()

    ___ input_number  v):
        __ self.state == READY:
            self.state _ INPUT
            self.stack[-1] _ v
        ____
            self.stack[-1] _ self.stack[-1] * 10 + v

        self.display()

    ___ operation  op):
        __ self.current_op:  # Complete the current operation
            self.equals()

        self.stack.append(0)
        self.state _ INPUT
        self.current_op _ op

    ___ operation_pc(self):
        self.state _ INPUT
        self.stack[-1] *_ 0.01
        self.display()

    ___ equals(self):
        # Support to allow '=' to repeat previous operation
        # if no further input has been added.
        __ self.state == READY and self.last_operation:
            s, self.current_op _ self.last_operation
            self.stack.append(s)

        __ self.current_op:
            self.last_operation _ self.stack[-1], self.current_op

            try:
                self.stack _ [self.current_op(*self.stack)]
            except Exception:
                self.lcdNumber.display('Err')
                self.stack _ [0]
            ____
                self.current_op _ N..
                self.state _ READY
                self.display()


__ __name__ == '__main__':
    app _ ?
    app.sAN..("Calculon")

    window _ MainWindow()
    app.e..
