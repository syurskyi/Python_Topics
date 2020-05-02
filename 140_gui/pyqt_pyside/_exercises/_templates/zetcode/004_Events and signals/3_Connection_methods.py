____ ?.?C.. ______ __
____ ?.?W.. ______ *

c_ myWidget(W..):
    ___ -
        s__(myWidget,  .-
        layout _ ?VB..(
        button _ ?P..('Print')
        layout.aW..(button)
        line _ QLineEdit
        layout.aW..(line)
        line.textChanged.c..(text)
        # first version
        # button.clicked.c..(self.action)
        # second version
        # self.c..(button, SIGNAL('clicked()'), self, SLOT('action()'))
        # third version
        @button.c__.c..
        ___ click :
            action

    # @SLOT()
    ___ action
        print('ACTION')

    ___ text(self, arg):
        print(arg)



___ start :
    #global form
    start.form _ myWidget
    start.form.show

start