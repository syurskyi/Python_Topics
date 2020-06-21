"""
@author: Abdelmoula Khdodui
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

from time import sleep
import sys, os

from os import path

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(resource_path("main.ui"))

import sqlite3


class Main(QMainWindow, FORM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.Handel_Buttons()
        self.NAVIGATE()
        
        
    def Handel_Buttons(self):
        self.refresh_btn.clicked.connect(self.GET_DATA)
        self.search_btn.clicked.connect(self.SEARCH)
        self.check_btn.clicked.connect(self.LEVEL)
        self.update_btn.clicked.connect(self.UPDATE)
        self.delete_btn.clicked.connect(self.DELETE)
        self.add_btn.clicked.connect(self.ADD)
        self.last_btn.clicked.connect(self.LAST)
    
    
    def GET_DATA(self):
        
        # Connect to Sqlite3 database ad fill GUI table with data.
        db=sqlite3.connect(resource_path("parts.db"))
        cursor=db.cursor()
        
        command=''' SELECT * from parts_table '''
        
        result=cursor.execute(command)
        
        self.table.setRowCount(0) 
        
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        
        # Display references number and type number in Statistics tab
        
        cursor2=db.cursor()
        cursor3=db.cursor()
        
        parts_nbr= ''' SELECT COUNT (DISTINCT PartName) from parts_table '''
        ref_nbr= ''' SELECT COUNT (DISTINCT Reference) from parts_table '''
        
        result_ref_nbr=cursor2.execute(ref_nbr)
        result_parts_nbr=cursor3.execute(parts_nbr)
        
        self.lbl_ref_nbr.setText(str(result_ref_nbr.fetchone()[0]))
        self.lbl_parts_nbr.setText(str(result_parts_nbr.fetchone()[0]))        
        
        # Display 4 results: Min, Max Nbr of holes in addition to their respective reference names
        
        cursor4=db.cursor()
        cursor5=db.cursor()
        
        min_hole=''' SELECT MIN(NumberOfHoles), Reference from parts_table '''
        max_hole=''' SELECT MAX(NumberOfHoles), Reference from parts_table '''        
        
        result_min_hole=cursor4.execute(min_hole)
        result_max_hole=cursor5.execute(max_hole)
        
        r1=result_min_hole.fetchone()
        r2=result_max_hole.fetchone()
        
        # Print Results in QLabels
        
        self.lbl_min_hole.setText(str(r1[0]))
        self.lbl_max_hole.setText(str(r2[0]))
        
        self.lbl_min_hole_2.setText(str(r1[1]))
        self.lbl_max_hole_2.setText(str(r2[1]))
        
        if int(self.lbl_ref_nbr.text())<15:
            
            self.lbl_ref_nbr.setStyleSheet(""" QWidget {
                    background-color: rgb(255, 0, 0);
                    color: rgb(255, 255, 255);
                    }""")
        
    def SEARCH(self):

        db=sqlite3.connect("parts.db")
        cursor=db.cursor()
        
        nbr=int(self.count_filter_txt.text())
        
        command=''' SELECT * from parts_table WHERE count<=?'''
        
        result=cursor.execute(command,[nbr])
        
        self.table.setRowCount(0) 
        
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))        
        
    def LEVEL(self):
            
        db=sqlite3.connect("parts.db")
        cursor=db.cursor()
        
        command=''' SELECT Reference, PartName, Count from parts_table order by Count asc LIMIT 3 '''
        
        result=cursor.execute(command)
        
        self.table2.setRowCount(0) 
        
        for row_number, row_data in enumerate(result):
            self.table2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table2.setItem(row_number, column_number, QTableWidgetItem(str(data)))           

    def NAVIGATE(self):

        db=sqlite3.connect("parts.db")
        cursor=db.cursor()
        
        command=''' SELECT * from  parts_table'''
        
        result=cursor.execute(command)
        val=result.fetchone()
        
        self.id.setText(str(val[0]))
        self.reference.setText(str(val[1]))
        self.part_name.setText(str(val[2]))
        self.min_area.setText(str(val[3]))
        self.max_area.setText(str(val[4]))
        self.number_of_holes.setText(str(val[5]))
        self.min_diameter.setText(str(val[6]))
        self.max_diameter.setText(str(val[7]))
        self.count.setValue(val[8])
      
    def UPDATE(self):

        db=sqlite3.connect("parts.db")
        cursor=db.cursor()
        
        id_=int(self.id.text())
        reference_=self.reference.text()
        part_name_=self.part_name.text()
        min_area_=self.min_area.text()
        max_area_=self.max_area.text()
        number_of_holes_=self.number_of_holes.text()
        min_diameter_=self.min_diameter.text()
        max_diameter_=self.max_diameter.text()
        count_=str(self.count.value())
        
        row=(reference_,part_name_,min_area_,max_area_,number_of_holes_,min_diameter_,max_diameter_,count_,id_)
        
        command=''' UPDATE parts_table SET Reference=?,PartName=?,MinArea=?,MaxArea=?,NumberOfHoles=?,MinDiameter=?,MaxDiameter=?,Count=? WHERE ID=?'''
                
        cursor.execute(command,row)
        
        db.commit()

    def DELETE(self):

        db=sqlite3.connect("parts.db")
        cursor=db.cursor()
        
        d=self.id.text()
        
        command= ''' DELETE FROM parts_table WHERE  ID=? '''
        
        cursor.execute(command,d)
        
        db.commit()
        
    def ADD(self):

        db=sqlite3.connect("parts.db")
        cursor=db.cursor()
        
        reference_=self.reference.text()
        part_name_=self.part_name.text()
        min_area_=self.min_area.text()
        max_area_=self.max_area.text()
        number_of_holes_=self.number_of_holes.text()
        min_diameter_=self.min_diameter.text()
        max_diameter_=self.max_diameter.text()
        count_=str(self.count.value())
        
        row=(reference_,part_name_,min_area_,max_area_,number_of_holes_,min_diameter_,max_diameter_,count_)
        
        command=''' INSERT INTO parts_table (Reference,PartName,MinArea,MaxArea,NumberOfHoles,MinDiameter,MaxDiameter,Count) VALUES (?,?,?,?,?,?,?,?)'''
                
        cursor.execute(command,row)
        
        db.commit()        
        
        
    def LAST(self):

        db=sqlite3.connect("parts.db")
        cursor=db.cursor()
        
        command=''' SELECT * from  parts_table'''
        
        result=cursor.execute(command)
        '''
        val=result.fetchone()
        print (result.rowcount)
        '''
        for row in result:
            sleep(2)
            #val=result.fetchone()
            self.id.setText(str(row[0]))
            self.reference.setText(str(row[1]))
            self.part_name.setText(str(row[2]))
            self.min_area.setText(str(row[3]))
            self.max_area.setText(str(row[4]))
            self.number_of_holes.setText(str(row[5]))
            self.min_diameter.setText(str(row[6]))
            self.max_diameter.setText(str(row[7]))
            self.count.setValue(row[8])
        
        
        
def main():
    
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()
    

if __name__=='__main__':
    main()    
