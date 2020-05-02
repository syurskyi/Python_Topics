_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoSimpleInheritance _____ *

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


c_ Marks(Student
    historyMarks = 0
    geographyMarks = 0
 
    ___  -  ,  code, name, historyMarks, geographyMarks
        Student. -  ,code,name)
        historyMarks = historyMarks
        geographyMarks = geographyMarks
        
    ___ getHistoryMarks 
        return historyMarks

    ___ getGeographyMarks 
        return geographyMarks
    

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.ButtonClickMe.clicked.c..(dispmessage)
        s..

    ___ dispmessage 
        marksObj=Marks(ui.lineEditCode.text(), ui.lineEditName.text(), ui.lineEditHistoryMarks.text(), ui.lineEditGeographyMarks.text())  
        ui.labelResponse.sT..("Code: "+marksObj.getCode()+", Name:"+marksObj.getName()+"\nHistory Marks:"+marksObj.getHistoryMarks()+", Geography Marks:"+marksObj.getGeographyMarks())

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
