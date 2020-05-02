_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoStudentClass _____ _

c_ Student:
    name _ ""
    code _ ""
 
    ___  -  , code, name
        code _ code
        name _ name

    ___ getCode 
        return code
    
    ___ getName 
        return name

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.ButtonClickMe.c___.c..(dispmessage)
        s..

    ___ dispmessage 
        studentObj_Student(ui.lineEditCode.t..(), ui.lEN__.t..())
        ui.lR___.sT..("Code: "+studentObj.getCode()+", Name:"+studentObj.getName())

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
