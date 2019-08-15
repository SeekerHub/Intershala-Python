# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finder2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(430, 20, 88, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setStyleSheet("")
        self.b1.setObjectName("b1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 80, 204, 17))
        # self.label_5.setInputMask("")
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Lol = QtWidgets.QFrame(self.centralwidget)
        self.Lol.setGeometry(QtCore.QRect(30, 110, 461, 41))
        self.Lol.setFrameShape(QtWidgets.QFrame.HLine)
        self.Lol.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Lol.setObjectName("Lol")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(420, 150, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setStyleSheet("")
        self.b2.setObjectName("b2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(160, 20, 251, 33))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setBold(True)
        font.setWeight(75)
        self.line1.setFont(font)
        self.line1.setInputMask("")
        self.line1.setObjectName("line1")
        self.line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(160, 160, 211, 33))
        self.line_2.setInputMask("")
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.line_2.setValidator(QtGui.QIntValidator())
        self.b1.clicked.connect(self.findd)
        self.b2.clicked.connect(self.total)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Book Title :  "))
        self.b1.setText(_translate("MainWindow", "Find Price"))
        self.label_2.setText(_translate("MainWindow", "Price     :"))
        self.label_5.setText(_translate("MainWindow", "Rs. "))
        self.label_3.setText(_translate("MainWindow", "Quantity  :"))
        self.b2.setText(_translate("MainWindow", " Total"))
        self.label_4.setText(_translate("MainWindow", "Total     : "))
        self.label_6.setText(_translate("MainWindow", "Rs. "))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


    def findd(self):
        text = self.line1.text()
        bok = sqlite3.connect('Books.db')
        curs = bok.cursor()
        sqlc = 'select * from Books where title = \'{}\';'.format(text)
        curs.execute(sqlc)
        r= curs.fetchone()
        print(r)
        if r==None:
            print('Sorry! Book is not available at the moment')
            self.label_5.setText("Not Available")

            # break
        else:
            self.label_5.setText(str(r[3]))
            self.b2.clicked.connect(self.total)


    def total(self):
        # print(total)
        m = self.label_5.text()
        k = self.line_2.text()
        k = int(k)
        j = float(m)
        tot = k*j
        print(tot)
        # print(tot)

        self.label_6.setText("Rs. {}".format(tot))



        # # qty  = int(input('Enter the Quantity:\t'))
        # sqlc = 'select price from Books where title = \'{}\';'.format(name)
        # # print(sqlc)
        # curs = bok.cursor()
        # # curs.execute('''SELECT * FROM Books WHERE title= '''+ str(name) +''';''' )
        # curs.execute(sqlc)
        # found = 1
        # while found!=0:
        #     record = curs.fetchone()
        #
        #     if record==None:
        #         # print('Sorry! Book is not available at the moment')
        #         found+=1
        #         break
        #     print('Total price to be paid :',  record[0]*qty)
        #     found=0
        #
        # if found!=0 :
        #     print('Sorry! Book is not available at the moment')
        # print('\n')
        #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
