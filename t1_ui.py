# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 60, 160, 113))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b1.setObjectName("b1")

        self.b1.clicked.connect(self.chkbtn)
        self.b1.clicked.connect(self.btnstate)
        self.verticalLayout.addWidget(self.b1)
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b2.setObjectName("b2")
        self.verticalLayout.addWidget(self.b2)
        self.b2.clicked.connect(lambda:self.chkbtn(self.b2))
        self.b2.clicked.connect(self.chkbtn)
        self.b2.clicked.connect(self.btnstate)
        self.b3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(lambda:self.chkbtn(self.b3))
        self.b3.clicked.connect(self.chkbtn)
        self.b1.clicked.connect(self.btnstate)
        self.verticalLayout.addWidget(self.b3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "Button 1"))
        self.b2.setText(_translate("Form", "Button 2"))
        self.b3.setText(_translate("Form", "Button 3"))

    def chkbtn(self,b):
        print ("caption of pressed button :", b.text())

    def btnstate(self):
        if self.b1.isChecked():
             self.b1.setText("pressed")
        else:
             self.b1.setText("released")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
