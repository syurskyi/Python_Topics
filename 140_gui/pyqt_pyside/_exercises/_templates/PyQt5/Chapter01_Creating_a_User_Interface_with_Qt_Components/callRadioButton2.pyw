_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoRadioButton2 _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
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
        selected1_"";
        selected2_""
        __ ui.radioButtonMedium.iC..__T..:
            selected1_"Medium"
        __ ui.radioButtonLarge.iC..__T..:
            selected1_"Large"
        __ ui.radioButtonXL.iC..__T..:
            selected1_"Extra Large"
        __ ui.radioButtonXXL.iC..__T..:
            selected1_"Extra Extra Large"
        __ ui.radioButtonDebitCard.iC..__T..:
            selected2_"Debit/Credit Card"
        __ ui.radioButtonNetBanking.iC..__T..:
            selected2_"NetBanking"
        __ ui.radioButtonCashOnDelivery.iC..__T..:
            selected2_"Cash On Delivery"
        ui.labelSelected.sT..("Chosen shirt size is "+selected1+" and payment method as " + selected2)

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
