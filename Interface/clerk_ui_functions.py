
from audioop import add
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from matplotlib.widgets import Widget
from SQLconnection import cursor, connection

from ui_clerk import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.row = 0
        self.customerID = 312

        self.displayCustomers()
        self.ui.addCustomer_button.clicked.connect(self.addCustomer)
        self.ui.deleteCustomer_button.clicked.connect(self.deleteCustomer)
        
    def show(self):
        self.main_win.show()

    def displayCustomers(self):
        self.ui.MC_table.setRowCount(50)
        
        cursor.execute('SELECT * FROM customer')

        for i in cursor:
            self.ui.MC_table.setItem(self.row, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            for col in range(1,8):
                self.ui.MC_table.setItem(self.row, col, QtWidgets.QTableWidgetItem(i[col]))
            self.row += 1

    def addCustomer(self):
        firstName = self.ui.firstName_textEdit.toPlainText()
        lastName = self.ui.lastName_textEdit.toPlainText()
        phoneNum = self.ui.phoneNum_textEdit.toPlainText()
        email = self.ui.email_textEdit.toPlainText()
        TC = self.ui.TC_textEdit.toPlainText()
        address = self.ui.address_textEdit.toPlainText()
        self.customerID += 1
        newCustomer = (str(self.customerID),firstName,lastName,email, phoneNum, TC, address)

        for i in range(0,7):
            self.ui.MC_table.setItem(self.row, i, QtWidgets.QTableWidgetItem(newCustomer[i]))

        self.row += 1

    def deleteCustomer(self):
        deletedRow = ['','','','','','','']
        cus_toBeDeleted = int(self.ui.MC_table.item(self.ui.MC_table.currentRow(),0).text())
        print(cus_toBeDeleted)
        self.ui.MC_table.removeRow(self.ui.MC_table.currentRow())
        self.ui.MC_table.setRowCount(50)
        cursor.execute(f''' DELETE customer
                        FROM customer c
                        WHERE c.id = {cus_toBeDeleted}''')
        #for i in range(0,7):
        #    self.ui.MC_table.setItem(self.ui.MC_table.currentRow(), i, QtWidgets.QTableWidgetItem(deletedRow[i]))
        self.row -= 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


