_____ ___

____ ?.?W.. _____ ?D.., ?A..,QTableWidgetItem
____ DemoTableWidget _____ *

c_ MyForm(?D..
    ___  -  ,data
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        data=data
        addcontent()

    ___ addcontent
        row=0
        for tup in data:
            col=0
            for item in tup:
                oneitem=QTableWidgetItem(item)
                ui.tableWidget.setItem(row, col, oneitem)
                col+=1
            row+=1
data=[]
data.append(('Suite', '40$'))
data.append(('Super Luxury', '30$'))
data.append(('Super Deluxe', '20$'))
data.append(('Ordinary', '10$'))

                
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm(data)
    w.s..
    ___.e..(app.exec_())
