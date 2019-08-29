# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(314, 253)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list1 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.list1.setObjectName("list1")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.list1.addItem(item)
        self.horizontalLayout.addWidget(self.list1)


        self.list1.itemDoubleClicked.connect(self.removelist1)



        self.list2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.list2.setObjectName("list2")


        self.list2.itemDoubleClicked.connect(self.removelist2)


        self.horizontalLayout.addWidget(self.list2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 220, 131, 19))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 220, 121, 19))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.list1.isSortingEnabled()
        self.list1.setSortingEnabled(False)
        item = self.list1.item(0)
        item.setText(_translate("Form", "Kohli"))
        item = self.list1.item(1)
        item.setText(_translate("Form", "Dhoni"))
        item = self.list1.item(2)
        item.setText(_translate("Form", "Gandhi"))
        item = self.list1.item(3)
        item.setText(_translate("Form", "Rahane"))
        item = self.list1.item(4)
        item.setText(_translate("Form", "Jadu"))
        item = self.list1.item(5)
        item.setText(_translate("Form", "Pant"))
        self.list1.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "Avalable Players"))
        self.label_2.setText(_translate("Form", "Selected"))

    def removelist1(self, item):
        self.list1.takeItem(self.list1.row(item))
        self.list2.addItem(item.text())

    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        self.list1.addItem(item.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
