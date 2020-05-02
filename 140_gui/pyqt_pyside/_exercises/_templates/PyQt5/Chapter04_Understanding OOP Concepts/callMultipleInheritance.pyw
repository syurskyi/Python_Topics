_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoMultipleInheritance _____ *

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


c_ Marks:
    historyMarks = 0
    geographyMarks = 0
 
    ___  -  ,  historyMarks, geographyMarks
        historyMarks = historyMarks
        geographyMarks = geographyMarks
        
    ___ getHistoryMarks 
        return historyMarks

    ___ getGeographyMarks 
        return geographyMarks

c_ Result(Student, Marks
    totalMarks = 0
    percentage = 0
 
    ___  -  ,  code, name, historyMarks, geographyMarks
        Student. -  ,  code, name)
        Marks. -  , historyMarks, geographyMarks)
        totalMarks = historyMarks + geographyMarks
        percentage = (historyMarks + geographyMarks) / 200 * 100
        
    ___ getTotalMarks 
        return totalMarks

    ___ getPercentage 
        return percentage

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.ButtonClickMe.clicked.c..(dispmessage)
        s..

    ___ dispmessage 
        resultObj=Result(ui.lineEditCode.text(), ui.lineEditName.text(), int(ui.lineEditHistoryMarks.text()), int(ui.lineEditGeographyMarks.text()))
        ui.lineEditTotal.sT..(st.(resultObj.getTotalMarks()))
        ui.lineEditPercentage.sT..(st.(resultObj.getPercentage()))

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
