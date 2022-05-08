import sys
from unicodedata import name
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from matplotlib.widgets import Widget

from test import test

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = test()
        self.ui.setupUi(self.main_win)

        self.ui.addButton.clicked.connect(self.addComponent)
        self.ui.removeButton.clicked.connect(self.removeComponent)
        self.widgetCount = 1

    def show(self):
        self.main_win.show()

    def addComponent(self, row):
        self.widgetCount += 1
        self.widget = QtWidgets.QWidget(self.ui.mainFrame)
        newWidget = self.widget
        newWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        newWidget.setStyleSheet(u"background-color:#888888;")
        newWidget.setObjectName("widget" + str(self.widgetCount))
        self.horizontalLayout = QtWidgets.QHBoxLayout(newWidget)
        self.horizontalLayout.setObjectName("horizontalLayout"+str(self.widgetCount))
        newLabel = QtWidgets.QLabel(newWidget)
        newLabel.setText("new label")
        newLabel.setObjectName("label" + str(self.widgetCount))
        self.horizontalLayout.addWidget(newLabel)
        self.ui.verticalLayout.addWidget(newWidget,row)
    
    def removeComponent(self):
        if self.widgetCount == 1:
            lastWidget = self.ui.mainFrame.findChild(QWidget,"widget")
            if lastWidget:
                self.ui.mainFrame.findChild(QWidget,"widget").deleteLater()
            return
        self.ui.mainFrame.findChild(QWidget,"widget" + str(self.widgetCount)).deleteLater()
        self.widgetCount -= 1
        print(self.widgetCount)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
