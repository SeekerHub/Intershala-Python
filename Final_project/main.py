import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import sqlite3 as db
import score
from Evaluate import Ui_Evaluate

con = db.connect('Info.db')
curs = con.cursor()

sqlc = 'SELECT Player FROM Match'
curs.execute(sqlc)
r= curs.fetchall()
i = 0
play = []
while(i!=len(r)):
    play.append(r[i][0])
    i+=1
styel = ['BAT','BWL','WK','AR']
bowl =[]
bat = []
ar = []
wk = []
for j in styel:
    # print(j)
    sql2 = 'SELECT player from Stats WHERE ctg=\'{}\''.format(j)
    curs.execute(sql2)
    r = curs.fetchall()

    if (j=='BWL'):
        i = 0
        bowl = []
        while(i!=len(r)):
            bowl.append(r[i][0])
            i+=1
    elif(j=='BAT'):
        i=0
        while(i!=len(r)):
            bat.append(r[i][0])
            i+=1
    elif(j=='WK'):
        i = 0
        while(i!=len(r)):
            wk.append(r[i][0])
            i+=1
    elif(j=='AR'):
        i = 0
        while(i!=len(r)):
            ar.append(r[i][0])
            i+=1
    else:
        print("Error")
datalist = []
ctg = []
req = ['ctg','value']
for p in req:
    sql3 = 'SELECT {} FROM Stats'.format(p)
    curs.execute(sql3)
    r= curs.fetchall()
    i = 0
    while(i!=len(r)):
        if(p=='value'):
            datalist.append(r[i][0])
        else:
            ctg.append(r[i][0])
        i+=1
# print(play)
data_1 = dict(zip(play,ctg))
data_value = dict(zip(play,datalist))
# print(data_value)



class Ui_MainWindow(object):
    def __init__(self, l, h=0):
        self.count = 0
        self.bats = 0
        self.bowls = 0
        self.ars = 0
        self.wks = 0
        self.l = l
        self.h = h


    def openWindow(self):

        itemsTextList =  [str(self.list_2.item(i).text()) for i in range(self.list_2.count())]
        self.window = QtWidgets.QMainWindow()
        self.itemsList = itemsTextList
        self.ui = Ui_Evaluate(self.itemsList)
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 641)
        MainWindow.setMaximumSize(QtCore.QSize(730, 16777215))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(20, 20, 691, 51))
        self.horizontalWidget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));\n"
"border-color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(0, 0, 0, 230));")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_10 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_6.setStyleSheet("font: 75 9pt \"Open Sans\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 260, 691, 281))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.list_1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_1.setFont(font)
        self.list_1.setStyleSheet("border-color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(0, 0, 26, 255));\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.list_1.setObjectName("list_1")
        self.horizontalLayout_3.addWidget(self.list_1)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.list_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_2.setFont(font)
        self.list_2.setStyleSheet("border-color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(0, 0, 26, 255));\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.list_2.setObjectName("list_2")
        self.horizontalLayout_3.addWidget(self.list_2)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(190, 90, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));\n"
"padding: 0px 0px 0px 0px;")
        self.label_14.setObjectName("label_14")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 90, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(540, 90, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));\n"
"padding: 0px 0px 0px 0px;")
        self.label_15.setObjectName("label_15")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(370, 90, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(370, 150, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(540, 150, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.label_16.setObjectName("label_16")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 70, 691, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 210, 691, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 150, 341, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.rb1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb1.setFont(font)
        self.rb1.setStyleSheet("color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_2.addWidget(self.rb1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.rb2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb2.setFont(font)
        self.rb2.setStyleSheet("")
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_2.addWidget(self.rb2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.rb3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb3.setFont(font)
        self.rb3.setStyleSheet("")
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_2.addWidget(self.rb3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.rb4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb4.setFont(font)
        self.rb4.setStyleSheet("")
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_2.addWidget(self.rb4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.rb2.raise_()
        self.rb3.raise_()
        self.rb4.raise_()
        self.rb1.raise_()
        self.pb_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_2.setGeometry(QtCore.QRect(440, 550, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_2.setFont(font)
        self.pb_2.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(42, 169, 0, 230));\n"
"color: rgb(238, 238, 236);")
        self.pb_2.setObjectName("pb_2")
        self.pb_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_1.setGeometry(QtCore.QRect(70, 550, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_1.setFont(font)
        self.pb_1.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(255, 18, 22, 221));\n"
"color: rgb(238, 238, 236);")
        self.pb_1.setObjectName("pb_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 11pt \"Open Sans\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 0, 21, 611))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(710, 0, 31, 601))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 230, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(440, 230, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 25))
        self.menubar.setObjectName("menubar")
        self.menuManage_team = QtWidgets.QMenu(self.menubar)
        self.menuManage_team.setObjectName("menuManage_team")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionNew_Team.setFont(font)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionDelete_Team = QtWidgets.QAction(MainWindow)
        self.actionDelete_Team.setObjectName("actionDelete_Team")
        self.actionClose = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionClose.setFont(font)
        self.actionClose.setObjectName("actionClose")
        self.actionManage_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionManage_Team.setFont(font)
        self.actionManage_Team.setObjectName("actionManage_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionSave_Team.setFont(font)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionOpen_Team.setFont(font)
        self.actionEvaluate_Team.setFont(font)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.menuManage_team.addAction(self.actionNew_Team)
        self.menuManage_team.addAction(self.actionOpen_Team)
        self.menuManage_team.addAction(self.actionEvaluate_Team)

        # self.menuManage_team.addAction(self.actionManage_Team)
        self.menuManage_team.addAction(self.actionSave_Team)
        self.menuManage_team.addSeparator()
        self.menuManage_team.addAction(self.actionClose)
        self.menubar.addAction(self.menuManage_team.menuAction())


        self.actionOpen_Team.triggered.connect(self.openTeam_2)
        # self.actionEvaluate_Team.triggered.connect(self.openTeam)
        self.actionNew_Team.triggered.connect(self.NewTeam)
        self.actionSave_Team.triggered.connect(self.Saveteam)
        self.actionEvaluate_Team.triggered.connect(self.openTeam)



        self.list_1.itemDoubleClicked.connect(self.removelist1)
        self.list_2.itemDoubleClicked.connect(self.removelist2)

        self.rb1.toggled.connect(self.checkstate)
        self.rb2.toggled.connect(self.checkstate)
        self.rb3.toggled.connect(self.checkstate)
        self.rb4.toggled.connect(self.checkstate)
        # self.Saveteam()
        # self.pb_2.clicked.connect(self.openWindow)

        self.pb_2.clicked.connect(self.Saveteam)


        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        self.pb_1.pressed.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600; color:#2e3436;\">Batsman : </span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">0</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600; color:#2e3436;\">Bowler : </span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">0</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">Allrounder :</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#edd400;\">0</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#2e3436;\">Wicket-Keeper:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">0</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">1000</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Points Available : </span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Nil</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Points Used : </span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Team  :</p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nil</p></body></html>"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOWL"))
        self.rb3.setText(_translate("MainWindow", "WK"))
        self.rb4.setText(_translate("MainWindow", "AR"))
        self.pb_2.setText(_translate("MainWindow", "Save Team"))
        self.pb_1.setText(_translate("MainWindow", "EXIT"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#555753;\">Your Selections</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Available Players</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Selected Players</span></p></body></html>"))
        self.menuManage_team.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionDelete_Team.setText(_translate("MainWindow", "Delete Team"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionManage_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))



    def NewTeam(self):
        Dialog2.show()
        self.name = ""
        self.itemsTextList_2 = []
        self.count = 0
        self.bats = 0
        self.bowls = 0
        self.ars = 0
        self.wks = 0
        self.l = 1000
        self.h = 0
        self.label_15.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{}</span></p></body></html>".format(self.h))
        self.label_14.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{}</span></p></body></html>".format(self.l))
        self.label_10.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.bats))
        self.label_9.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.bowls))
        self.label_8.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.ars))
        self.label_7.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.wks))

        Ui_MainWindow(1000)
        self.list_1.clear()
        self.list_2.clear()
        self.list_1.addItems(play)
        # print(self.l)
        self.label_14.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">1000</span></p></body></html>")
        self.label_15.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">0</span></p></body></html>")

    def Saveteam(self):

        con = db.connect('Info.db')
        curs = con.cursor()

        self.name = str(value)
        # print(self.name)
        self.itemsTextList_2 =  [str(self.list_2.item(i).text()) for i in range(self.list_2.count())]
        # print(self.itemsTextList_2[0])
        curs.execute("INSERT INTO Teams (name,player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.name, self.itemsTextList_2[0], self.itemsTextList_2[1], self.itemsTextList_2[2], self.itemsTextList_2[3], self.itemsTextList_2[4], self.itemsTextList_2[5], self.itemsTextList_2[6], self.itemsTextList_2[7], self.itemsTextList_2[8], self.itemsTextList_2[9], self.itemsTextList_2[10]))
        con.commit()
        r1 = curs.execute("SELECT name FROM Teams")
        # print("Work")
        # print(len(r1.fetchall()))

    def removelist1(self, item):
        if(self.count<11):
            c = item.text()
            if(data_1.get(c)=='BAT'):
                n = data_value.get(c)
                self.bats+=1
                self.label_10.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.bats))


                self.list_1.takeItem(self.list_1.row(item))
                self.list_2.addItem(item.text())
                # count+=1
            if(data_1.get(c)=='BWL'):
                n = data_value.get(c)
                self.bowls+=1
                self.label_9.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.bowls))
                self.list_1.takeItem(self.list_1.row(item))
                self.list_2.addItem(item.text())
                # count+=1


            if(data_1.get(c)=='AR'):
                n = data_value.get(c)
                self.ars+=1
                self.label_8.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.ars))
                self.list_1.takeItem(self.list_1.row(item))
                self.list_2.addItem(item.text())
                # count+=1


            if(data_1.get(c)=='WK'):
                n = data_value.get(c)
                self.wks+=1
                if self.wks>1:
                    msg = QMessageBox()
                    msg.setStyleSheet("QLabel{min-width: 200px;}")
                    msg.setIcon(QMessageBox.Critical)
                    # msg.setText("Error")
                    msg.setInformativeText('YOU CAN\'T INSERT MORE THAN ONE WICKETKEEPER')
                    msg.setWindowTitle("Error")

                    self.label_7.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">1</span></p></body></html>")
                    msg.exec_()

                else:
                    self.label_7.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.wks))
                    self.list_1.takeItem(self.list_1.row(item))
                    self.list_2.addItem(item.text())


            k = self.l - n
            if k<0:
                msg = QMessageBox()
                msg.setStyleSheet("QLabel{min-width: 250px;}")
                # msg.setIcon(QMessageBox.Critical)
                # msg.setText("Error")
                msg.setInformativeText('Not Enoght Point Available')
                msg.setWindowTitle("Error")

                self.label_7.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">1</span></p></body></html>")
                msg.exec_()
                # k < 0
                self.label_14.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{}</span></p></body></html>".format(k))
            else:
                self.label_14.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{}</span></p></body></html>".format(self.l))
            self.l = k
            # print(self.h)
            increase = self.h + n
            if increase>1000:
                increase = 0
                self.label_15.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{}</span></p></body></html>".format(increase))
            else:
                self.label_15.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{}</span></p></body></html>".format(increase))
            self.h = increase

            self.count+=1


        else:
            # print("player limit exceeded")
            msg = QMessageBox()
            msg.setStyleSheet("QLabel{min-width: 250px;}")
            # msg.setIcon(QMessageBox.Critical)
            # msg.setText("Error")
            msg.setInformativeText('Player Limit Exceeded')
            msg.setWindowTitle("Error")

            self.label_7.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">1</span></p></body></html>")
            msg.exec_()

    def checkstate(self):
        state1='OFF'
        state2='OFF'
        state3 = 'OFF'
        state4='OFF'
        if self.rb1.isChecked()==True:
            state1='ON'
            self.list_1.clear()
            self.list_1.addItems(bat)

        else:
            state1='OFF'

        if self.rb2.isChecked()==True:
            state2='ON'
            self.list_1.clear()
            self.list_1.addItems(bowl)

        else:
            state2='OFF'

        if self.rb3.isChecked()==True:
            state3='ON'
            self.list_1.clear()
            self.list_1.addItems(wk)

        else:
            state3='OFF'

        if self.rb4.isChecked()==True:
            state4='ON'
            self.list_1.clear()
            self.list_1.addItems(ar)

        else:
            state4='OFF'
        # self.t1.setText("Button1 is {} Button2 is {}".format(state1,state2))




    def removelist2(self, item):

        c = item.text()
        if(data_1.get(c)=='BAT'):
            n = data_value.get(c)
            self.bats-=1
            self.label_10.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.bats))
            self.list_2.takeItem(self.list_2.row(item))
            self.list_1.addItem(item.text())
        if(data_1.get(c)=='BWL'):
            n = data_value.get(c)
            self.bowls-=1
            self.label_9.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.bowls))
            self.list_2.takeItem(self.list_2.row(item))
            self.list_1.addItem(item.text())

        if(data_1.get(c)=='AR'):
            n = data_value.get(c)
            self.ars-=1
            self.label_8.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">{}</span></p></body></html>".format(self.ars))
            self.list_2.takeItem(self.list_2.row(item))
            self.list_1.addItem(item.text())

        if(data_1.get(c)=='WK'):
            n = data_value.get(c)
            self.wks-=1
            if self.wks>1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('YOU CAN\'T INSERT MORE THAN ONE WICKETKEEPER')
                msg.setWindowTitle("Error")

                self.label_7.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">1</span></p></body></html>")
                msg.exec_()
            else:
                self.label_7.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#edd400;\">0</span></p></body></html>")
                self.list_2.takeItem(self.list_2.row(item))
                self.list_1.addItem(item.text())


        k = self.h - n
        self.label_15.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{}</span></p></body></html>".format(k))
        self.h = k
        decrease = self.l + n
        self.label_14.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{}</span></p></body></html>".format(decrease))
        self.l = decrease

    def openTeam_2(self):
        Dialog.show()


    def openTeam(self):
        itemsTextList =  []
        r1 = curs.execute("SELECT name FROM Teams")
        team = r1.fetchall()
        print("This part Begins")
        # n = len(r1.fetchall())
        # print(n)

        # print(r1.fetchall())
        for x in team:
            itemsTextList.append(x[0])

        print(itemsTextList)
        self.window = QtWidgets.QMainWindow()
        self.itemsList = itemsTextList
        self.ui = Ui_Evaluate(self.itemsList)
        self.ui.setupUi(self.window)
        self.window.show()

    def labelText_2(self, MainWindow, value):
        self.name = str(value)
        self.label_16.setText(str(value))
        sql = 'select player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11 from Teams where name = \'{}\''.format(value)
        # print(sql)
        curs.execute(sql)
        r1 = curs.fetchall()
        # print(r1)
        for x in r1[0]:
            print(x)
            self.list_2.addItem(x)

    def labelText(self, MainWindow, value):
        self.team_available = []
        self.name = str(value)
        r1 = curs.execute("SELECT name FROM Teams")
        team = r1.fetchall()
        # print(team)

        for x in team:
            self.team_available.append(x[0])


        if self.name in self.team_available:
            msg = QMessageBox()
            msg.setStyleSheet("QLabel{min-width: 150px;}")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Team name Exist , Try some another name')
            msg.setWindowTitle("Error")
            msg.exec_()
            Dialog2.show()
        else:
            self.label_16.setText(str(value))

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):

        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(369, 160)
        Dialog2.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(0, 191, 183, 221));")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 110, 91, 33))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));\n"
"background-color: rgb(186, 189, 182);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(70, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 70, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_2.clicked.connect(self.CloseAndRefresh_2)

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog2"))
        self.pushButton_2.setText(_translate("Dialog2", "OK"))
        self.label.setText(_translate("Dialog2", "<html><head/><body><p align=\"center\"><span style=\" color:#eeeeec;\">Enter Team Name</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog2", "Enter here"))

    def CloseAndRefresh_2(self):
        # print("Working")
        global value
        value = self.lineEdit.text()
        # print(value)
        ui.labelText(MainWindow, value)
        Dialog2.close()




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.teamlist = []
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 198)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(0, 191, 183, 221));")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 231, 51))

        r1 = curs.execute("SELECT name FROM Teams")
        team = r1.fetchall()
        print(team)
        for x in team:
            print(x)
            self.teamlist.append(x[0])
        print(self.teamlist)

        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(80, 80, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));\n"
"background-color: rgb(186, 189, 182);")
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItems(self.teamlist)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 140, 91, 33))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.983, y2:1, stop:0 rgba(255, 255, 255, 255));\n"
"background-color: rgb(186, 189, 182);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.CloseAndRefresh)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#eeeeec;\">Choose Your Team </span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def CloseAndRefresh(self):
        global value_2
        value_2 = self.comboBox.currentText()
        # print(value)
        ui.labelText_2(MainWindow, value_2)
        Dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(1000)
    ui.setupUi(MainWindow)
    MainWindow.show()

    Dialog2 = QtWidgets.QDialog()
    dia_2 = Ui_Dialog2()
    dia_2.setupUi(Dialog2)

    Dialog = QtWidgets.QDialog()
    dia = Ui_Dialog()
    dia.setupUi(Dialog)

    sys.exit(app.exec_())
