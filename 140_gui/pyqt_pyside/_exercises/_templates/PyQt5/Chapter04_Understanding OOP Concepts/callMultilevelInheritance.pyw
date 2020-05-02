_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoMultilevelInheritance _____ _

c_ Student:
    name _ ""
    code _ ""
 
    ___  -  , code, name
        code _ code
        name _ name

    ___ getCode
        r_ code
    
    ___ getName
        r_ name


c_ Marks(Student
    historyMarks _ 0
    geographyMarks _ 0
 
    ___  -  ,  code, name, historyMarks, geographyMarks
        Student. -  ,code,name)
        historyMarks _ historyMarks
        geographyMarks _ geographyMarks
        
    ___ getHistoryMarks
        r_ historyMarks

    ___ getGeographyMarks
        r_ geographyMarks

c_ Result(Marks
    totalMarks _ 0
    percentage _ 0
 
    ___  -  ,  code, name, historyMarks, geographyMarks
        Marks. -  ,  code, name, historyMarks, geographyMarks)
        totalMarks _ historyMarks + geographyMarks
        percentage _ (historyMarks + geographyMarks) / 200 * 100
        
    ___ getTotalMarks
        r_ totalMarks

    ___ getPercentage
        r_ percentage

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ ?
        ui.sU..
        ui.ButtonClickMe.c___.c..(dispmessage)
        s..

    ___ dispmessage
        resultObj_Result(ui.lineEditCode.t..(), ui.lEN__.t..(), int(ui.lineEditHistoryMarks.t..()), int(ui.lineEditGeographyMarks.t..()))
        ui.lineEditTotal.sT..(st.(resultObj.getTotalMarks()))
        ui.lineEditPercentage.sT..(st.(resultObj.getPercentage()))

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e
