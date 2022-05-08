import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from managerMain import Ui_ManagerWindow
from customerMain import Ui_CustomerWindow
from homeMain import Ui_MainWindow


class CustomerWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_CustomerWindow()
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


class ManagerWindow:
    def __init__(self):
        self.main_window = QMainWindow()
        self.ui = Ui_ManagerWindow()
        self.ui.setupUi(self.main_window)

        self.ui.stackedWidget.setCurrentWidget(self.ui.main_widget)

        self.ui.addNewCurrency.clicked.connect(self.showAddNewCurrency)
        self.ui.updateCurrency.clicked.connect(self.showUpdateCurrency)
        self.ui.update_clerk.clicked.connect(self.showUpdate_clerk)
        self.ui.update_interest.clicked.connect(self.showUpdate_interest)
        self.ui.add_customer.clicked.connect(self.showAdd_customer)
        self.ui.view_transactions.clicked.connect(self.showView_transactions)

    def show(self):
        self.main_window.show()

    def showAddNewCurrency(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.add_currency_widget)

    def showUpdateCurrency(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.update_currency_widget)

    def showUpdate_clerk(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.update_clerk_widget)

    def showUpdate_interest(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.update_interest_widget)

    def showAdd_customer(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.add_customer_widget)

    def showView_transactions(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.view_transactions_widget)


class MainWindow:
    def __init__(self):
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.ui.cutomer_btn.clicked.connect(self.customer_clicked)
        self.ui.clerk_btn.clicked.connect(self.clerk_clicked)
        self.ui.manager_btn.clicked.connect(self.manager_clicked)

    def show(self):
        self.main_window.show()

    def hide(self):
        self.main_window.hide()

    def customer_clicked(self):
        cus_id = self.ui.customer_id_value.text()
        print(cus_id)
        main_win.hide()
        customer_win.show()

    def clerk_clicked(self):
        ck_id = self.ui.clerk_id_value.text()
        print(ck_id)
        # main_win.hide()
        # clerk_window.show()

    def manager_clicked(self):
        ck_id = self.ui.clerk_id_value.text()
        print(ck_id)
        main_win.hide()
        manager_window.show()


app = QApplication(sys.argv)
main_win = MainWindow()
customer_win = CustomerWindow()
manager_window = ManagerWindow()
main_win.show()
sys.exit(app.exec_())


# type = input("1-Customer\n2-Manager\n3-Clerk")
# if type == '1':
#     app = QApplication(sys.argv)
#     main_win = CustomerWindow()
#     main_win.show()
#     sys.exit(app.exec_())


# if type == '2':
#     app = QApplication(sys.argv)
#     main_window = ManagerWindow()
#     main_window.show()
#     sys.exit(app.exec_())
