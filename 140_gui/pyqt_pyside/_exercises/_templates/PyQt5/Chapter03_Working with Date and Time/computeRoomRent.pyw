_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ reservehotel _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        roomtypes_['Suite', 'Super Luxury', 'Super Deluxe', 'Ordinary']
        addcontent()     
        ui.pushButton.clicked.c..(computeRoomRent) 
        s..

    ___ addcontent 
        for i in roomtypes:
          ui.comboBox.addItem(i)
     
    ___ computeRoomRent 
        dateselected_ui.calendarWidget.selectedDate()
        dateinstring_st.(dateselected.toPyDate())
        noOfDays_ui.spinBox.value()
        chosenRoomType_ui.comboBox.itemText(ui.comboBox.currentIndex())
        ui.Enteredinfo.sT..('Date of reservation: '+dateinstring+ ', Number of days: '+ st.(noOfDays) + ' \nand Room type selected: '+ chosenRoomType)
        roomRent_0
        __ chosenRoomType__"Suite":
          roomRent_40
        __ chosenRoomType__"Super Luxury":
          roomRent_30
        __ chosenRoomType__"Super Deluxe":
          roomRent_20
        __ chosenRoomType__"Ordinary":
          roomRent_10
        total_roomRent*noOfDays
        ui.RoomRentinfo.sT..('Room Rent for single day for '+ chosenRoomType +' type is '+ st.(roomRent)+ '$. \nTotal room rent is '+ st.(total)+ '$')
 
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
