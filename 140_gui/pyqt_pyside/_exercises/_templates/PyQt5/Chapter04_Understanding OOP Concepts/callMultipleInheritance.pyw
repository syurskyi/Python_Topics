_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoMultipleInheritance _____ _

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


c_ Marks:
    historyMarks _ 0
    geographyMarks _ 0
 
    ___  -  ,  historyMarks, geographyMarks
        historyMarks _ historyMarks
        geographyMarks _ geographyMarks
        
    ___ getHistoryMarks 
        return historyMarks

    ___ getGeographyMarks 
        return geographyMarks

c_ Result(Student, Marks
    totalMarks _ 0
    percentage _ 0
 
    ___  -  ,  code, name, historyMarks, geographyMarks
        Student. -  ,  code, name)
        Marks. -  , historyMarks, geographyMarks)
        totalMarks _ historyMarks + geographyMarks
        percentage _ (historyMarks + geographyMarks) / 200 * 100
        
    ___ getTotalMarks 
        return totalMarks

    ___ getPercentage 
        return percentage

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.ButtonClickMe.c___.c..(dispmessage)
        s..

    ___ dispmessage 
        resultObj_Result(ui.lineEditCode.t..(), ui.lEN__.t..(), int(ui.lineEditHistoryMarks.t..()), int(ui.lineEditGeographyMarks.t..()))
        ui.lineEditTotal.sT..(st.(resultObj.getTotalMarks()))
        ui.lineEditPercentage.sT..(st.(resultObj.getPercentage()))

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
