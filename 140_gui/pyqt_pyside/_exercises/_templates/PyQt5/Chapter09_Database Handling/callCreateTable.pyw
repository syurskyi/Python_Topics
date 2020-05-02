_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoCreateTable _____ *

tabledefinition=""
c_ MyForm(?D..

    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonCreateTable.clicked.c..(createTable)
        ui.pushButtonAddColumn.clicked.c..(addColumns)
        s..

    ___ addColumns
        global tabledefinition         
        __ tabledefinition__"":
            tabledefinition="CREATE TABLE IF NOT EXISTS "+ ui.lineEditTableName.text()+"("+ui.lineEditColumnName.text()+" "+ui.comboBoxDataType.itemText(ui.comboBoxDataType.currentIndex())
        else:
            tabledefinition+=", "+ui.lineEditColumnName.text()+" "+ui.comboBoxDataType.itemText(ui.comboBoxDataType.currentIndex())
        ui.lineEditColumnName.sT..("")
        ui.lineEditColumnName.setFocus()

    ___ createTable
        global tabledefinition 
        try:
            conn = sqlite3.c..(ui.lineEditDBName.text()+".db")
            ui.labelResponse.sT..("Database is connected")
            c = conn.cursor()
            tabledefinition+=");"
            c.execute(tabledefinition)
            ui.labelResponse.sT..("Table is successfully created")
        except Error as e:
            ui.labelResponse.sT..("Error in creating table")
        finally:
            conn.close()

__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
