____ ?.?W.. _____ *
____ ?.QtGui _____ QPixmap,QFont
_____ ___,os
_____ sqlite3
____ PIL _____ Image


con _ sqlite3.c..('employees.db')
cur _ con.cursor()
defaultImg_"person.png"
person_id_None
c_ Main(?W..
    ___  -  
        s__. - ()
        setWindowTitle("My Employees")
        setGeometry(450,150,750,600)
        UI()
        s..


    ___ UI 
        mainDesign()
        layouts()
        getEmployees()
        displayFirstRecord()

    ___ mainDesign 
        setStyleSheet("font-size:14pt;font-family:Arial Bold;")
        employeeList_QListWidget()
        employeeList.itemClicked.c..(singleClick)
        btnNew_?PB..("New")
        btnNew.c___.c..(addEmployee)
        btnUpdate_?PB..("Update")
        btnUpdate.c___.c..(updateEmployee)
        btnDelete_?PB..("Delete")
        btnDelete.c___.c..(deleteEmployee)

    ___ layouts 
        ###################Layouts###############
        mainLayout_QHBoxLayout()
        leftLayout_QFormLayout()
        rightMainLayout_QVBoxLayout()
        rightTopLayout_QHBoxLayout()
        rightBottomLayout_QHBoxLayout()
        #####################Adding child layouts to main layout###########
        rightMainLayout.addLayout(rightTopLayout)
        rightMainLayout.addLayout(rightBottomLayout)
        mainLayout.addLayout(leftLayout,40)
        mainLayout.addLayout(rightMainLayout,60)
        ###################adding wigdets to layouts#################
        rightTopLayout.addWidget(employeeList)
        rightBottomLayout.addWidget(btnNew)
        rightBottomLayout.addWidget(btnUpdate)
        rightBottomLayout.addWidget(btnDelete)
        ##############setting main window layout#####################
        setLayout(mainLayout)

    ___ addEmployee 
        newEmployee_AddEmployee()
        close()
    ___ getEmployees 
        query_"SELECT id,name,surname FROM employees"
        employees_cur.execute(query).fetchall()
        for employee in employees:
            employeeList.addItem(st.(employee[0])+"-"+employee[1]+" "+employee[2] )

    ___ displayFirstRecord 
        query_"SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee_cur.execute(query).fetchone()
        img_QLabel()
        img.setPixmap(QPixmap("images/"+employee[5]))
        name_QLabel(employee[1])
        surname_QLabel(employee[2])
        phone_QLabel(employee[3])
        email_QLabel(employee[4])
        address_QLabel(employee[6])
        leftLayout.setVerticalSpacing(20)
        leftLayout.addRow("",img)
        leftLayout.addRow("Name: ",name)
        leftLayout.addRow("Surname :",surname)
        leftLayout.addRow("Phone :",phone)
        leftLayout.addRow("Email :",email)
        leftLayout.addRow("Address:",address)

    ___ singleClick 
        for i in reversed(range(leftLayout.count())):
            widget_leftLayout.takeAt(i).widget()

            __ widget is not None:
                widget.deleteLater()

        employee_employeeList.currentItem().t..()
        id_employee.split("-")[0]
        query_("SELECT * FROM employees WHERE id=?")
        person_cur.execute(query,(id,)).fetchone()#single item tuple=(1,)
        img _ QLabel()
        img.setPixmap(QPixmap("images/" + person[5]))
        name _ QLabel(person[1])
        surname _ QLabel(person[2])
        phone _ QLabel(person[3])
        email _ QLabel(person[4])
        address _ QLabel(person[6])
        leftLayout.setVerticalSpacing(20)
        leftLayout.addRow("", img)
        leftLayout.addRow("Name: ", name)
        leftLayout.addRow("Surname :", surname)
        leftLayout.addRow("Phone :", phone)
        leftLayout.addRow("Email :", email)
        leftLayout.addRow("Address:", address)

    ___ deleteEmployee 
        __ employeeList.selectedItems(
            person_employeeList.currentItem().t..()
            id _ person.split("-")[0]
            mbox_QMessageBox.question ,"Warning","Are you sure to delete this person?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            __ mbox __ QMessageBox.Yes:
                try:
                    query_"DELETE FROM employees WHERE id=?"
                    cur.execute(query,(id,))
                    con.commit()
                    QMessageBox.information ,"Info!!!","Person has been deleted")
                    close()
                    main_Main()

                except:
                    QMessageBox.information ,"Warning!!!","Person has not been deleted")


        else:
            QMessageBox.information , "Warning!!!", "Please select a person to delete")

    ___ updateEmployee 
        global person_id
        __ employeeList.selectedItems(
            person _ employeeList.currentItem().t..()
            person_id_person.split("-")[0]
            updateWindow_UpdateEmployee()
            close()

        else:
            QMessageBox.information , "Warning!!!", "Please select a person to update")



c_ UpdateEmployee(?W..
    ___  -  
        s__. - ()
        setWindowTitle("Update Employee")
        setGeometry(450,150,350,600)
        UI()
        s..

    ___ UI 

        getPerson()
        mainDesign()
        layouts()

    ___ closeEvent , event
        main _ Main()

    ___ getPerson 
        global person_id
        query_"SELECT * FROM employees WHERE id=?"
        employee_cur.execute(query,(person_id,)).fetchone()
        print(employee)
        name_employee[1]
        surname_employee[2]
        phone_employee[3]
        email_employee[4]
        image_employee[5]
        address_employee[6]

    ___ mainDesign 
        ################Top Layout widgets#######################
        setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        title _ QLabel("Update Person")
        title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        imgAdd _ QLabel()
        imgAdd.setPixmap(QPixmap("images/{}".format(image)))
        ###################Bottom Layout Widgets#####################
        nameLbl _ QLabel("Name :")
        nameEntry _ QLineEdit()
        nameEntry.sT..(name)
        surnameLbl _ QLabel("Surname :")
        surnameEntry _ QLineEdit()
        surnameEntry.sT..(surname)
        phoneLbl _ QLabel("Phone :")
        phoneEntry _ QLineEdit()
        phoneEntry.sT..(phone)
        emailLbl _ QLabel("Email :")
        emailEntry _ QLineEdit()
        emailEntry.sT..(email)
        imgLbl _ QLabel("Picture: ")
        imgButton _ ?PB..("Browse")
        imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        imgButton.c___.c..(uploadImage)
        addressLbl _ QLabel("Address: ")
        addressEditor _ QTextEdit()
        addressEditor.sT..(address)
        addButton _ ?PB..("Update")
        addButton.setStyleSheet("background-color:orange;font-size:10pt")
        addButton.c___.c..(updateEmployee)

    ___ layouts 
        ##################creating main layouts##########
        mainLayout _ QVBoxLayout()
        topLayout _ QVBoxLayout()
        bottomLayout _ QFormLayout()

        ##########adding child layouts to main layout##############
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        ##################adding wigdets to layouts##############
        ##############top layout################
        topLayout.addStretch()
        topLayout.addWidget(title)
        topLayout.addWidget(imgAdd)
        topLayout.addStretch()
        topLayout.setContentsMargins(110, 20, 10, 30)  # left,top,right,bottom
        ###########bottom layout#################
        bottomLayout.addRow(nameLbl, nameEntry)
        bottomLayout.addRow(surnameLbl, surnameEntry)
        bottomLayout.addRow(phoneLbl, phoneEntry)
        bottomLayout.addRow(emailLbl, emailEntry)
        bottomLayout.addRow(imgLbl, imgButton)
        bottomLayout.addRow(addressLbl, addressEditor)
        bottomLayout.addRow("", addButton)

        ###########setting main layout for window##################
        setLayout(mainLayout)


    ___ uploadImage 
        global defaultImg
        size _(128,128)
        fileName,ok _QFileDialog.getOpenFileName ,'Upload Image','','Image Files (*.jpg *.png)')

        __ ok:

            defaultImg_os.path.basename(fileName)
            img_Image.open(fileName)
            img_img.resize(size)
            img.save("images/{}".format(defaultImg))



    ___ updateEmployee 
        global defaultImg
        global person_id
        name_nameEntry.t..()
        surname_surnameEntry.t..()
        phone_phoneEntry.t..()
        email_emailEntry.t..()
        img_defaultImg
        address_addressEditor.toPlainText()
        __ (name and surname and phone !_""
            try:
                query_"UPDATE employees set name =?, surname=?, phone=?,email=?,img=?,address=? WHERE id=?"
                cur.execute(query,(name,surname,phone,email,img,address,person_id))
                con.commit()
                QMessageBox.information ,"Success","Person has been updated")
                close()
                main_Main()
            except:
                QMessageBox.information , "Warning", "Person has not been updated")

        else:
            QMessageBox.information , "Warning", "Fields can not be empty")



c_ AddEmployee(?W..
    ___  -  
        s__. - ()
        setWindowTitle("Add Employees")
        setGeometry(450,150,350,600)
        UI()
        s..

    ___ UI 
        mainDesign()
        layouts()

    ___ closeEvent , event
        main_Main()

    ___ mainDesign 
        ################Top Layout widgets#######################
        setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        title_QLabel("Add Person")
        title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        imgAdd_QLabel()
        imgAdd.setPixmap(QPixmap("icons/person.png"))
        ###################Bottom Layout Widgets#####################
        nameLbl_QLabel("Name :")
        nameEntry_QLineEdit()
        nameEntry.setPlaceholderText("Enter Employee Name")
        surnameLbl _ QLabel("Surname :")
        surnameEntry _ QLineEdit()
        surnameEntry.setPlaceholderText("Enter Employee Surname")
        phoneLbl _ QLabel("Phone :")
        phoneEntry _ QLineEdit()
        phoneEntry.setPlaceholderText("Enter Employee Phone Number")
        emailLbl _ QLabel("Email :")
        emailEntry _ QLineEdit()
        emailEntry.setPlaceholderText("Enter Employee Email")
        imgLbl_QLabel("Picture: ")
        imgButton_?PB..("Browse")
        imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        imgButton.c___.c..(uploadImage)
        addressLbl_QLabel("Address: ")
        addressEditor_QTextEdit()
        addButton_?PB..("Add")
        addButton.setStyleSheet("background-color:orange;font-size:10pt")
        addButton.c___.c..(addEmployee)

    ___ layouts 
        ##################creating main layouts##########
        mainLayout_QVBoxLayout()
        topLayout_QVBoxLayout()
        bottomLayout_QFormLayout()

        ##########adding child layouts to main layout##############
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        ##################adding wigdets to layouts##############
                ##############top layout################
        topLayout.addStretch()
        topLayout.addWidget(title)
        topLayout.addWidget(imgAdd)
        topLayout.addStretch()
        topLayout.setContentsMargins(110,20,10,30) #left,top,right,bottom
                ###########bottom layout#################
        bottomLayout.addRow(nameLbl,nameEntry)
        bottomLayout.addRow(surnameLbl,surnameEntry)
        bottomLayout.addRow(phoneLbl,phoneEntry)
        bottomLayout.addRow(emailLbl,emailEntry)
        bottomLayout.addRow(imgLbl,imgButton)
        bottomLayout.addRow(addressLbl,addressEditor)
        bottomLayout.addRow("",addButton)

        ###########setting main layout for window##################
        setLayout(mainLayout)

    ___ uploadImage 
        global defaultImg
        size _(128,128)
        fileName,ok _QFileDialog.getOpenFileName ,'Upload Image','','Image Files (*.jpg *.png)')

        __ ok:

            defaultImg_os.path.basename(fileName)
            img_Image.open(fileName)
            img_img.resize(size)
            img.save("images/{}".format(defaultImg))



    ___ addEmployee 
        global defaultImg
        name_nameEntry.t..()
        surname_surnameEntry.t..()
        phone_phoneEntry.t..()
        email_emailEntry.t..()
        img_defaultImg
        address_addressEditor.toPlainText()
        __ (name and surname and phone !_""
            try:
                query_"INSERT INTO employees (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query,(name,surname,phone,email,img,address))
                con.commit()
                QMessageBox.information ,"Success","Person has been added")
                close()
                main_Main()
            except:
                QMessageBox.information , "Warning", "Person has not been added")

        else:
            QMessageBox.information , "Warning", "Fields can not be empty")



___ main(
    APP_?A..(___.argv)
    window_Main()
    ___.e..(APP.e
__ __name__ __ '__main__':
    main()