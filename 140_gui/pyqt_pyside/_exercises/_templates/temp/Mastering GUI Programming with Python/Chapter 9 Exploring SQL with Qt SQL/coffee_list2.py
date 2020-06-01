______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtCore as qtc
____ ? ______ QtGui as qtg
____ ? ______ QtSql as qts


"""
TODO:

- Adding new reviews and new coffees

"""


class DateDelegate(qtw.QStyledItemDelegate):

    ___ createEditor(self, parent, option, proxyModelIndex):
        # make sure to explicitly set the parent
        # otherwise it pops up in a top-level window!
        date_inp _ qtw.QDateEdit(parent, calendarPopup_True)
        return date_inp


class CoffeeForm(qtw.QWidget):
    """Form to display/edit all info about a coffee"""

    ___ __init__(self, coffees_model, reviews_model):
        super().__init__()
        self.setLayout(qtw.QFormLayout())

        # Coffee Fields
        self.coffee_brand _ qtw.QLineEdit()
        self.layout().addRow('Brand: ', self.coffee_brand)
        self.coffee_name _ qtw.QLineEdit()
        self.layout().addRow('Name: ', self.coffee_name)
        self.roast _ qtw.QComboBox()
        self.layout().addRow('Roast: ', self.roast)

        # Map the coffee fields
        self.coffees_model _ coffees_model
        self.mapper _ qtw.QDataWidgetMapper(self)
        self.mapper.setModel(self.coffees_model)
        self.mapper.setItemDelegate(
            qts.QSqlRelationalDelegate(self))
        self.mapper.addMapping(
            self.coffee_brand,
            self.coffees_model.fieldIndex('coffee_brand')
        )
        self.mapper.addMapping(
            self.coffee_name,
            self.coffees_model.fieldIndex('coffee_name')
        )
        self.mapper.addMapping(
            self.roast,
            self.coffees_model.fieldIndex('description')
        )
        # retrieve a model for the roasts and setup the combo box
        roasts_model _ coffees_model.relationModel(
            self.coffees_model.fieldIndex('description'))
        self.roast.setModel(roasts_model)
        self.roast.setModelColumn(1)
        # Cause data to be written when changed

        # Reviews
        self.reviews _ qtw.QTableView()
        self.layout().addRow(self.reviews)
        self.reviews.setModel(reviews_model)
        self.reviews.hideColumn(0)
        self.reviews.hideColumn(1)
        self.reviews.horizontalHeader().setSectionResizeMode(
            4, qtw.QHeaderView.Stretch)


        # Using a custom delegate
        self.dateDelegate _ DateDelegate()
        self.reviews.setItemDelegateForColumn(
            reviews_model.fieldIndex('review_date'),
            self.dateDelegate)

        # add and delete reviews
        self.new_review _ qtw.?PB..(
            'New Review', c___self.add_review)
        self.delete_review _ qtw.?PB..(
            'Delete Review', c___self.delete_review)
        self.layout().addRow(self.new_review, self.delete_review)

    ___ show_coffee(self, coffee_index):
        self.mapper.setCurrentIndex(coffee_index.row())
        # show the reviews
        id_index _ coffee_index.siblingAtColumn(0)
        self.coffee_id _ int(self.coffees_model.data(id_index))
        self.reviews.model().setFilter(f'coffee_id = {self.coffee_id}')
        self.reviews.model().setSort(3, qtc.Qt.DescendingOrder)
        self.reviews.model().select()
        self.reviews.resizeRowsToContents()
        self.reviews.resizeColumnsToContents()

    ___ delete_review(self):
        for index in self.reviews.selectedIndexes() or []:
            self.reviews.model().removeRow(index.row())
        self.reviews.model().select()

    ___ add_review(self):
        reviews_model _ self.reviews.model()
        new_row _ reviews_model.record()
        defaults _ {
            'coffee_id': self.coffee_id,
            'review_date': qtc.QDate.currentDate(),
            'reviewer': '',
            'review': ''
        }
        for field, value in defaults.items
            index _ reviews_model.fieldIndex(field)
            new_row.setValue(index, value)
        inserted _ reviews_model.insertRecord(-1, new_row)
        if not inserted:
            error _ reviews_model.lastError().text()
            print(f"Insert Failed: {error}")
        # Select so the new row is editable
        reviews_model.select()


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        Code in this method should define window properties,
        create backend resources, etc.
        """
        super().__init__()
        # Code starts here
        self.stack _ qtw.QStackedWidget()
        self.setCentralWidget(self.stack)
        # Connect to the database
        db _ qts.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.db')
        if not db.open
            qtw.QMessageBox.critical(
                None, 'DB Connection Error',
                'Could not open database file: '
                f'{db.lastError().text()}')
            sys.exit(1)

        # Check for missing tables
        required_tables _ {'roasts', 'coffees', 'reviews'}
        missing_tables _ required_tables - set(db.tables())
        if missing_tables:
            qtw.QMessageBox.critical(
                None, 'DB Integrity Error',
                'Missing tables, please repair DB: '
                f'{missing_tables}')
            sys.exit(1)

        # Create the models
        self.reviews_model _ qts.QSqlTableModel()
        self.reviews_model.setTable('reviews')

        self.coffees_model _ qts.QSqlRelationalTableModel()
        self.coffees_model.setTable('coffees')
        self.coffees_model.setRelation(
            self.coffees_model.fieldIndex('roast_id'),
            qts.QSqlRelation('roasts', 'id', 'description')
        )
        self.coffees_model.setEditStrategy(0)
        self.coffees_model.dataChanged.c..(print)
        self.coffee_list _ qtw.QTableView()
        self.coffee_list.setModel(self.coffees_model)
        self.stack.addWidget(self.coffee_list)

        self.coffees_model.select()
        #self.show()
        #return
        self.show_list()

        # Inserting and deleting rows.
        toolbar _ self.addToolBar('Controls')
        toolbar.addAction('Delete Coffee(s)', self.delete_coffee)
        toolbar.addAction('Add Coffee', self.add_coffee)

        self.coffee_list.setItemDelegate(qts.QSqlRelationalDelegate())

        #self.show()
        #return

        # The coffee form
        self.coffee_form _ CoffeeForm(
            self.coffees_model,
            self.reviews_model
        )
        self.stack.addWidget(self.coffee_form)
        self.coffee_list.doubleClicked.c..(
            self.coffee_form.show_coffee)
        self.coffee_list.doubleClicked.c..(
            lambda: self.stack.setCurrentWidget(self.coffee_form))

        toolbar.addAction("Back to list", self.show_list)

        # Code ends here
        self.s..

    ___ delete_coffee(self):
        selected _ self.coffee_list.selectedIndexes()
        for index in selected or []:
            self.coffees_model.removeRow(index.row())
        self.coffees_model.select()

    ___ add_coffee(self):
        self.stack.setCurrentWidget(self.coffee_list)
        self.coffees_model.insertRows(
            self.coffees_model.rowCount(), 1)

    ___ show_list(self):
        self.coffee_list.resizeColumnsToContents()
        self.coffee_list.resizeRowsToContents()
        self.stack.setCurrentWidget(self.coffee_list)


if __name__ == '__main__':
    app _ qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
