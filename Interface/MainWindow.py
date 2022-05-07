import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from Ui_MainWindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.PListAccounts)

        self.ui.moneyTransfer.clicked.connect(self.showMoneyTransfer)
        self.ui.deposit.clicked.connect(self.showDeposit)
        self.ui.withdraw.clicked.connect(self.showWithdraw)  
        self.ui.listAccounts.clicked.connect(self.showListAccounts)
        self.ui.newAccount.clicked.connect(self.showCreateAccount)
        self.ui.deleteAccount.clicked.connect(self.showDeleteAccount) 

    def show(self):
        self.main_win.show()

    def showMoneyTransfer(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PMoneyTransfer)

    def showDeposit(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PDeposit)

    def showWithdraw(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PWithdraw)

    def showListAccounts(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PListAccounts)

    def showCreateAccount(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PCreateAccount)

    def showDeleteAccount(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PDeleteAccount)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())