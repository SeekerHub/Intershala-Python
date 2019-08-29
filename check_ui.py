# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 373)
        self.t1 = QtWidgets.QTextBrowser(Form)
        self.t1.setGeometry(QtCore.QRect(10, 40, 256, 81))
        self.t1.setObjectName("t1")
        self.cb1 = QtWidgets.QCheckBox(Form)
        self.cb1.setGeometry(QtCore.QRect(30, 150, 98, 23))
        self.cb1.setCheckable(True)
        self.cb1.setObjectName("cb1")
        self.cb2 = QtWidgets.QCheckBox(Form)
        self.cb2.setGeometry(QtCore.QRect(150, 150, 98, 23))
        self.cb2.setCheckable(True)
        self.cb2.setChecked(False)
        self.cb2.setObjectName("cb2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cb1.setText(_translate("Form", "cb1"))
        self.cb2.setText(_translate("Form", "cb2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
