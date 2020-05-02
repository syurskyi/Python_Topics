_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoSimpleInheritance _____ *

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


c_ Marks(Student
    historyMarks _ 0
    geographyMarks _ 0
 
    ___  -  ,  code, name, historyMarks, geographyMarks
        Student. -  ,code,name)
        historyMarks _ historyMarks
        geographyMarks _ geographyMarks
        
    ___ getHistoryMarks 
        return historyMarks

    ___ getGeographyMarks 
        return geographyMarks
    

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.ButtonClickMe.clicked.c..(dispmessage)
        s..

    ___ dispmessage 
        marksObj_Marks(ui.lineEditCode.text(), ui.lineEditName.text(), ui.lineEditHistoryMarks.text(), ui.lineEditGeographyMarks.text())
        ui.labelResponse.sT..("Code: "+marksObj.getCode()+", Name:"+marksObj.getName()+"\nHistory Marks:"+marksObj.getHistoryMarks()+", Geography Marks:"+marksObj.getGeographyMarks())

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
