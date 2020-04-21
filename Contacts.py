import sys
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import *


Connection = sqlite3.connect('DataBase/Contacts.db')
Cursor = Connection.cursor()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contacts")
        self.setGeometry(450,150,750,600)
        self.UI()
        

    def UI(self):
        
        # Main Design Creator :
        self.MainDesign()
        
        # create layouts for UI :
        self.Layouts()

        self.show()

    def MainDesign(self):
        ### This function just create UI widgets : 

        ########## List Widget ##########
        # List Widget : 
        self.ContactsList = QListWidget()
        
        ########## Buttons ##########
        # New Button :
        self.Btn_New = QPushButton('New')
        self.Btn_New.clicked.connect(self.Func_AddContact)

        # Edit Button :
        self.Btn_Edit = QPushButton('Edit')

        # Remove Button :
        self.Btn_Remove = QPushButton('Remove')

    def Layouts(self):
        # This function creates UI Layouts and setting Widgets to them : 

        ########## Layouts ##########
        # Mail Layout :
        self.MainLayout = QHBoxLayout()
        
        # Left Side Layout :
        self.LeftSideLayout = QFormLayout()

        # Right Side Layout : 
        self.RightMainLayout = QVBoxLayout()

        # Right Side Top Layout :
        self.RightTopLayout = QHBoxLayout()

        # Right side Bottom Layout(for Buttons):
        self.RightBottomLayout = QHBoxLayout()

        ########## Setting Layouts ##########
        # add two right layouts to right layouts :
        self.RightMainLayout.addLayout(self.RightTopLayout)
        self.RightMainLayout.addLayout(self.RightBottomLayout)

        # add Left and Right layouts to Main Layout:
        self.MainLayout.addLayout(self.LeftSideLayout,40)
        self.MainLayout.addLayout(self.RightMainLayout,60)

        ########## Add Widgets to LayOut ##########
        # Right Side : 
        self.RightTopLayout.addWidget(self.ContactsList) 
        self.RightBottomLayout.addWidget(self.Btn_New)
        self.RightBottomLayout.addWidget(self.Btn_Edit)
        self.RightBottomLayout.addWidget(self.Btn_Remove)


        # set Main Layout for our ui :
        self.setLayout(self.MainLayout)

    def Func_AddContact(self):
        # This functoin open a new form to add contacts to DB
        self.Form_AddContact = Class_AddContact()
        self.close()

## Add Contact Class (Contains Form):

class Class_AddContact(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Contact')
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):
        # This function create and design Form widgets
        
        # Create widgets
        self.MainDesign()
        
        # Create layouts and set widgets to them
        self.Layouts()

    def MainDesign(self):
        # create widgets : 
        self.lbl_Title = QLabel('Add Person')
        self.lbl_Title.setStyleSheet('font-size: 24pt;font-family: Arial Bold;color: rgb(128,0,64);')
        self.lbl_Title.setAlignment(Qt.AlignCenter)
        
        self.lbl_Image = QLabel()
        self.lbl_Image.setPixmap(QPixmap('icons/Man_Default.png'))
        self.lbl_Image.setAlignment(Qt.AlignCenter) 
        

    def Layouts(self):

        ########## Layouts #########
        # main Layout 
        self.MainLayout = QVBoxLayout()

        # Top Layout
        self.TopLayout = QVBoxLayout()

        # Bottom Layout 
        self.BottomLayout = QFormLayout()

        ########## Setting Layouts ##########
        # Add Top and Bottom layputs to main layout
        self.MainLayout.addLayout(self.TopLayout)
        self.MainLayout.addLayout(self.BottomLayout)

        ########## Setting Widgets to Layouts ##########
        self.TopLayout.addStretch()
        self.TopLayout.addWidget(self.lbl_Title)
        self.TopLayout.addWidget(self.lbl_Image)
        self.TopLayout.addStretch()

        # set main layout for this form (Add Contacts)
        self.setLayout(self.MainLayout)


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()