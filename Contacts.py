import sys
from PyQt5.QtWidgets import *
import sqlite3

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

def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()