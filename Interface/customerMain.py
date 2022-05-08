from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CustomerWindow(object):
    def setupUi(self, CustomerWindow):
        CustomerWindow.setObjectName("CustomerWindow")
        CustomerWindow.resize(885, 795)
        CustomerWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(CustomerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.info = QtWidgets.QWidget(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(0, 0, 1251, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 27, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.info.setPalette(palette)
        self.info.setStyleSheet("#info{\n"
                                "background-color: rgb(2, 27, 66);\n"
                                "}")
        self.info.setObjectName("info")
        self.cusID = QtWidgets.QLabel(self.info)
        self.cusID.setGeometry(QtCore.QRect(30, -20, 121, 121))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.cusID.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cusID.setFont(font)
        self.cusID.setObjectName("cusID")
        self.cusName = QtWidgets.QLabel(self.info)
        self.cusName.setGeometry(QtCore.QRect(180, -20, 271, 121))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.cusName.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.cusName.setFont(font)
        self.cusName.setObjectName("cusName")
        self.subOp = QtWidgets.QWidget(self.centralwidget)
        self.subOp.setGeometry(QtCore.QRect(240, 90, 1221, 851))
        self.subOp.setStyleSheet("#subOp{\n"
                                 "    background-color:#ffffff;\n"
                                 "}")
        self.subOp.setObjectName("subOp")
        self.stackedWidget = QtWidgets.QStackedWidget(self.subOp)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 651, 701))
        self.stackedWidget.setObjectName("stackedWidget")
        self.PListAccounts = QtWidgets.QWidget()
        self.PListAccounts.setObjectName("PListAccounts")
        self.acc1 = QtWidgets.QGroupBox(self.PListAccounts)
        self.acc1.setGeometry(QtCore.QRect(20, 20, 611, 91))
        self.acc1.setStyleSheet("#acc1{\n"
                                "    border-width:4px;\n"
                                "    border-color:rgb(62, 90, 127);\n"
                                "    border-style:solid;\n"
                                "    border-radius:20px;\n"
                                "}")
        self.acc1.setTitle("")
        self.acc1.setObjectName("acc1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.acc1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accID = QtWidgets.QLabel(self.acc1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accID.setFont(font)
        self.accID.setObjectName("accID")
        self.horizontalLayout.addWidget(self.accID)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.accBalance = QtWidgets.QLabel(self.acc1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accBalance.setFont(font)
        self.accBalance.setObjectName("accBalance")
        self.horizontalLayout.addWidget(self.accBalance)
        self.accCurrency = QtWidgets.QLabel(self.acc1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accCurrency.setFont(font)
        self.accCurrency.setObjectName("accCurrency")
        self.horizontalLayout.addWidget(self.accCurrency)
        self.stackedWidget.addWidget(self.PListAccounts)
        self.PWithdraw = QtWidgets.QWidget()
        self.PWithdraw.setObjectName("PWithdraw")
        self.textEdit_3 = QtWidgets.QTextEdit(self.PWithdraw)
        self.textEdit_3.setGeometry(QtCore.QRect(50, 60, 391, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_8 = QtWidgets.QLabel(self.PWithdraw)
        self.label_8.setGeometry(QtCore.QRect(50, 110, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.PWithdraw)
        self.label_9.setGeometry(QtCore.QRect(50, 30, 101, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox_4 = QtWidgets.QComboBox(self.PWithdraw)
        self.comboBox_4.setGeometry(QtCore.QRect(50, 140, 73, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.stackedWidget.addWidget(self.PWithdraw)
        self.PDeposit = QtWidgets.QWidget()
        self.PDeposit.setObjectName("PDeposit")
        self.label_4 = QtWidgets.QLabel(self.PDeposit)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.PDeposit)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 55, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.PDeposit)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 190, 73, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textEdit_2 = QtWidgets.QTextEdit(self.PDeposit)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 110, 391, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.stackedWidget.addWidget(self.PDeposit)
        self.PDeleteAccount = QtWidgets.QWidget()
        self.PDeleteAccount.setObjectName("PDeleteAccount")
        self.comboBox_5 = QtWidgets.QComboBox(self.PDeleteAccount)
        self.comboBox_5.setGeometry(QtCore.QRect(40, 70, 73, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_2 = QtWidgets.QLabel(self.PDeleteAccount)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 501, 16))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.PDeleteAccount)
        self.PCreateAccount = QtWidgets.QWidget()
        self.PCreateAccount.setObjectName("PCreateAccount")
        self.stackedWidget.addWidget(self.PCreateAccount)
        self.PMoneyTransfer = QtWidgets.QWidget()
        self.PMoneyTransfer.setObjectName("PMoneyTransfer")
        self.label = QtWidgets.QLabel(self.PMoneyTransfer)
        self.label.setGeometry(QtCore.QRect(50, 70, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.PMoneyTransfer)
        self.comboBox.setGeometry(QtCore.QRect(50, 190, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.PMoneyTransfer)
        self.label_6.setGeometry(QtCore.QRect(50, 160, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.PMoneyTransfer)
        self.label_7.setGeometry(QtCore.QRect(250, 160, 55, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.PMoneyTransfer)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 190, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.PMoneyTransfer)
        self.textEdit.setGeometry(QtCore.QRect(50, 100, 391, 31))
        self.textEdit.setObjectName("textEdit")
        self.radioButton = QtWidgets.QRadioButton(self.PMoneyTransfer)
        self.radioButton.setGeometry(QtCore.QRect(50, 260, 331, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.PMoneyTransfer)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 320, 331, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.PMoneyTransfer)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 380, 331, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.stackedWidget.addWidget(self.PMoneyTransfer)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 90, 241, 701))
        self.frame.setStyleSheet("#frame{\n"
                                 "    background-color:rgb(62, 90, 127);\n"
                                 "    border-width:0px;\n"
                                 "    border-style:none;\n"
                                 "    height:100%;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listAccounts = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listAccounts.sizePolicy().hasHeightForWidth())
        self.listAccounts.setSizePolicy(sizePolicy)
        self.listAccounts.setMinimumSize(QtCore.QSize(62, 50))
        self.listAccounts.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        self.listAccounts.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.listAccounts.setFont(font)
        self.listAccounts.setStyleSheet("QRadioButton::indicator{\n"
                                        "    width:0;\n"
                                        "    height:0;\n"
                                        "}\n"
                                        "\n"
                                        "QRadioButton::indicator::unchecked {\n"
                                        "    image: url(:/images/radiobutton_unchecked.png);\n"
                                        "}\n"
                                        "\n"
                                        "QRadioButton::checked {\n"
                                        "    background-color: #ffffff;\n"
                                        "}\n"
                                        "\n"
                                        "QRadioButton::indicator::checked {\n"
                                        "    visibility:hidden;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.listAccounts.setCheckable(True)
        self.listAccounts.setChecked(False)
        self.listAccounts.setObjectName("listAccounts")
        self.buttonGroup = QtWidgets.QButtonGroup(CustomerWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.listAccounts)
        self.verticalLayout.addWidget(self.listAccounts)
        self.moneyTransfer = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.moneyTransfer.sizePolicy().hasHeightForWidth())
        self.moneyTransfer.setSizePolicy(sizePolicy)
        self.moneyTransfer.setMinimumSize(QtCore.QSize(62, 50))
        self.moneyTransfer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        self.moneyTransfer.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.moneyTransfer.setFont(font)
        self.moneyTransfer.setStyleSheet("QRadioButton::indicator{\n"
                                         "    width:0;\n"
                                         "    height:0;\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::indicator::unchecked {\n"
                                         "    image: url(:/images/radiobutton_unchecked.png);\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::checked {\n"
                                         "    background-color: #ffffff;\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::indicator::checked {\n"
                                         "    visibility:hidden;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.moneyTransfer.setCheckable(True)
        self.moneyTransfer.setChecked(False)
        self.moneyTransfer.setObjectName("moneyTransfer")
        self.buttonGroup.addButton(self.moneyTransfer)
        self.verticalLayout.addWidget(self.moneyTransfer)
        self.withdraw = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.withdraw.sizePolicy().hasHeightForWidth())
        self.withdraw.setSizePolicy(sizePolicy)
        self.withdraw.setMinimumSize(QtCore.QSize(21, 50))
        self.withdraw.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.withdraw.setFont(font)
        self.withdraw.setAutoFillBackground(False)
        self.withdraw.setStyleSheet("QRadioButton::indicator{\n"
                                    "    width:0;\n"
                                    "    height:0;\n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::indicator::unchecked {\n"
                                    "    image: url(:/images/radiobutton_unchecked.png);\n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::checked {\n"
                                    "    background-color: #ffffff;\n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::indicator::checked {\n"
                                    "    visibility:hidden;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.withdraw.setCheckable(True)
        self.withdraw.setChecked(False)
        self.withdraw.setObjectName("withdraw")
        self.buttonGroup.addButton(self.withdraw)
        self.verticalLayout.addWidget(self.withdraw)
        self.deposit = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.deposit.sizePolicy().hasHeightForWidth())
        self.deposit.setSizePolicy(sizePolicy)
        self.deposit.setMinimumSize(QtCore.QSize(220, 50))
        self.deposit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.deposit.setFont(font)
        self.deposit.setStyleSheet("QRadioButton::indicator{\n"
                                   "    width:0;\n"
                                   "    height:0;\n"
                                   "}\n"
                                   "\n"
                                   "QRadioButton::indicator::unchecked {\n"
                                   "    image: url(:/images/radiobutton_unchecked.png);\n"
                                   "}\n"
                                   "\n"
                                   "QRadioButton::checked {\n"
                                   "    background-color: #ffffff;\n"
                                   "}\n"
                                   "\n"
                                   "QRadioButton::indicator::checked {\n"
                                   "    visibility:hidden;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "")
        self.deposit.setCheckable(True)
        self.deposit.setChecked(False)
        self.deposit.setObjectName("deposit")
        self.buttonGroup.addButton(self.deposit)
        self.verticalLayout.addWidget(self.deposit)
        self.newAccount = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.newAccount.sizePolicy().hasHeightForWidth())
        self.newAccount.setSizePolicy(sizePolicy)
        self.newAccount.setMinimumSize(QtCore.QSize(0, 50))
        self.newAccount.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.newAccount.setFont(font)
        self.newAccount.setStyleSheet("QRadioButton::indicator{\n"
                                      "    width:0;\n"
                                      "    height:0;\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator::unchecked {\n"
                                      "    image: url(:/images/radiobutton_unchecked.png);\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::checked {\n"
                                      "    background-color: #ffffff;\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator::checked {\n"
                                      "    visibility:hidden;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "")
        self.newAccount.setCheckable(True)
        self.newAccount.setChecked(False)
        self.newAccount.setObjectName("newAccount")
        self.buttonGroup.addButton(self.newAccount)
        self.verticalLayout.addWidget(self.newAccount)
        self.deleteAccount = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.deleteAccount.sizePolicy().hasHeightForWidth())
        self.deleteAccount.setSizePolicy(sizePolicy)
        self.deleteAccount.setMinimumSize(QtCore.QSize(0, 50))
        self.deleteAccount.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.deleteAccount.setFont(font)
        self.deleteAccount.setStyleSheet("QRadioButton::indicator{\n"
                                         "    width:0;\n"
                                         "    height:0;\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::indicator::unchecked {\n"
                                         "    image: url(:/images/radiobutton_unchecked.png);\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::checked {\n"
                                         "    background-color: #ffffff;\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::indicator::checked {\n"
                                         "    visibility:hidden;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.deleteAccount.setCheckable(True)
        self.deleteAccount.setChecked(False)
        self.deleteAccount.setObjectName("deleteAccount")
        self.buttonGroup.addButton(self.deleteAccount)
        self.verticalLayout.addWidget(self.deleteAccount)
        self.subOp.raise_()
        self.frame.raise_()
        self.info.raise_()
        CustomerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomerWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(CustomerWindow)

    def retranslateUi(self, CustomerWindow):
        _translate = QtCore.QCoreApplication.translate
        CustomerWindow.setWindowTitle(
            _translate("CustomerWindow", "MainWindow"))
        self.cusID.setText(_translate("CustomerWindow", "cusID"))
        self.cusName.setText(_translate("CustomerWindow", "cusName"))
        self.accID.setText(_translate("CustomerWindow", "acc_id"))
        self.accBalance.setText(_translate("CustomerWindow", "balance"))
        self.accCurrency.setText(_translate("CustomerWindow", "currency"))
        self.textEdit_3.setPlaceholderText(_translate(
            "CustomerWindow", "enter amount to withdraw"))
        self.label_8.setText(_translate("CustomerWindow", "from:"))
        self.label_9.setText(_translate("CustomerWindow", "withdraw:"))
        self.comboBox_4.setItemText(0, _translate("CustomerWindow", "acc1"))
        self.comboBox_4.setItemText(1, _translate("CustomerWindow", "acc2"))
        self.label_4.setText(_translate("CustomerWindow", "deposit:"))
        self.label_5.setText(_translate("CustomerWindow", "into:"))
        self.comboBox_3.setItemText(0, _translate("CustomerWindow", "acc1"))
        self.comboBox_3.setItemText(1, _translate("CustomerWindow", "acc2"))
        self.textEdit_2.setPlaceholderText(_translate(
            "CustomerWindow", "enter amount to deposit"))
        self.comboBox_5.setItemText(0, _translate("CustomerWindow", "acc1"))
        self.comboBox_5.setItemText(1, _translate("CustomerWindow", "acc2"))
        self.label_2.setText(_translate(
            "CustomerWindow", "choose acc to delete"))
        self.label.setText(_translate("CustomerWindow", "total:"))
        self.comboBox.setItemText(0, _translate("CustomerWindow", "acc1"))
        self.comboBox.setItemText(1, _translate("CustomerWindow", "acc2"))
        self.label_6.setText(_translate("CustomerWindow", "from"))
        self.label_7.setText(_translate("CustomerWindow", "to"))
        self.comboBox_2.setItemText(0, _translate("CustomerWindow", "acc3"))
        self.comboBox_2.setItemText(1, _translate("CustomerWindow", "acc4"))
        self.textEdit.setPlaceholderText(_translate(
            "CustomerWindow", "enter amount to send"))
        self.radioButton.setText(_translate(
            "CustomerWindow", "901   |   3000  |   TL  "))
        self.radioButton_2.setText(_translate(
            "CustomerWindow", "902  |   3000  |   TL  "))
        self.radioButton_3.setText(_translate(
            "CustomerWindow", "901   |   3000  |   TL  "))
        self.listAccounts.setText(_translate(
            "CustomerWindow", "List Accounts"))
        self.moneyTransfer.setText(_translate(
            "CustomerWindow", "Money Transfer"))
        self.withdraw.setText(_translate("CustomerWindow", "Withdraw"))
        self.deposit.setText(_translate("CustomerWindow", "Deposit"))
        self.newAccount.setText(_translate("CustomerWindow", "Create Account"))
        self.deleteAccount.setText(_translate(
            "CustomerWindow", "Delete Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomerWindow = QtWidgets.QMainWindow()
    ui = Ui_CustomerWindow()
    ui.setupUi(CustomerWindow)
    CustomerWindow.show()
    sys.exit(app.exec_())
