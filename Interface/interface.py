from locale import currency
from functools import total_ordering
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
from SQLconnection import cursor, connection

from managerMain import Ui_ManagerWindow
from customerMain import Ui_CustomerWindow
from homeMain import Ui_MainWindow
import classes
from clerk_ui_functions import clerk_Window

from classes import Account, Customer, searchAccountIDs, getCurrencies, req_open


def check_user_input(input, type):
    try:
        u_id = int(input)
        if(type == "customer"):
            cursor.execute(
                '''SELECT customer2.* FROM customer2, customerStatus2 
                WHERE customerStatus2.cus_id = customer2.id and
                customer2.id = ? and
                customerStatus2.cus_status = 'ACTIVE' ''', u_id)
            row = cursor.fetchone()
            if(not row):
                msg.setWindowTitle("Error")
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
                msg.setWindowTitle("Error")
                msg.setText("Clerk not Found")
                x = msg.exec_()
                return "Clerk not Found"
            else:
                return u_id
    except ValueError:
        msg.setWindowTitle("Error")
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

        currencies = getCurrencies()
        self.ui.CA_currency_dropDown.addItems(currencies)

        self.ui.listAccounts_radio.clicked.connect(self.showListAccounts)
        self.ui.moneyTransfer_radio.clicked.connect(self.showMoneyTransfer)
        self.ui.withdraw_radio.clicked.connect(self.showWithdraw)
        self.ui.deposit_radio.clicked.connect(self.showDeposit)
        self.ui.newAccount_radio.clicked.connect(self.showCreateAccount)
        self.ui.deleteAccount_radio.clicked.connect(self.showDeleteAccount)
        self.ui.loan_info_radio.clicked.connect(self.showLoanInfo)
        self.ui.req_loan_radio.clicked.connect(self.showReqLoan)
        self.ui.editInfo_radio.clicked.connect(self.showEditInfo)
        self.ui.monthlySummary_radio.clicked.connect(self.showMonthlySummery)
        self.ui.monthlySummary_radio.clicked.connect(self.showMonthlySummery)

        self.ui.deposit_btn.clicked.connect(self.deposit)
        self.ui.withdraw_btn.clicked.connect(self.withdraw)
        self.ui.tranfer_btn.clicked.connect(self.money_transfer)
        self.ui.delete_acc_btn.clicked.connect(self.delete)
        self.ui.CA_create_account_button.clicked.connect(self.open_acc)
        self.ui.edit_save_button.clicked.connect(self.edit_info)
        self.ui.req_loan_btn.clicked.connect(self.requestLoan)

    def show(self):
        self.display_customer_info()
        self.display_accounts()
        self.main_win.show()

    def showMoneyTransfer(self):
        # print("customer2222: " + str(self.cus_id))
        self.display_moneyTransfer()
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PMoneyTransfer)

    def showLoanInfo(self):
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PLoanInfo)

    def showReqLoan(self):
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PRequestLoan)

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
            t = transaction.to_array_customer()
            for i in range(0, 5):
                self.ui.tableWidget.setItem(
                    counter, i, QtWidgets.QTableWidgetItem(str(t[i])))
            counter += 1

    def requestLoan(self):
        # req_loan_btn m_edit l_edit
        amount = self.ui.l_edit.text()
        months = self.ui.m_edit.text()
        print(months, amount, self.cus_id)
        query = f'''INSERT INTO loanRequests(cus_id, ay, anapara) VALUES({self.cus_id},{months},{amount})'''
        cursor.execute(query)
        cursor.commit()

    def withdraw(self):
        cur_cus = Customer(self.cus_id)
        accounts = cur_cus.list_accounts()
        c = self.ui.withdraw_tableWidget.currentRow()
        selected_acc = accounts[c]

        try:
            amount = float(self.ui.withdraw_textEdit.toPlainText())
            if(c != -1 and (float(selected_acc.balance) - float(amount)) >= 0):
                selected_acc.withdraw(amount)
            else:
                msg.setWindowTitle("Error")
                msg.setText("Selection or overlimit ERROR")
                x = msg.exec_()
        except ValueError:
            msg.setWindowTitle("Error")
            msg.setText("Invalid")
            x = msg.exec_()
        # Redirect to list accounts home page
        self.ui.listAccounts_radio.setChecked(True)
        self.showListAccounts()

    def deposit(self):
        cur_cus_d = Customer(self.cus_id)
        accounts_d = cur_cus_d.list_accounts()
        c = self.ui.deposit_tableWidget.currentRow()
        try:
            amount = float(self.ui.deposit_textEdit.toPlainText())
            selected_acc = accounts_d[c]
            if(c != -1):
                selected_acc.deposit(amount)
            else:
                msg.setWindowTitle("Error")
                msg.setText("Selection or overlimit ERROR")
                x = msg.exec_()
        except ValueError:
            msg.setWindowTitle("Error")
            msg.setText("Invalid")
            x = msg.exec_()

        self.ui.listAccounts_radio.setChecked(True)
        self.showListAccounts()

    def money_transfer(self):
        cur_cus_m = Customer(self.cus_id)
        accounts_m = cur_cus_m.list_accounts()
        c = self.ui.MT_listAccounts_tableWidget.currentRow()
        try:
            receiver_id = int(self.ui.to_account_no.toPlainText())
            total = float(self.ui.MT_total_textEdit.toPlainText())
            receiver_acc = searchAccountIDs(receiver_id)
            selected_acc = accounts_m[c]
            if(c != -1 and (float(selected_acc.balance) - float(total)) >= 0 and receiver_acc != 1):
                selected_acc.money_transfer(receiver_acc, total)
            else:
                msg.setWindowTitle("Error")
                msg.setText("Selection or overlimit ERROR \nor acc error")
                x = msg.exec_()
        except ValueError:
            msg.setWindowTitle("Error")
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
            msg.setWindowTitle("Error")
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
            msg.setWindowTitle("Error")
            msg.setText("Invalid input")
            x = msg.exec_()

        self.display_customer_info()
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
        self.ui.main.clicked.connect(self.showMain)

        self.display_update_currency()
        self.display_update_interest()
        self.display_update_salary()
        self.display_summery()
        self.init_LoadRequests()

        self.ui.pushButton.clicked.connect(self.add_customer)
        self.ui.loan_requests.clicked.connect(self.showLoanRequests)
        self.ui.add_currency_btn.clicked.connect(self.add_currency)
        self.ui.update_currency_btn.clicked.connect(self.update_currency)
        self.ui.accept_loan_btn.clicked.connect(self.acceptRequest)
        self.ui.reject_loan_btn.clicked.connect(self.rejectRequest)

    def show(self):
        self.diplayFinances()
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

    def showMain(self):
        self.diplayFinances()
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_widget)

    def showView_transactions(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.view_transactions_widget)

    def showLoanRequests(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loan_requests_widget)

    def init_LoadRequests(self):
        self.ui.loan_req_tableWidget.setRowCount(50)
        # loan_req_tableWidget
        # reject_loan_btn
        # faiz_edit
        # accept_loan_btn
        query = '''SELECT req_no, cus_id, ay, anapara
                    FROM loanRequests
                    WHERE faiz IS NULL;'''
        cursor.execute(query)
        #rows = cursor.fetchall()
        row = 0
        for item in cursor:
            for col in range(0, 4):
                self.ui.loan_req_tableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(item[col])))
            row += 1

    def display_summery(self):
        self.ui.income_value.setText("404")
        self.ui.expenses_value.setText("404")
        self.ui.profit_value.setText("404")
        self.ui.balance_value.setText("404")

    def display_update_currency(self):
        self.ui.currency_comboBox.clear()
        currencies = getCurrencies()
        self.ui.currency_comboBox.addItems(currencies)

    def display_update_interest(self):
        self.ui.previous_interest_value.setText("404")

    def display_update_salary(self):
        salary = classes.get_salary()
        self.ui.previous_salary_value.setText(str(salary))

    def diplayFinances(self):
        incomeQuery = '''
                SELECT lp.total + dep.total bank_income
                FROM (SELECT SUM(total) total
                FROM transactions2 tr
                WHERE trans_type = 'loan payment') as lp,
                (SELECT SUM(t2.total*exch_rate) total
                FROM transactions2 t2, account2 a, currency cur
                WHERE (t2.trans_type = 'deposit' and
                    t2.rsv_id = a.acc_id and
                    cur.curr_code = a.currency)) as dep'''

        expensesQuery = '''SELECT lt.total + wd.total bank_expense
                    FROM (SELECT SUM(total) total
                    FROM transactions2 tr
                    WHERE trans_type = 'loan takeout') as lt,
                    (SELECT SUM(t2.total*exch_rate) total
                    FROM transactions2 t2, account2 a, currency cur
                    WHERE (t2.trans_type = 'withdraw' and
                        t2.src_id = a.acc_id and
                        cur.curr_code = a.currency)) as wd'''

        totalBalanceQuery = '''SELECT SUM(balance * exch_rate) bank_balance
                        FROM account2 a, currency curr
                        WHERE a.currency = curr.curr_code'''

        cursor.execute(incomeQuery)
        income = cursor.fetchone()[0]
        cursor.execute(expensesQuery)
        expense = cursor.fetchone()[0]
        cursor.execute(totalBalanceQuery)
        totalBalance = cursor.fetchone()[0]
        print(income, totalBalance, expense)
        self.ui.income_value.setText(str(income))
        self.ui.expenses_value.setText(str(expense))
        self.ui.balance_value.setText(str(totalBalance))

    def add_customer(self):
        try:
            fn = str(self.ui.FN_textEdit.toPlainText())
            ln = str(self.ui.LN_textEdit.toPlainText())
            tc = str(self.ui.TC_textEdit.toPlainText())
            p = str(self.ui.phoneNum_textEdit.toPlainText())
            e = str(self.ui.email_textEdit.toPlainText())
            ad = str(self.ui.Address_textEdit.toPlainText())
            if not fn:
                raise ValueError()
            if not ln:
                raise ValueError()
            if not tc:
                raise ValueError()
            if not p:
                raise ValueError()
            if not e:
                raise ValueError()
            if not ad:
                raise ValueError()
            classes.add_customer(fn, ln, e, p, tc, ad)
            msg.setWindowTitle("Success")
            msg.setText("Customer Has Been Added")
            x = msg.exec_()
        except ValueError:
            msg.setWindowTitle("Error")
            msg.setText("Invalid input")
            x = msg.exec_()

    def add_currency(self):
        try:
            cur_code = str(self.ui.currency_code_value.toPlainText())
            ex = str(self.ui.new_er_value.toPlainText())
            if not cur_code:
                raise ValueError()
            if not ex:
                raise ValueError()
            classes.add_currency(cur_code, ex)
            msg.setWindowTitle("Susccess")
            msg.setText("Currency Has Been Added")
            x = msg.exec_()
        except ValueError:
            msg.setWindowTitle("Error")
            msg.setText("Invalid input")
            x = msg.exec_()
        except:
            msg.setWindowTitle("Error")
            msg.setText("Currency already Exists")
            x = msg.exec_()

    def update_currency(self):
        try:
            u_rate = str(self.ui.update_er_value.toPlainText())
            currency = str(self.ui.currency_comboBox.currentText())
            if not u_rate:
                raise ValueError()
            classes.add_currency(currency, u_rate)
            msg.setWindowTitle("Susccess")
            msg.setText("Currency Has Been Updated")
            x = msg.exec_()
        except ValueError:
            msg.setWindowTitle("Error")
            msg.setText("Invalid input")
            x = msg.exec_()

    def acceptRequest(self):
        try:
            today = str(date.today())
            faiz = self.ui.faiz_edit.text()

            if not faiz:
                raise ValueError()
            isSelected = self.ui.loan_req_tableWidget.currentRow()

            if isSelected == -1:
                msg.setWindowTitle("Error")
                msg.setText("Please select row")
                x = msg.exec_()
            else:
                req_no = self.ui.loan_req_tableWidget.item(
                    isSelected, 0).text()
                print(faiz, type(faiz), today, type(
                    today), req_no, type(req_no))
                query = f'''UPDATE loanRequests 
                            SET acpt_date = '{today}', faiz = {faiz}
                            WHERE req_no = {req_no}'''
                cursor.execute(query)
                cursor.commit()
                self.ui.loan_req_tableWidget.removeRow(
                    self.ui.loan_req_tableWidget.currentRow())
                self.ui.loan_req_tableWidget.setRowCount(50)

        except ValueError:
            msg.setWindowTitle("Error")
            msg.setText("Invalid input")
            x = msg.exec_()

    def rejectRequest(self):
        try:
            date = 'NULL'
            faiz = '-1'
            selected = self.ui.loan_req_tableWidget.currentRow()

            if selected == -1:
                msg.setWindowTitle("Error")
                msg.setText("Please select row")
                x = msg.exec_()
            else:
                req_no = self.ui.loan_req_tableWidget.item(selected, 0).text()
                query = f'''UPDATE loanRequests 
                            SET acpt_date = {date}, faiz = {faiz}
                            WHERE req_no = {req_no}'''
                cursor.execute(query)
                cursor.commit()

                self.ui.loan_req_tableWidget.removeRow(
                    self.ui.loan_req_tableWidget.currentRow())

                self.ui.loan_req_tableWidget.setRowCount(50)
        except ValueError:
            msg.setWindowTitle("Error")
            msg.setText("Please select row")
            x = msg.exec_()


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
            # main_win.hide()
            CustomerWindow.cus_id = customer_id
            customer_win.show()

    def clerk_clicked(self):
        ck_id = self.ui.clerk_id_value.text()
        check = check_user_input(ck_id, "clerk")
        print(check)
        if(type(check) == int):
            # main_win.hide()
            clerk_window.setClerkID(check)
            clerk_window.init_window()
            clerk_window.show()

    def manager_clicked(self):
        # main_win.hide()
        manager_window.show()


app = QApplication(sys.argv)
msg = QMessageBox()
# msg.setWindowTitle("Error")
main_win = MainWindow()
customer_win = CustomerWindow()
manager_window = ManagerWindow()
clerk_window = clerk_Window()
main_win.show()
sys.exit(app.exec_())
