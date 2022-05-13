
from audioop import add
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from matplotlib.widgets import Widget
from SQLconnection import cursor, connection
import classes

from ui_clerk import Ui_MainWindow


class clerk_Window:
    clerk_id = 0
    def __init__(self):
        #self.clerk_id = clerk_id
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.row = 0
        self.ui.clerk_id.setText(str(self.clerk_id))
        

        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PManage_customers)
        self.init_customer_comboBox()
        self.ui.reject_button.clicked.connect(self.rejectRequest)
        self.ui.accept_button.clicked.connect(self.acceptRequest)
        

        """self.init_manageCustomers()
        self.init_viewCusFinances()
        self.init_viewCusTransactions()
        self.init_viewCusRequests()"""
        self.ui.addCustomer_radio.clicked.connect(self.show_addCustomer)
        self.ui.manageCustomers_radio.clicked.connect(self.show_manageCustomers)
        self.ui.viewCusRequests_radio.clicked.connect(self.show_viewCusRequests)
        self.ui.viewCustomerFinances_radio.clicked.connect(self.show_viewCusFinances)
        self.ui.viewCusTransactions_radio.clicked.connect(self.show_viewCusTransactions)
        self.ui.customer_comboBox.currentTextChanged.connect(self.displayTransactions)
        
        

    def init_customer_comboBox(self):
        print(self.clerk_id)
        #clerk_id = 3
        cursor.execute(u'''SELECT cus_id 
                        FROM customerClerks2
                        WHERE clerk_id = (?);''', self.clerk_id)
        rows = cursor.fetchall()
        for i in rows:
            print(str(i.cus_id))
            self.ui.customer_comboBox.addItem(str(i.cus_id))

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
        #self.ui.addCustomer_button.clicked.connect(self.addCustomer)
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
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PManage_customers)

    def show_viewCusTransactions(self):
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PCustomer_transactions)

    def show_viewCusFinances(self):
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PCustomer_finances)

    def show_viewCusRequests(self):
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PCustomer_requests)

    def show_addCustomer(self):
        self.ui.addCustomer_button.clicked.connect(self.addCustomer)
        self.ui.operations_stackedWidget.setCurrentWidget(self.ui.PAdd_Customer)

    def displayTransactions(self):
        self.ui.transactions_table.setRowCount(0)
        
        cus_id = self.ui.customer_comboBox.currentText()
        row = 0
        self.ui.transactions_table.setRowCount(50)
        query = f'''SELECT DISTINCT trans_date, ua1.cus_id src_cus, ua2.cus_id rsv_cus, src_id, rsv_id, trans_type, total, (a1.balance - total) src_balance, (a2.balance + total *(ISNULL(c1.exch_rate,c2.exch_rate) / (ISNULL(c2.exch_rate,c1.exch_rate)))) as rsv_balance 
                    FROM transactions2 tr
                    LEFT JOIN account2 a1
                    ON tr.src_id = a1.acc_id
                    LEFT JOIN account2 a2
                    ON tr.rsv_id = a2.acc_id
                    LEFT JOIN userAccounts2 ua1
                    ON ua1.acc_id = src_id
                    LEFT JOIN userAccounts2 ua2
                    ON ua2.acc_id = rsv_id
                    LEFT JOIN currency c1
                    ON c1.curr_code = a1.currency
                    LEFT JOIN currency c2
                    ON c2.curr_code = a2.currency
                    WHERE ua1.cus_id = {cus_id} or ua2.cus_id = {cus_id};'''
        cursor.execute(query)

        for i in cursor:
            for col in range(0,9):
                self.ui.transactions_table.setItem(row, col, QtWidgets.QTableWidgetItem(str(i[col])))
            row += 1

    def displayCustomers(self):
        self.ui.MC_table.setRowCount(50)
        #clerk_id = 3
        query = f'''SELECT c.*
                FROM customer2 c, customerStatus2 cs , customerClerks2 cc
                WHERE cs.cus_id = cc.cus_id and
                    cc.clerk_id = {self.clerk_id} and
                    c.id = cs.cus_id and 
                    cus_status = 'ACTIVE' '''

        cursor.execute(query)

        for i in cursor:
            self.ui.MC_table.setItem(self.row, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            for col in range(1,7):
                self.ui.MC_table.setItem(self.row, col, QtWidgets.QTableWidgetItem(i[col]))
            self.row += 1

    def addCustomer(self):
        msg = QMessageBox()
        try:
            fn = str(self.ui.addFirstName_textEdit.toPlainText())
            ln = str(self.ui.addLastName_textEdit.toPlainText())
            tc = str(self.ui.addTC_textEdit.toPlainText())
            p = str(self.ui.addPhoneNum_textEdit.toPlainText())
            e = str(self.ui.addEmail_textEdit.toPlainText())
            ad = str(self.ui.addAddress_textEdit.toPlainText())
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

    def deleteCustomer(self):
        if(not self.ui.MC_table.item(self.ui.MC_table.currentRow(),0)): return
        cus_toBeDeleted = str(self.ui.MC_table.item(self.ui.MC_table.currentRow(),0).text())
        #if(not cus_toBeDeleted): return
        print(cus_toBeDeleted)
        self.ui.MC_table.removeRow(self.ui.MC_table.currentRow())
        self.ui.MC_table.setRowCount(50)
        cursor.execute(f''' UPDATE customerStatus2
                        SET cus_status = 'DELETED'
                        WHERE cus_id = {cus_toBeDeleted};''')
        cursor.commit()
        #cursor.execute()

        #cursor.commit()
        self.row -= 1

    def displayFinances(self):
        self.ui.finances_table.setRowCount(0)
        self.ui.finances_table.setRowCount(50)
        row = 0
        #clerk_id = 3
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
                            WHERE t1.cus_id = cc.cus_id and
                            cc.clerk_id = {self.clerk_id}
                            GROUP BY(t1.cus_id) ORDER BY t1.cus_id;'''
        cursor.execute(incomeQuery)

        for i in cursor:
            self.ui.finances_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.ui.finances_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            row+=1
        
        row = 0

        expenseQuery = f'''SELECT DISTINCT ua.cus_id, SUM(total * ISNULL(exch_rate,1))
                        FROM transactions2 tr, currency curr, account2 a, userAccounts2 ua
                        WHERE ua.acc_id = tr.src_id and
                            tr.src_id = a.acc_id and
                            a.currency = curr.curr_code
                            and (rsv_id NOT IN (SELECT acc_id
                                                FROM userAccounts2 ua2 
                                                WHERE ua.cus_id = ua2.cus_id)
                            OR rsv_id IS NULL) and ua.cus_id IN(SELECT cc.cus_id
                                                                FROM customerClerks2 cc
                                                                WHERE ua.cus_id = cc.cus_id and
                                                                cc.clerk_id = {self.clerk_id})
                        GROUP BY(ua.cus_id) ORDER BY ua.cus_id;'''

        cursor.execute(expenseQuery)

        for i in cursor:
            if str(i[0]) == self.ui.finances_table.item(row, 0).text():
                self.ui.finances_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(i[1])))
            row+=1
        
        row = 0

        totalBalanceQuery = f'''SELECT c.id, SUM(exch_rate * balance)  as totalBalance
                                FROM currency cur, userAccounts2 ua, account2 a, customer2 c
                                WHERE ua.acc_id = a.acc_id and
                                        a.currency = cur.curr_code and
                                        c.id = ua.cus_id and ua.cus_id IN(SELECT cc.cus_id
                                                                        FROM customerClerks2 cc
                                                                        WHERE ua.cus_id = cc.cus_id and
                                                                        cc.clerk_id = {self.clerk_id})
                                GROUP BY(c.id) ORDER BY c.id'''
        cursor.execute(totalBalanceQuery)

        for i in cursor:
            if str(i[0]) == self.ui.finances_table.item(row, 0).text():
                self.ui.finances_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(i[1])))
            row+=1

    def displayCustomerRequests(self):
        self.ui.customerRequests_table.setRowCount(0)
        self.ui.customerRequests_table.setRowCount(50)
        row = 0
        #clerk_id = 3
        requestQuery = f'''SELECT ua.cus_id, astat.acc_status, ua.acc_id 
                        FROM customerClerks2 cc, accountStatus2 astat, userAccounts2 ua
                        WHERE cc.cus_id = ua.cus_id and
                            ua.acc_id = astat.acc_id and
                            cc.clerk_id = {self.clerk_id} and
                            (astat.acc_status = 'R-DELETED' or astat.acc_status = 'R-OPEN')'''
        cursor.execute(requestQuery)

        for i in cursor:
            for col in range(0,3):
                self.ui.customerRequests_table.setItem(row, col, QtWidgets.QTableWidgetItem(str(i[col])))
            row += 1

    def acceptRequest(self):
        acc_id = self.ui.customerRequests_table.item(self.ui.customerRequests_table.currentRow(), 2).text()
        request_type = self.ui.customerRequests_table.item(self.ui.customerRequests_table.currentRow(), 1).text()

        if request_type == 'R-DELETED':
            cursor.execute(f'''UPDATE accountStatus2
                            SET acc_status = 'DELETED'
                            WHERE acc_id = {acc_id};''')
        elif request_type == 'R-OPEN':
            cursor.execute(f'''UPDATE accountStatus2
                            SET acc_status = 'ACTIVE'
                            WHERE acc_id = {acc_id};''')
        cursor.commit()

        self.ui.customerRequests_table.removeRow(self.ui.customerRequests_table.currentRow())
    
    def rejectRequest(self):
        acc_id = self.ui.customerRequests_table.item(self.ui.customerRequests_table.currentRow(), 2).text()
        request_type = self.ui.customerRequests_table.item(self.ui.customerRequests_table.currentRow(), 1).text()

        if request_type == 'R-DELETED':
            cursor.execute(f'''UPDATE accountStatus2
                            SET acc_status = 'ACTIVE'
                            WHERE acc_id = {acc_id};''')
        elif request_type == 'R-OPEN':
            cursor.execute(f'''UPDATE accountStatus2
                            SET acc_status = 'DELETED'
                            WHERE acc_id = {acc_id};''')
        cursor.commit()
        self.ui.customerRequests_table.removeRow(self.ui.customerRequests_table.currentRow())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = clerk_Window()
    main_win.show()
    sys.exit(app.exec_())


