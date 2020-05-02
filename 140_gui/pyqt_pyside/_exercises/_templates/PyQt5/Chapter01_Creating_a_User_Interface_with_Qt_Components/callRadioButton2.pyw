_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoRadioButton2 _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.radioButtonMedium.toggled.c..(dispSelected)
        ui.radioButtonLarge.toggled.c..(dispSelected)
        ui.radioButtonXL.toggled.c..(dispSelected)
        ui.radioButtonXXL.toggled.c..(dispSelected)
        ui.radioButtonDebitCard.toggled.c..(dispSelected)
        ui.radioButtonNetBanking.toggled.c..(dispSelected)
        ui.radioButtonCashOnDelivery.toggled.c..(dispSelected)
        s..

    ___ dispSelected
        selected1="";
        selected2=""
        __ ui.radioButtonMedium.iC..__T..:
            selected1="Medium"
        __ ui.radioButtonLarge.iC..__T..:
            selected1="Large"
        __ ui.radioButtonXL.iC..__T..:
            selected1="Extra Large"
        __ ui.radioButtonXXL.iC..__T..:
            selected1="Extra Extra Large"
        __ ui.radioButtonDebitCard.iC..__T..:
            selected2="Debit/Credit Card"
        __ ui.radioButtonNetBanking.iC..__T..:
            selected2="NetBanking"
        __ ui.radioButtonCashOnDelivery.iC..__T..:
            selected2="Cash On Delivery"
        ui.labelSelected.sT..("Chosen shirt size is "+selected1+" and payment method as " + selected2)

__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
