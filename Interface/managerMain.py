import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 110, 901, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(290, 140, 20, 581))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.main = QtWidgets.QRadioButton(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(40, 170, 161, 21))
        self.main.setChecked(True)
        self.main.setObjectName("main")

        self.addNewCurrency = QtWidgets.QRadioButton(self.centralwidget)
        self.addNewCurrency.setGeometry(QtCore.QRect(40, 220, 171, 20))
        self.addNewCurrency.setObjectName("addNewCurrency")

        self.updateCurrency = QtWidgets.QRadioButton(self.centralwidget)
        self.updateCurrency.setGeometry(QtCore.QRect(40, 270, 171, 20))
        self.updateCurrency.setObjectName("updateCurrency")

        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setGeometry(QtCore.QRect(330, 150, 601, 571))
        self.mainWidget.setObjectName("mainWidget")

        self.mainLable = QtWidgets.QLabel(self.centralwidget)
        self.mainLable.setGeometry(QtCore.QRect(380, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mainLable.setFont(font)
        self.mainLable.setObjectName("mainLable")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # On radio button clicks
        self.main.clicked.connect(self.interface)
        self.addNewCurrency.clicked.connect(self.interface)
        self.updateCurrency.clicked.connect(self.interface)

        self.income = QtWidgets.QLabel(self.mainWidget)
        self.income.setGeometry(QtCore.QRect(70, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.income.setFont(font)
        self.income.setObjectName("income")

        self.expenses = QtWidgets.QLabel(self.mainWidget)
        self.expenses.setGeometry(QtCore.QRect(70, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.expenses.setFont(font)
        self.expenses.setObjectName("expenses")

        self.profit = QtWidgets.QLabel(self.mainWidget)
        self.profit.setGeometry(QtCore.QRect(70, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.profit.setFont(font)
        self.profit.setObjectName("profit")

        self.balance = QtWidgets.QLabel(self.mainWidget)
        self.balance.setGeometry(QtCore.QRect(70, 390, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.balance.setFont(font)
        self.balance.setObjectName("balance")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def interface(self):
        if self.main.isChecked():
            self.mainWidget.show()

        elif self.addNewCurrency.isChecked():
            self.mainWidget.hide()

        elif self.updateCurrency.isChecked():
            self.mainWidget.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main.setText(_translate("MainWindow", "Mail"))
        self.addNewCurrency.setText(
            _translate("MainWindow", "Add New Currency"))
        self.updateCurrency.setText(
            _translate("MainWindow", "Update Currency"))
        self.income.setText(_translate("MainWindow", "Income"))
        self.expenses.setText(_translate("MainWindow", "Expenses"))
        self.profit.setText(_translate("MainWindow", "Profit"))
        self.balance.setText(_translate("MainWindow", "Total Balance"))
        self.mainLable.setText(_translate("MainWindow", "Bank Muduru"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
