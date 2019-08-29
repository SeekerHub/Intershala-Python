# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wid.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(289, 300)
        self.t2 = QtWidgets.QTextEdit(Form)
        self.t2.setEnabled(True)
        self.t2.setGeometry(QtCore.QRect(100, 30, 181, 31))
        self.t2.setObjectName("t2")
        self.b1 = QtWidgets.QPushButton(Form)
        self.b1.setGeometry(QtCore.QRect(20, 30, 61, 33))
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.additem)
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setGeometry(QtCore.QRect(10, 100, 88, 33))
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.rmitem)
        self.combo1 = QtWidgets.QComboBox(Form)
        self.combo1.setGeometry(QtCore.QRect(110, 100, 111, 33))
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.t2.setPlaceholderText(_translate("Form", "Write your text"))
        self.b1.setText(_translate("Form", "Add"))
        self.b2.setText(_translate("Form", "Remove"))
        self.combo1.setItemText(0, _translate("Form", "C++"))
        self.combo1.setItemText(1, _translate("Form", "Python"))
        self.combo1.setItemText(2, _translate("Form", "Java"))
    def rmitem(self):
        indx=self.combo1.currentIndex()
        item=self.combo1.currentText()
        self.t2.setText(item+" is removed from combobox")
        self.combo1.removeItem(indx)
    def additem(self):
        self.combo1.addItem(self.t1.text())
        self.t2.setText(self.t1.text()+" is added to combobox")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
