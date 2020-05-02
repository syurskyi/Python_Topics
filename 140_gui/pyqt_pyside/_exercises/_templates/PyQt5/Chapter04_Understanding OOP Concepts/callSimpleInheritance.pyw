_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoSimpleInheritance _____ _

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
        ui.sU..
        ui.ButtonClickMe.c___.c..(dispmessage)
        s..

    ___ dispmessage 
        marksObj_Marks(ui.lineEditCode.t..(), ui.lEN__.t..(), ui.lineEditHistoryMarks.t..(), ui.lineEditGeographyMarks.t..())
        ui.lR___.sT..("Code: "+marksObj.getCode()+", Name:"+marksObj.getName()+"\nHistory Marks:"+marksObj.getHistoryMarks()+", Geography Marks:"+marksObj.getGeographyMarks())

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ ?
    w.s..
    ___.e..(app.e
