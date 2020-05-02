_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ LineEditClass _____ *

c_ Student:
    name _ ""
 
    ___  -  , name
        name _ name
 
    ___ printName 
        return name

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.ButtonClickMe.clicked.c..(dispmessage)
        s..

    ___ dispmessage 
        studentObj_Student(ui.lineEditName.text())
        ui.labelResponse.sT..("Hello "+studentObj.printName())

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
