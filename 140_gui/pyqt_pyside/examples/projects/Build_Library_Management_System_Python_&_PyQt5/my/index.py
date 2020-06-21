from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os
import sqlite3
import datetime
from xlrd import *
from xlsxwriter import *

# ui = loadUiType('library.ui')[0]
ui,_ = loadUiType('library.ui')

# ui = loadUiType('library.ui')[0]
login_ui,_ = loadUiType('login.ui')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Login(QWidget , login_ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.handel_login)
        style = open(resource_path('themes/darkorange.css') , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def handel_login(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = """SELECT * FROM users"""

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Enterd Your Username And Password Correctly')


class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui_changes()
        self.handle_buttons()
        self.dark_orange_theme()

        self.show_author()
        self.show_category()
        self.show_publisher()

        self.show_category_combobox()
        self.show_author_combobox()
        self.show_publisher_combobox()

        self.show_all_clients()
        self.show_all_books()

        self.show_all_operations()

    def handel_ui_changes(self):
        self.hidding_themes()
        self.tabWidget.tabBar().setVisible(False)

    def handle_buttons(self):
        self.pushButton_5.clicked.connect(self.show_themes)
        self.pushButton_49.clicked.connect(self.hidding_themes)

        self.pushButton.clicked.connect(self.open_day_to_day_tab)
        self.pushButton_2.clicked.connect(self.open_books_tab)
        self.pushButton_26.clicked.connect(self.open_clients_tab)
        self.pushButton_3.clicked.connect(self.open_users_tab)
        self.pushButton_4.clicked.connect(self.open_settings_tab)

        self.pushButton_7.clicked.connect(self.add_new_book)
        self.pushButton_9.clicked.connect(self.search_books)
        self.pushButton_8.clicked.connect(self.edit_books)
        self.pushButton_10.clicked.connect(self.delete_books)

        self.pushButton_14.clicked.connect(self.add_category)
        self.pushButton_15.clicked.connect(self.add_author)
        self.pushButton_16.clicked.connect(self.add_publisher)

        self.pushButton_11.clicked.connect(self.add_new_user)
        self.pushButton_12.clicked.connect(self.login)
        self.pushButton_13.clicked.connect(self.edit_user)

        self.pushButton_46.clicked.connect(self.dark_orange_theme)
        self.pushButton_45.clicked.connect(self.dark_blue_theme)
        self.pushButton_48.clicked.connect(self.dark_gray_theme)
        self.pushButton_47.clicked.connect(self.qdark_theme)
        
        self.pushButton_22.clicked.connect(self.add_new_client)
        self.pushButton_24.clicked.connect(self.search_client)
        self.pushButton_23.clicked.connect(self.edit_client)
        self.pushButton_25.clicked.connect(self.delete_client)

        self.pushButton_6.clicked.connect(self.handel_day_operations)

        self.pushButton_29.clicked.connect(self.export_day_operations)
        self.pushButton_27.clicked.connect(self.export_books)
        self.pushButton_28.clicked.connect(self.export_clients)

    def show_themes(self):
        self.groupBox_3.show()

    def hidding_themes(self):
        self.groupBox_3.hide()

    # #################################################################################################################
    # ############################## openning tabs ####################################################################

    def open_day_to_day_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def open_books_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def open_clients_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def open_users_tab(self):
        self.tabWidget.setCurrentIndex(3)

    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(4)

    # #################################################################################################################
    # ############################## Day Operations ###################################################################

    def handel_day_operations(self):
        book_title = self.lineEdit.text()
        client_name = self.lineEdit_29.text()
        type = self.comboBox.currentText()
        days_number = self.comboBox_2.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days_number)

        print(today_date)
        print(to_date)

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""INSERT INTO dayoperations
                            (book_name,
                            client, 
                            type,
                            days, 
                            date, 
                            to_date )
                            VALUES (?, ?, ?, ?, ?, ?)""",
                         (book_title,
                          client_name,
                          type,
                          days_number,
                          today_date,
                          to_date))

        self.db.commit()
        self.statusBar().showMessage('New Operation Added')

        self.show_all_operations()

    def show_all_operations(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT book_name , client , type , date , to_date FROM dayoperations""")

        data = self.cur.fetchall()

        print(data)

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

    # #################################################################################################################
    # ############################## Books ############################################################################

    def show_all_books(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT book_code, 
                                   book_name, 
                                   book_description,
                                   book_category, 
                                   book_author,
                                   book_publisher, 
                                   book_price FROM book""")
        data = self.cur.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close

    def add_new_book(self):

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_4.text()

        self.cur.execute("""INSERT INTO book(
                                             book_name, 
                                             book_description, 
                                             book_code, 
                                             book_category, 
                                             book_author, 
                                             book_publisher, 
                                             book_price)
                                             VALUES (?, ?, ?, ?, ?, ?, ?)""",
                         (book_title, book_description, book_code, book_category, book_author, book_publisher ,book_price))

        self.db.commit()
        self.statusBar().showMessage("New Book has been added")

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_4.setText('')
        self.show_all_books()

    def search_books(self):

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()

        sql = """SELECT * FROM book WHERE book_name = ?"""
        self.cur.execute(sql, [(book_title)])

        data = self.cur.fetchone()

        print(data)
        self.lineEdit_8.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_7.setText(data[3])
        self.comboBox_7.setCurrentText(data[4])
        self.comboBox_8.setCurrentText(data[5])
        self.comboBox_6.setCurrentText(data[6])
        self.lineEdit_6.setText(str(data[7]))

    def edit_books(self):

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        book_title = self.lineEdit_8.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_7.text()
        book_category = self.comboBox_7.currentText()
        book_author = self.comboBox_8.currentText()
        book_publisher = self.comboBox_6.currentText()
        book_price = self.lineEdit_6.text()

        search_book_title = self.lineEdit_5.text()

        self.cur.execute("""UPDATE book SET 
                            book_name=?,
                            book_description=?,
                            book_code=?,
                            book_category=?,
                            book_author=?,
                            book_publisher=?,
                            book_price=? 
                            WHERE book_name = ? """,
                    (book_title,
                     book_description,
                     book_code,
                     book_category,
                     book_author,
                     book_publisher,
                     book_price,
                     search_book_title))

        self.db.commit()
        self.statusBar().showMessage('book updated')
        self.show_all_books()

    def delete_books(self):

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()

        warning = QMessageBox.warning(self, 'Delete Book', "are you sure you want to delete this book",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            sql = """DELETE FROM book WHERE book_name = ?"""
            self.cur.execute(sql, [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

            self.show_all_books

    # #################################################################################################################
    # ############################## Clients ##########################################################################

    def show_all_clients(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT client_name , client_email ,client_nationalid FROM clients""")
        data = self.cur.fetchall()

        print(data)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

        self.db.close()

    def add_new_client(self):
        client_name = self.lineEdit_22.text()
        client_email = self.lineEdit_23.text()
        client_nationalid = self.lineEdit_24.text()

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""INSERT INTO clients(client_name, client_email, client_nationalid) VALUES(?, ?, ?)""",
                         (client_name, client_email, client_nationalid))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('New Client Has Been Added')
        self.show_all_clients()

    def search_client(self):
        client_national_id = self.lineEdit_25.text()

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        sql = """SELECT * FROM clients WHERE client_nationalid = ?"""
        self.cur.execute(sql, [(client_national_id)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_28.setText(data[1])
        self.lineEdit_27.setText(data[2])
        self.lineEdit_26.setText(data[3])

    def edit_client(self):
        client_original_national_id = self.lineEdit_25.text()
        client_name = self.lineEdit_28.text()
        client_email = self.lineEdit_27.text()
        client_national_id = self.lineEdit_26.text()

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""UPDATE clients SET 
                            client_name = ?, 
                            client_email = ?, 
                            client_nationalid = ?
                            WHERE client_nationalid = ?""",
                         (client_name,
                          client_email,
                          client_national_id,
                          client_original_national_id))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('Client Data Has Been Updated ')
        self.show_all_clients()

    def delete_client(self):
        client_original_national_id = self.lineEdit_25.text()

        warning_message = QMessageBox.warning(self, "Delete CLient", "are you sure you want to delete this client",
                                              QMessageBox.Yes | QMessageBox.No)

        if warning_message == QMessageBox.Yes:
            self.db = sqlite3.connect(resource_path("db.db"))
            self.cur = self.db.cursor()

            sql = """DELETE FROM clients WHERE client_nationalid = ?"""
            self.cur.execute(sql, [(client_original_national_id)])

            self.db.commit()
            self.db.close()
            self.statusBar().showMessage('CLient Deleted ')
            self.show_all_clients()

    # #################################################################################################################
    # ############################## Users ############################################################################

    def add_new_user(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        username = self.lineEdit_9.text()
        email = self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        password2 = self.lineEdit_12.text()

        if password == password2:
            self.cur.execute("""INSERT INTO users(user_name, user_email, user_password) VALUES (?, ?, ?)""",
                             (username, email, password))

            self.db.commit()
            self.statusBar().showMessage("New User has been Added")
        else:
            self.label_30.setText("Please Add a Valid Password Twice")

    def login(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        username = self.lineEdit_14.text()
        password = self.lineEdit_13.text()

        sql = """SELECT * FROM users"""

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                print('User Match')
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_4.setEnabled(True)

                self.lineEdit_17.setText(row[1])
                self.lineEdit_15.setText(row[2])
                self.lineEdit_16.setText(row[3])

    def edit_user(self):

        username = self.lineEdit_17.text()
        email = self.lineEdit_15.text()
        password = self.lineEdit_16.text()
        password2 = self.lineEdit_18.text()

        original_name = self.lineEdit_14.text()

        if password == password2:
            self.db = sqlite3.connect(resource_path("db.db"))
            self.cur = self.db.cursor()

            print(username)
            print(email)
            print(password)

            self.cur.execute("""UPDATE users SET 
                                user_name=?, 
                                user_email=?, 
                                user_password=? 
                                WHERE user_name=?""",
                             (username, email, password, original_name))

            self.db.commit()
            self.statusBar().showMessage('User Data Has Been Updated Successfully')

        else:
            print('Make Sure You Entered Your Password Correctly')

    # #################################################################################################################
    # ############################## Settings #########################################################################

    def add_category(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()
        
        category_name = self.lineEdit_19.text()
        
        self.cur.execute("""INSERT INTO category (category_name) VALUES (?)""", (category_name, ))

        self.db.commit()
        self.statusBar().showMessage("New Category Added")
        self.lineEdit_19.setText('')
        self.show_category()
        self.show_category_combobox()

    def show_category(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT category_name FROM category""")
        data= self.cur.fetchall()
        # print(data)

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def add_author(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()

        self.cur.execute("""INSERT INTO authors (author_name) VALUES (?)""", (author_name,))

        self.db.commit()
        self.lineEdit_20.setText('')
        self.statusBar().showMessage("New Author Added")
        self.show_author()
        self.show_author_combobox()

    def show_author(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT author_name FROM authors""")
        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def add_publisher(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()

        self.cur.execute("""INSERT INTO publisher (publisher_name) VALUES (?)""", (publisher_name,))

        self.db.commit()
        self.lineEdit_21.setText('')
        self.statusBar().showMessage("New Publisher Added")
        self.show_publisher()
        self.show_publisher_combobox()

    def show_publisher(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT publisher_name FROM publisher""")
        data = self.cur.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)

    # #################################################################################################################
    # ##############################  show settings data in UI ########################################################

    def show_category_combobox(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT category_name FROM category""")
        data = self.cur.fetchall()
        # print(data)

        self.comboBox_3.clear()

        for category in data:
            # print(category[0])
            self.comboBox_3.addItem(category[0])

    def show_author_combobox(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT author_name FROM authors""")
        data = self.cur.fetchall()

        self.comboBox_4.clear()

        for author in data:
            self.comboBox_4.addItem(author[0])

    def show_publisher_combobox(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT publisher_name FROM publisher""")
        data = self.cur.fetchall()

        self.comboBox_5.clear()

        for publisher in data:
            self.comboBox_5.addItem(publisher[0])

    # #################################################################################################################
    # ############################## Export Data ######################################################################

    def export_day_operations(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT book_name , client , type , date , to_date FROM dayoperations""")

        data = self.cur.fetchall()
        wb = Workbook('day_operations.xlsx')
        sheet1  = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'cliant name')
        sheet1.write(0,2,'type')
        sheet1.write(0,3,'from - date')
        sheet1.write(0,4,'to - date')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')

    def export_books(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT 
                            book_code,
                            book_name,
                            book_description,
                            book_category,
                            book_author,
                            book_publisher,
                            book_price 
                            FROM book""")
        data = self.cur.fetchall()

        wb = Workbook('all_books.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'Book Code')
        sheet1.write(0,1 , 'Book Name')
        sheet1.write(0,2 , 'Book Description')
        sheet1.write(0,3 , 'Book Category')
        sheet1.write(0,4 , 'Book Author')
        sheet1.write(0,5 , 'Book publisher')
        sheet1.write(0,6 , 'Book Price')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Book Report Created Successfully')

    def export_clients(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT 
                            client_name, 
                            client_email,
                            client_nationalid 
                            FROM clients""")
        data = self.cur.fetchall()

        wb = Workbook('all_CLients.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'Client Name')
        sheet1.write(0,1 , 'CLient Email')
        sheet1.write(0,2 , 'CLient NationalID')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('CLients Report Created Successfully')

    # #################################################################################################################
    # ############################## UI Themes ########################################################################

    def dark_blue_theme(self):
        style = open(resource_path('themes/darkblue.css'), 'r')
        style = style.read()
        self.setStyleSheet(style)

    def dark_gray_theme(self):
        style = open(resource_path('themes/darkgray.css'), 'r')
        style = style.read()
        self.setStyleSheet(style)

    def dark_orange_theme(self):
        style = open(resource_path('themes/darkorange.css'), 'r')
        style = style.read()
        self.setStyleSheet(style)

    def qdark_theme(self):
        style = open(resource_path('themes/qdark.css'), 'r')
        style = style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()