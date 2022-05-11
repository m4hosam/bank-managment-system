import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from SQLconnection import cursor, connection

from managerMain import Ui_ManagerWindow
from customerMain import Ui_CustomerWindow
from homeMain import Ui_MainWindow

from classes import Account, Customer, searchAccountIDs


def check_user_input(input, type):
    try:
        u_id = int(input)
        if(type == "customer"):
            cursor.execute(
                'SELECT * FROM customer2 WHERE customer2.id = ?', u_id)
            row = cursor.fetchone()
            if(not row):
                msg.setText("Customer Not Found")
                x = msg.exec_()
                return "Customer Not Found"
            else:
                return u_id

        elif(type == "clerk"):
            cursor.execute(
                'SELECT * FROM customerClerks2 WHERE customerClerks2.clerk_id = ?', u_id)
            row = cursor.fetchone()
            if(not row):
                msg.setText("Clerk not Found")
                x = msg.exec_()
                return "Clerk not Found"
            else:
                return u_id
    except ValueError:
        msg.setText("Invalid input")
        x = msg.exec_()
        return "invalid"


class CustomerWindow:
    cus_id = 0

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_CustomerWindow()
        self.ui.setupUi(self.main_win)
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PListAccounts)

        self.ui.listAccounts_radio.clicked.connect(self.showListAccounts)
        self.ui.moneyTransfer_radio.clicked.connect(self.showMoneyTransfer)
        self.ui.withdraw_radio.clicked.connect(self.showWithdraw)
        self.ui.deposit_radio.clicked.connect(self.showDeposit)
        self.ui.newAccount_radio.clicked.connect(self.showCreateAccount)
        self.ui.deleteAccount_radio.clicked.connect(self.showDeleteAccount)
        self.ui.editInfo_radio.clicked.connect(self.showEditInfo)
        self.ui.monthlySummary_radio.clicked.connect(self.showMonthlySummery)

        self.ui.deposit_btn.clicked.connect(self.deposit)
        self.ui.withdraw_btn.clicked.connect(self.withdraw)
        self.ui.tranfer_btn.clicked.connect(self.money_transfer)

    def show(self):
        self.display_customer_info()
        self.display_accounts()
        self.main_win.show()

    def showMoneyTransfer(self):
        # print("customer2222: " + str(self.cus_id))
        self.display_moneyTransfer()
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PMoneyTransfer)

    def showDeposit(self):
        # print("customer3333: " + str(self.cus_id))
        self.display_deposit()
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PDeposit)
        print("deposit k85")
        # self.ui.deposit_btn.clicked.connect(self.deposit)

    def showWithdraw(self):
        # print("customer44444: " + str(self.cus_id))
        self.display_withdraw()
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PWithdraw)
        print("withdraw k95")
        # self.ui.withdraw_btn.clicked.connect(self.withdraw)

    def showListAccounts(self):
        # print("customer5555: " + str(self.cus_id))
        self.display_accounts()
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PListAccounts)

    def showCreateAccount(self):
        # print("customer6666: " + str(self.cus_id))
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PCreateAccount)

    def showDeleteAccount(self):
        # print("customer77777: " + str(self.cus_id))
        self.display_delete()
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PDeleteAccount)

    def showEditInfo(self):
        # print("customer8888: " + str(self.cus_id))
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.Pedit_info)

    def showMonthlySummery(self):
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PMonthlySummary)

    def display_customer_info(self):
        currentCustomer = Customer(self.cus_id)
        self.ui.info_cusID_label.setText("NO: "+str(self.cus_id))
        self.ui.info_cusName_label.setText(
            currentCustomer.first_name+" "+currentCustomer.last_name)
        self.ui.info_TC_label.setText(currentCustomer.TC)
        self.ui.info_phoneNum_label.setText(currentCustomer.phone)
        self.ui.info_email_label.setText(currentCustomer.email)
        self.ui.info_address_label.setText(currentCustomer.address)

    def display_accounts(self):

        currentCustomer = Customer(self.cus_id)
        accounts = currentCustomer.list_accounts()
        self.ui.listAccounts_tableWidget_2.setRowCount(len(accounts))
        counter = 0
        for account in accounts:
            self.ui.listAccounts_tableWidget_2.setItem(
                counter, 0, QtWidgets.QTableWidgetItem(str(account.account_id)))
            self.ui.listAccounts_tableWidget_2.setItem(
                counter, 1, QtWidgets.QTableWidgetItem(account.currency))
            self.ui.listAccounts_tableWidget_2.setItem(
                counter, 2, QtWidgets.QTableWidgetItem(str(account.balance)))
            counter += 1

    def display_withdraw(self):
        currentCustomer = Customer(self.cus_id)
        accounts = currentCustomer.list_accounts()
        self.ui.withdraw_tableWidget.setRowCount(len(accounts))
        counter = 0
        for account in accounts:
            self.ui.withdraw_tableWidget.setItem(
                counter, 0, QtWidgets.QTableWidgetItem(str(account.account_id)))
            self.ui.withdraw_tableWidget.setItem(
                counter, 1, QtWidgets.QTableWidgetItem(account.currency))
            self.ui.withdraw_tableWidget.setItem(
                counter, 2, QtWidgets.QTableWidgetItem(str(account.balance)))
            counter += 1

    def display_deposit(self):
        currentCustomer = Customer(self.cus_id)
        accounts = currentCustomer.list_accounts()
        self.ui.deposit_tableWidget.setRowCount(len(accounts))
        counter = 0
        for account in accounts:
            self.ui.deposit_tableWidget.setItem(
                counter, 0, QtWidgets.QTableWidgetItem(str(account.account_id)))
            self.ui.deposit_tableWidget.setItem(
                counter, 1, QtWidgets.QTableWidgetItem(account.currency))
            self.ui.deposit_tableWidget.setItem(
                counter, 2, QtWidgets.QTableWidgetItem(str(account.balance)))
            counter += 1

    def display_delete(self):
        currentCustomer = Customer(self.cus_id)
        accounts = currentCustomer.list_accounts()
        self.ui.DA_tableWidget.setRowCount(len(accounts))
        counter = 0
        for account in accounts:
            self.ui.DA_tableWidget.setItem(
                counter, 0, QtWidgets.QTableWidgetItem(str(account.account_id)))
            self.ui.DA_tableWidget.setItem(
                counter, 1, QtWidgets.QTableWidgetItem(account.currency))
            self.ui.DA_tableWidget.setItem(
                counter, 2, QtWidgets.QTableWidgetItem(str(account.balance)))
            counter += 1

    def display_moneyTransfer(self):
        currentCustomer = Customer(self.cus_id)
        accounts = currentCustomer.list_accounts()
        self.ui.MT_listAccounts_tableWidget.setRowCount(len(accounts))
        counter = 0
        for account in accounts:
            self.ui.MT_listAccounts_tableWidget.setItem(
                counter, 0, QtWidgets.QTableWidgetItem(str(account.account_id)))
            self.ui.MT_listAccounts_tableWidget.setItem(
                counter, 1, QtWidgets.QTableWidgetItem(account.currency))
            self.ui.MT_listAccounts_tableWidget.setItem(
                counter, 2, QtWidgets.QTableWidgetItem(str(account.balance)))
            counter += 1

    def withdraw(self):
        cur_cus = Customer(self.cus_id)
        accounts = cur_cus.list_accounts()
        c = self.ui.withdraw_tableWidget.currentRow()
        selected_acc = accounts[c]

        try:
            amount = int(self.ui.withdraw_textEdit.toPlainText())
            if(c != -1 and (int(selected_acc.balance) - int(amount)) >= 0):
                selected_acc.withdraw(amount)
            else:
                msg.setText("Selection or overlimit ERROR")
                x = msg.exec_()
        except ValueError:
            msg.setText("Invalid input")
            x = msg.exec_()
        # Redirect to list accounts home page
        self.ui.listAccounts_radio.setChecked(True)
        self.showListAccounts()

    def deposit(self):
        cur_cus_d = Customer(self.cus_id)
        accounts_d = cur_cus_d.list_accounts()
        c = self.ui.deposit_tableWidget.currentRow()
        selected_acc = accounts_d[c]
        try:
            amount = int(self.ui.deposit_textEdit.toPlainText())
            if(c != -1 and type(amount) == int):
                selected_acc.deposit(amount)
            else:
                msg.setText("Selection or overlimit ERROR")
                x = msg.exec_()
        except ValueError:
            msg.setText("Invalid input")
            x = msg.exec_()

        self.ui.listAccounts_radio.setChecked(True)
        self.showListAccounts()

    def money_transfer(self):
        cur_cus_m = Customer(self.cus_id)
        accounts_m = cur_cus_m.list_accounts()
        c = self.ui.MT_listAccounts_tableWidget.currentRow()
        selected_acc = accounts_m[c]
        try:
            receiver_id = int(self.ui.to_account_no.toPlainText())
            total = int(self.ui.MT_total_textEdit.toPlainText())
            receiver_acc = searchAccountIDs(receiver_id)
            if(c != -1 and (int(selected_acc.balance) - int(total)) >= 0 and receiver_acc != 1):
                selected_acc.money_transfer(receiver_acc, total)
            else:
                msg.setText("Selection or overlimit ERROR or acc error")
                x = msg.exec_()
        except ValueError:
            msg.setText("Invalid input")
            x = msg.exec_()
        self.ui.listAccounts_radio.setChecked(True)
        self.showListAccounts()


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
        check = self.ui.customer_id_value.text()
        customer_id = check_user_input(check, "customer")
        if(type(customer_id) == int):
            main_win.hide()
            CustomerWindow.cus_id = customer_id
            customer_win.show()

    def clerk_clicked(self):
        ck_id = self.ui.clerk_id_value.text()
        check = check_user_input(ck_id, "customer")
        if(type(check) == int):
            main_win.hide()
            # clerk_window.show()

    def manager_clicked(self):
        main_win.hide()
        manager_window.show()

    # def customerId(self):
    #     return self.cus_id


app = QApplication(sys.argv)
msg = QMessageBox()
msg.setWindowTitle("Error")
main_win = MainWindow()
customer_win = CustomerWindow()
manager_window = ManagerWindow()
main_win.show()
sys.exit(app.exec_())
