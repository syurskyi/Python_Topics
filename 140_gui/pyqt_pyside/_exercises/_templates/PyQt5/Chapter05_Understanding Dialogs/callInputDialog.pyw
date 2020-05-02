_____ ___

____ ?.?W.. _____ ?D.., ?A.., QInputDialog

____ demoInputDialog _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.pushButtonCountry.c___.c..(dispmessage)
        s..

    ___ dispmessage 
      countries _ ("Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan")
      countryName, ok _ QInputDialog.getItem , "Input Dialog", "List of countries", countries, 0, False)
      __ ok and countryName:
          ui.lineEditCountry.sT..(countryName)

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e

