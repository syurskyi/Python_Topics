_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ LineEditClass _____ *

c_ Student:
    name = ""
 
    ___  -  , name
        name = name
 
    ___ printName 
        return name

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.ButtonClickMe.clicked.c..(dispmessage)
        s..

    ___ dispmessage 
        studentObj=Student(ui.lineEditName.text())  
        ui.labelResponse.sT..("Hello "+studentObj.printName())

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
