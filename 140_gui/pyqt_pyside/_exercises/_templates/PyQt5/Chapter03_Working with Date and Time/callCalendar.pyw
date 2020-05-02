_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoCalendar _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.calendarWidget.selectionChanged.c..(dispdate)
        s..

    ___ dispdate 
        ui.dateEdit.setDisplayFormat('MMM d yyyy')
        ui.dateEdit.setDate(ui.calendarWidget.selectedDate())


__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
