____ ?.?W.. _____ *
____ ?.QtGui _____ QPixmap,QFont
_____ ___,os
_____ sqlite3
____ PIL _____ Image


con = sqlite3.c..('employees.db')
cur = con.cursor()
defaultImg="person.png"
person_id=None
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
        employeeList=QListWidget()
        employeeList.itemClicked.c..(singleClick)
        btnNew=?PB..("New")
        btnNew.clicked.c..(addEmployee)
        btnUpdate=?PB..("Update")
        btnUpdate.clicked.c..(updateEmployee)
        btnDelete=?PB..("Delete")
        btnDelete.clicked.c..(deleteEmployee)

    ___ layouts 
        ###################Layouts###############
        mainLayout=QHBoxLayout()
        leftLayout=QFormLayout()
        rightMainLayout=QVBoxLayout()
        rightTopLayout=QHBoxLayout()
        rightBottomLayout=QHBoxLayout()
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
        newEmployee=AddEmployee()
        close()
    ___ getEmployees 
        query="SELECT id,name,surname FROM employees"
        employees=cur.execute(query).fetchall()
        for employee in employees:
            employeeList.addItem(st.(employee[0])+"-"+employee[1]+" "+employee[2] )

    ___ displayFirstRecord 
        query="SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee=cur.execute(query).fetchone()
        img=QLabel()
        img.setPixmap(QPixmap("images/"+employee[5]))
        name=QLabel(employee[1])
        surname=QLabel(employee[2])
        phone=QLabel(employee[3])
        email=QLabel(employee[4])
        address=QLabel(employee[6])
        leftLayout.setVerticalSpacing(20)
        leftLayout.addRow("",img)
        leftLayout.addRow("Name: ",name)
        leftLayout.addRow("Surname :",surname)
        leftLayout.addRow("Phone :",phone)
        leftLayout.addRow("Email :",email)
        leftLayout.addRow("Address:",address)

    ___ singleClick 
        for i in reversed(range(leftLayout.count())):
            widget=leftLayout.takeAt(i).widget()

            __ widget is not None:
                widget.deleteLater()

        employee=employeeList.currentItem().text()
        id=employee.split("-")[0]
        query=("SELECT * FROM employees WHERE id=?")
        person=cur.execute(query,(id,)).fetchone()#single item tuple=(1,)
        img = QLabel()
        img.setPixmap(QPixmap("images/" + person[5]))
        name = QLabel(person[1])
        surname = QLabel(person[2])
        phone = QLabel(person[3])
        email = QLabel(person[4])
        address = QLabel(person[6])
        leftLayout.setVerticalSpacing(20)
        leftLayout.addRow("", img)
        leftLayout.addRow("Name: ", name)
        leftLayout.addRow("Surname :", surname)
        leftLayout.addRow("Phone :", phone)
        leftLayout.addRow("Email :", email)
        leftLayout.addRow("Address:", address)

    ___ deleteEmployee 
        __ employeeList.selectedItems(
            person=employeeList.currentItem().text()
            id = person.split("-")[0]
            mbox=QMessageBox.question ,"Warning","Are you sure to delete this person?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            __ mbox __ QMessageBox.Yes:
                try:
                    query="DELETE FROM employees WHERE id=?"
                    cur.execute(query,(id,))
                    con.commit()
                    QMessageBox.information ,"Info!!!","Person has been deleted")
                    close()
                    main=Main()

                except:
                    QMessageBox.information ,"Warning!!!","Person has not been deleted")


        else:
            QMessageBox.information , "Warning!!!", "Please select a person to delete")

    ___ updateEmployee 
        global person_id
        __ employeeList.selectedItems(
            person = employeeList.currentItem().text()
            person_id=person.split("-")[0]
            updateWindow=UpdateEmployee()
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
        main = Main()

    ___ getPerson 
        global person_id
        query="SELECT * FROM employees WHERE id=?"
        employee=cur.execute(query,(person_id,)).fetchone()
        print(employee)
        name=employee[1]
        surname=employee[2]
        phone=employee[3]
        email=employee[4]
        image=employee[5]
        address=employee[6]

    ___ mainDesign 
        ################Top Layout widgets#######################
        setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        title = QLabel("Update Person")
        title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        imgAdd = QLabel()
        imgAdd.setPixmap(QPixmap("images/{}".format(image)))
        ###################Bottom Layout Widgets#####################
        nameLbl = QLabel("Name :")
        nameEntry = QLineEdit()
        nameEntry.sT..(name)
        surnameLbl = QLabel("Surname :")
        surnameEntry = QLineEdit()
        surnameEntry.sT..(surname)
        phoneLbl = QLabel("Phone :")
        phoneEntry = QLineEdit()
        phoneEntry.sT..(phone)
        emailLbl = QLabel("Email :")
        emailEntry = QLineEdit()
        emailEntry.sT..(email)
        imgLbl = QLabel("Picture: ")
        imgButton = ?PB..("Browse")
        imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        imgButton.clicked.c..(uploadImage)
        addressLbl = QLabel("Address: ")
        addressEditor = QTextEdit()
        addressEditor.sT..(address)
        addButton = ?PB..("Update")
        addButton.setStyleSheet("background-color:orange;font-size:10pt")
        addButton.clicked.c..(updateEmployee)

    ___ layouts 
        ##################creating main layouts##########
        mainLayout = QVBoxLayout()
        topLayout = QVBoxLayout()
        bottomLayout = QFormLayout()

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
        size =(128,128)
        fileName,ok =QFileDialog.getOpenFileName ,'Upload Image','','Image Files (*.jpg *.png)')

        __ ok:

            defaultImg=os.path.basename(fileName)
            img=Image.open(fileName)
            img=img.resize(size)
            img.save("images/{}".format(defaultImg))



    ___ updateEmployee 
        global defaultImg
        global person_id
        name=nameEntry.text()
        surname=surnameEntry.text()
        phone=phoneEntry.text()
        email=emailEntry.text()
        img=defaultImg
        address=addressEditor.toPlainText()
        __ (name and surname and phone !=""
            try:
                query="UPDATE employees set name =?, surname=?, phone=?,email=?,img=?,address=? WHERE id=?"
                cur.execute(query,(name,surname,phone,email,img,address,person_id))
                con.commit()
                QMessageBox.information ,"Success","Person has been updated")
                close()
                main=Main()
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
        main=Main()

    ___ mainDesign 
        ################Top Layout widgets#######################
        setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        title=QLabel("Add Person")
        title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        imgAdd=QLabel()
        imgAdd.setPixmap(QPixmap("icons/person.png"))
        ###################Bottom Layout Widgets#####################
        nameLbl=QLabel("Name :")
        nameEntry=QLineEdit()
        nameEntry.setPlaceholderText("Enter Employee Name")
        surnameLbl = QLabel("Surname :")
        surnameEntry = QLineEdit()
        surnameEntry.setPlaceholderText("Enter Employee Surname")
        phoneLbl = QLabel("Phone :")
        phoneEntry = QLineEdit()
        phoneEntry.setPlaceholderText("Enter Employee Phone Number")
        emailLbl = QLabel("Email :")
        emailEntry = QLineEdit()
        emailEntry.setPlaceholderText("Enter Employee Email")
        imgLbl=QLabel("Picture: ")
        imgButton=?PB..("Browse")
        imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        imgButton.clicked.c..(uploadImage)
        addressLbl=QLabel("Address: ")
        addressEditor=QTextEdit()
        addButton=?PB..("Add")
        addButton.setStyleSheet("background-color:orange;font-size:10pt")
        addButton.clicked.c..(addEmployee)

    ___ layouts 
        ##################creating main layouts##########
        mainLayout=QVBoxLayout()
        topLayout=QVBoxLayout()
        bottomLayout=QFormLayout()

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
        size =(128,128)
        fileName,ok =QFileDialog.getOpenFileName ,'Upload Image','','Image Files (*.jpg *.png)')

        __ ok:

            defaultImg=os.path.basename(fileName)
            img=Image.open(fileName)
            img=img.resize(size)
            img.save("images/{}".format(defaultImg))



    ___ addEmployee 
        global defaultImg
        name=nameEntry.text()
        surname=surnameEntry.text()
        phone=phoneEntry.text()
        email=emailEntry.text()
        img=defaultImg
        address=addressEditor.toPlainText()
        __ (name and surname and phone !=""
            try:
                query="INSERT INTO employees (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query,(name,surname,phone,email,img,address))
                con.commit()
                QMessageBox.information ,"Success","Person has been added")
                close()
                main=Main()
            except:
                QMessageBox.information , "Warning", "Person has not been added")

        else:
            QMessageBox.information , "Warning", "Fields can not be empty")



___ main(
    APP=?A..(___.argv)
    window=Main()
    ___.e..(APP.exec_())
__ __name__ __ '__main__':
    main()