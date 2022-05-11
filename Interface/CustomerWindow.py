import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from customerMain import Ui_CustomerWindow

from classes import Account, Customer, searchAccountIDs, getCurrencies, req_open


class CustomerWindow:
    cus_id = 0

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_CustomerWindow()
        self.ui.setupUi(self.main_win)
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PListAccounts)

        currencies = getCurrencies()
        self.ui.CA_currency_dropDown.addItems(currencies)

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
        self.ui.delete_acc_btn.clicked.connect(self.delete)
        self.ui.CA_create_account_button.clicked.connect(self.open_acc)
        self.ui.edit_save_button.clicked.connect(self.edit_info)

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
        self.display_monthlySummery()
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

        self.ui.FN_textEdit.setMarkdown(currentCustomer.first_name)
        self.ui.LN_textEdit.setMarkdown(currentCustomer.last_name)
        self.ui.TC_textEdit.setMarkdown(currentCustomer.TC)
        self.ui.phoneNum_textEdit.setMarkdown(currentCustomer.phone)
        self.ui.email_textEdit.setMarkdown(currentCustomer.email)
        self.ui.Address_textEdit.setMarkdown(currentCustomer.address)

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

    def display_monthlySummery(self):
        currentCustomer = Customer(self.cus_id)
        transactions = currentCustomer.list_transactions()
        self.ui.tableWidget.setRowCount(len(transactions))
        counter = 0
        for transaction in transactions:
            t = transaction.toArray()
            for i in range(0, 6):
                self.ui.tableWidget.setItem(
                    counter, i, QtWidgets.QTableWidgetItem(str(t[i])))
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
        try:
            amount = int(self.ui.deposit_textEdit.toPlainText())
            selected_acc = accounts_d[c]
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
        try:
            receiver_id = int(self.ui.to_account_no.toPlainText())
            total = int(self.ui.MT_total_textEdit.toPlainText())
            receiver_acc = searchAccountIDs(receiver_id)
            selected_acc = accounts_m[c]
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

    def delete(self):
        cur_cus = Customer(self.cus_id)
        accounts = cur_cus.list_accounts()
        c = self.ui.DA_tableWidget.currentRow()
        if(c != -1):
            selected_acc = accounts[c]
            if(selected_acc.balance != 0):
                msg.setText("Account's Balance is not 0\nCan't be deleted")
                x = msg.exec_()
            else:
                selected_acc.req_delete()
        else:
            msg.setText("Selection Error")
            x = msg.exec_()
        # label at the end of delete widget to inform the user
        # that account has been deleted
        self.ui.listAccounts_radio.setChecked(True)
        self.showListAccounts()

    def open_acc(self):
        currency = str(self.ui.CA_currency_dropDown.currentText())
        req_open(currency, self.cus_id)
        self.ui.listAccounts_radio.setChecked(True)
        self.showListAccounts()

    def edit_info(self):
        cur_cus = Customer(self.cus_id)
        try:
            fn = str(self.ui.FN_textEdit.toPlainText())
            ln = str(self.ui.LN_textEdit.toPlainText())
            tc = str(self.ui.TC_textEdit.toPlainText())
            p = str(self.ui.phoneNum_textEdit.toPlainText())
            e = str(self.ui.email_textEdit.toPlainText())
            ad = str(self.ui.Address_textEdit.toPlainText())
            cur_cus.update(fn, ln, e, p, tc, ad)
        except ValueError:
            msg.setText("Invalid input")
            x = msg.exec_()

        self.display_customer_info()
        self.ui.listAccounts_radio.setChecked(True)
        self.showListAccounts()
