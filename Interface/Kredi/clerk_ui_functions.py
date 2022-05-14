
from audioop import add
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from matplotlib.widgets import Widget
from SQLconnection import cursor, connection
import classes
from classes import Clerk, Customer

from ui_clerk import Ui_MainWindow


class clerk_Window:
    clerk_id = 0

    def __init__(self):
        # self.clerk_id = clerk_id
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.row = 0
        self.ui.clerk_id.setText(str(self.clerk_id))

        self.ui.manageCustomers_radio.setChecked(True)

        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PManage_customers)
        # self.init_customer_comboBox()
        self.ui.reject_button.clicked.connect(self.rejectRequest)
        self.ui.accept_button.clicked.connect(self.acceptRequest)

        self.ui.addCustomer_radio.clicked.connect(self.show_addCustomer)
        self.ui.edit_cus_radio.clicked.connect(self.show_edit_info)
        self.ui.manageCustomers_radio.clicked.connect(
            self.show_manageCustomers)
        self.ui.viewCusRequests_radio.clicked.connect(
            self.show_viewCusRequests)
        self.ui.viewCustomerFinances_radio.clicked.connect(
            self.show_viewCusFinances)
        self.ui.viewCusTransactions_radio.clicked.connect(
            self.show_viewCusTransactions)
        self.ui.customer_comboBox.currentTextChanged.connect(
            self.displayTransactions)
        self.ui.customer_comboBox.currentTextChanged.connect(
            self.displayCustomers)
        self.ui.customer_comboBox.currentTextChanged.connect(
            self.displayFinances)
        self.ui.customer_comboBox.currentTextChanged.connect(
            self.displayFinances)
        self.ui.customer_comboBox.currentTextChanged.connect(
            self.display_customer_info)

        self.ui.addCustomer_button.clicked.connect(self.addCustomer)
        self.ui.edit_save_button.clicked.connect(self.edit_info)

    def init_customer_comboBox(self):
        # clerk_id = 3
        c = self.ui.customer_comboBox.count()
        clerk = Clerk(self.clerk_id)
        # self.ui.customer_comboBox.clear()
        self.ui.customer_comboBox.addItems(clerk.customers)
        if (c != 0):
            for i in range(0, c):
                self.ui.customer_comboBox.removeItem(0)

    def init_window(self):
        self.ui.clerk_id.setText(str(self.clerk_id))
        self.init_customer_comboBox()
        self.init_manageCustomers()
        self.init_viewCusFinances()
        self.init_viewCusTransactions()
        self.init_viewCusRequests()

    def show(self):
        self.main_win.show()

    def setClerkID(self, clerk_id):
        self.clerk_id = clerk_id

    def init_manageCustomers(self):
        self.displayCustomers()

        self.ui.deleteCustomer_button.clicked.connect(self.deleteCustomer)

    def init_viewCusTransactions(self):
        self.ui.transactions_table.setRowCount(0)
        self.displayTransactions()

    def init_viewCusFinances(self):
        self.ui.finances_table.setRowCount(0)
        self.displayFinances()

    def init_viewCusRequests(self):
        self.ui.customerRequests_table.setRowCount(0)
        self.displayCustomerRequests()

    def show_manageCustomers(self):
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PManage_customers)

    def show_viewCusTransactions(self):
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PCustomer_transactions)

    def show_edit_info(self):
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.edit_cus_widget_2)

    def show_viewCusFinances(self):
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PCustomer_finances)

    def show_viewCusRequests(self):
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.PCustomer_requests)

    def show_addCustomer(self):
        self.ui.operations_stackedWidget.setCurrentWidget(
            self.ui.add_customer_widget)

    def displayTransactions(self):
        self.ui.transactions_table.setRowCount(0)
        clerk = Clerk(self.clerk_id)
        cus_id = self.ui.customer_comboBox.currentText()
        transactions = clerk.list_transactions(cus_id)
        self.ui.transactions_table.setRowCount(len(transactions))
        counter = 0
        for transaction in transactions:
            # print(transaction)
            for i in range(0, 9):
                self.ui.transactions_table.setItem(
                    counter, i, QtWidgets.QTableWidgetItem(str(transaction[i])))
            counter += 1

    def displayCustomers(self):
        clerk = Clerk(self.clerk_id)
        customers = clerk.list_customer()
        self.ui.MC_table.setRowCount(len(customers))

        counter = 0
        for customer in customers:
            arr = customer.to_array()
            for i in range(0, 7):
                self.ui.MC_table.setItem(
                    counter, i, QtWidgets.QTableWidgetItem(str(arr[i])))
            counter += 1

    def addCustomer(self):
        msg = QMessageBox()
        try:
            fn = str(self.ui.firstName_textEdit.toPlainText())
            ln = str(self.ui.lastName_textEdit.toPlainText())
            tc = str(self.ui.TC_textEdit.toPlainText())
            p = str(self.ui.phoneNum_textEdit.toPlainText())
            e = str(self.ui.email_textEdit.toPlainText())
            ad = str(self.ui.address_textEdit.toPlainText())
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

        self.init_customer_comboBox()

    def deleteCustomer(self):
        msg = QMessageBox()
        if(not self.ui.MC_table.item(self.ui.MC_table.currentRow(), 0)):
            return
        cus_toBeDeleted = str(self.ui.MC_table.item(
            self.ui.MC_table.currentRow(), 0).text())
        # print(cus_toBeDeleted)
        if(cus_toBeDeleted == "-1"):
            msg.setWindowTitle("Error")
            msg.setText("Selection or overlimit ERROR")
            x = msg.exec_()
        else:
            o = classes.delete_customer(cus_toBeDeleted)
            if(o == -1):
                msg.setWindowTitle("Error")
                msg.setText("Customer Can't be deleted\nbalance isn't 0")
                x = msg.exec_()
            else:
                msg.setWindowTitle("Success")
                msg.setText("Customer has been deleted")
                x = msg.exec_()
            self.displayCustomers()
            self.init_customer_comboBox()

    def displayFinances(self):
        cus_id = self.ui.customer_comboBox.currentText()
        self.ui.finances_table.setRowCount(0)
        self.ui.finances_table.setRowCount(50)
        row = 0
        # clerk_id = 3
        incomeQuery = f'''SELECT t1.cus_id, SUM(ISNULL(t1.income, 0) + ISNULL(t2.income,0))
                        FROM (SELECT ua2.cus_id , SUM(total * c1.exch_rate) income
                        FROM transactions2 tr, account2 a1, account2 a2, userAccounts2 ua1, userAccounts2 ua2, currency c1, currency c2
                        WHERE tr.src_id = a1.acc_id and
                        tr.rsv_id = a2.acc_id and
                        ua1.acc_id = src_id and
                        ua2.acc_id = rsv_id and
                        c1.curr_code = a1.currency and 
                        c2.curr_code = a2.currency and src_id not in(SELECT acc_id
                        FROM userAccounts2 ua
                        WHERE ua.cus_id = ua2.cus_id)
                        GROUP BY(ua2.cus_id)) t1
                        FULL OUTER JOIN (
                        SELECT ua1.cus_id, SUM(total * c1.exch_rate) income
                        FROM transactions2 tr, account2 a1, userAccounts2 ua1, currency c1
                        WHERE src_id IS NULL and
                        rsv_id = ua1.acc_id and
                        ua1.acc_id = a1.acc_id and
                        a1.currency = c1.curr_code
                        GROUP BY(ua1.cus_id)) t2 on t2.cus_id = t1.cus_id, customerClerks2 cc
                        WHERE t1.cus_id = cc.cus_id and t1.cus_id = {cus_id}
                        GROUP BY(t1.cus_id) ORDER BY t1.cus_id;'''
        cursor.execute(incomeQuery)

        for i in cursor:
            self.ui.finances_table.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.ui.finances_table.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            row += 1

        row = 0

        expenseQuery = f'''SELECT DISTINCT ua.cus_id, SUM(total * ISNULL(exch_rate,1))
                        FROM transactions2 tr, currency curr, account2 a, userAccounts2 ua
                        WHERE ua.acc_id = tr.src_id and
                        tr.src_id = a.acc_id and
                        a.currency = curr.curr_code
                        and (rsv_id NOT IN (SELECT acc_id
                        FROM userAccounts2 ua2 
                        WHERE ua.cus_id = ua2.cus_id)
                        OR rsv_id IS NULL) and ua.cus_id = {cus_id}
                        GROUP BY(ua.cus_id) ORDER BY ua.cus_id'''

        cursor.execute(expenseQuery)

        for i in cursor:
            k = self.ui.finances_table.item(row, 0)
            if k and str(i[0]) == k.text():
                self.ui.finances_table.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(str(i[1])))
            row += 1

        row = 0

        totalBalanceQuery = f'''SELECT c.id, SUM(exch_rate * balance)  as totalBalance
                            FROM currency cur, userAccounts2 ua, account2 a, customer2 c
                            WHERE ua.acc_id = a.acc_id and
                            a.currency = cur.curr_code and
                            c.id = ua.cus_id and 
                            c.id = {cus_id}
                            GROUP BY(c.id) ORDER BY c.id'''
        cursor.execute(totalBalanceQuery)

        for i in cursor:
            j = self.ui.finances_table.item(row, 0)
            if j and (str(i[0]) == j.text()):
                self.ui.finances_table.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(str(i[1])))
            row += 1

    def displayCustomerRequests(self):
        self.ui.customerRequests_table.setRowCount(0)
        self.ui.customerRequests_table.setRowCount(50)
        row = 0
        # clerk_id = 3
        requestQuery = f'''SELECT ua.cus_id, astat.acc_status, ua.acc_id 
                        FROM customerClerks2 cc, accountStatus2 astat, userAccounts2 ua
                        WHERE cc.cus_id = ua.cus_id and
                            ua.acc_id = astat.acc_id and
                            cc.clerk_id = {self.clerk_id} and
                            (astat.acc_status = 'R-DELETED' or astat.acc_status = 'R-OPEN')'''
        cursor.execute(requestQuery)

        for i in cursor:
            for col in range(0, 3):
                self.ui.customerRequests_table.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(i[col])))
            row += 1

    def display_customer_info(self):
        cus_id = int(self.ui.customer_comboBox.currentText())
        currentCustomer = Customer(cus_id)
        self.ui.FN_textEdit.setMarkdown(currentCustomer.first_name)
        self.ui.LN_textEdit.setMarkdown(currentCustomer.last_name)
        self.ui.TC_textEdit_2.setMarkdown(currentCustomer.TC)
        self.ui.phoneNum_textEdit_2.setMarkdown(currentCustomer.phone)
        self.ui.email_textEdit_2.setMarkdown(currentCustomer.email)
        self.ui.Address_textEdit.setMarkdown(currentCustomer.address)

    def acceptRequest(self):
        msg = QMessageBox()
        acc_id = self.ui.customerRequests_table.item(
            self.ui.customerRequests_table.currentRow(), 2).text()
        request_type = self.ui.customerRequests_table.item(
            self.ui.customerRequests_table.currentRow(), 1).text()
        if (acc_id == -1 or request_type == -1):
            msg.setWindowTitle("Error")
            msg.setText("Selection ERROR")
            x = msg.exec_()
        else:
            if request_type == 'R-DELETED':
                cursor.execute(f'''UPDATE accountStatus2
                                SET acc_status = 'DELETED'
                                WHERE acc_id = {acc_id};''')
            elif request_type == 'R-OPEN':
                cursor.execute(f'''UPDATE accountStatus2
                                SET acc_status = 'ACTIVE'
                                WHERE acc_id = {acc_id};''')
            cursor.commit()

        msg.setWindowTitle("Success")
        msg.setText("Request Has Been Accepted")
        x = msg.exec_()
        self.displayCustomerRequests()

    def rejectRequest(self):
        msg = QMessageBox()
        acc_id = self.ui.customerRequests_table.item(
            self.ui.customerRequests_table.currentRow(), 2).text()
        request_type = self.ui.customerRequests_table.item(
            self.ui.customerRequests_table.currentRow(), 1).text()

        if request_type == 'R-DELETED':
            cursor.execute(f'''UPDATE accountStatus2
                            SET acc_status = 'ACTIVE'
                            WHERE acc_id = {acc_id};''')
        elif request_type == 'R-OPEN':
            cursor.execute(f'''UPDATE accountStatus2
                            SET acc_status = 'DELETED'
                            WHERE acc_id = {acc_id};''')
        cursor.commit()

        msg.setWindowTitle("Reject")
        msg.setText("Request Has Been Rejected")
        x = msg.exec_()
        self.displayCustomerRequests()

    def edit_info(self):
        cus_id = int(self.ui.customer_comboBox.currentText())
        cur_cus = Customer(cus_id)
        try:
            fn = str(self.ui.FN_textEdit.toPlainText())
            ln = str(self.ui.LN_textEdit.toPlainText())
            tc = str(self.ui.TC_textEdit_2.toPlainText())
            p = str(self.ui.phoneNum_textEdit_2.toPlainText())
            e = str(self.ui.email_textEdit_2.toPlainText())
            ad = str(self.ui.Address_textEdit.toPlainText())
            cur_cus.update(fn, ln, e, p, tc, ad)
        except ValueError:
            msg.setWindowTitle("Error")
            msg.setText("Invalid input")
            x = msg.exec_()

        self.displayCustomers()
        self.ui.manageCustomers_radio.setChecked(True)
        self.show_manageCustomers()
