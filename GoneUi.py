# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GoneUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GoneUi(object):
    def setupUi(self, GoneUi):
        GoneUi.setObjectName("GoneUi")
        GoneUi.resize(822, 653)
        self.centralwidget = QtWidgets.QWidget(GoneUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 811, 631))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Vraj Raj/OneDrive/Desktop/gone/Siri.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 590, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton.setStyleSheet("background-color:rgb(0, 85, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 590, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("background-color:rgb(170, 0, 0)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 201, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Vraj Raj/OneDrive/Desktop/gone/Initiate.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 460, 256, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(420, 460, 256, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        GoneUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(GoneUi)
        QtCore.QMetaObject.connectSlotsByName(GoneUi)

    def retranslateUi(self, GoneUi):
        _translate = QtCore.QCoreApplication.translate
        GoneUi.setWindowTitle(_translate("GoneUi", "MainWindow"))
        self.pushButton.setText(_translate("GoneUi", "Run"))
        self.pushButton_2.setText(_translate("GoneUi", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GoneUi = QtWidgets.QMainWindow()
    ui = Ui_GoneUi()
    ui.setupUi(GoneUi)
    GoneUi.show()
    sys.exit(app.exec_())
