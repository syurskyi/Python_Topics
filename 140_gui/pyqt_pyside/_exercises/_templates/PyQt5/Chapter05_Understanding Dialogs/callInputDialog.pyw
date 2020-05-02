_____ ___

____ ?.?W.. _____ ?D.., ?A.., QInputDialog

____ demoInputDialog _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonCountry.clicked.c..(dispmessage)
        s..

    ___ dispmessage 
      countries = ("Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan")
      countryName, ok = QInputDialog.getItem , "Input Dialog", "List of countries", countries, 0, False)			
      __ ok and countryName:
          ui.lineEditCountry.sT..(countryName)

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())

