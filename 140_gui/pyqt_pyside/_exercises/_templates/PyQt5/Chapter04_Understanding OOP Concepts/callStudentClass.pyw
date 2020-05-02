_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoStudentClass _____ *

c_ Student:
    name = ""
    code = ""
 
    ___  -  , code, name
        code = code
        name = name

    ___ getCode 
        return code
    
    ___ getName 
        return name

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.ButtonClickMe.clicked.c..(dispmessage)
        s..

    ___ dispmessage 
        studentObj=Student(ui.lineEditCode.text(), ui.lineEditName.text())  
        ui.labelResponse.sT..("Code: "+studentObj.getCode()+", Name:"+studentObj.getName())

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
