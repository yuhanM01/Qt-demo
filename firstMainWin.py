# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 140, 531, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_maxdrawdowns_min = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_maxdrawdowns_min.setObjectName("doubleSpinBox_maxdrawdowns_min")
        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdowns_min, 2, 0, 1, 1)
        self.doubleSpinBox_sharp_min = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_sharp_min.setObjectName("doubleSpinBox_sharp_min")
        self.gridLayout.addWidget(self.doubleSpinBox_sharp_min, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.doubleSpinBox_returns_max = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_returns_max.setObjectName("doubleSpinBox_returns_max")
        self.gridLayout.addWidget(self.doubleSpinBox_returns_max, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.doubleSpinBox_returns_min = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_returns_min.setObjectName("doubleSpinBox_returns_min")
        self.gridLayout.addWidget(self.doubleSpinBox_returns_min, 1, 0, 1, 1)
        self.doubleSpinBox_sharp_max = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_sharp_max.setObjectName("doubleSpinBox_sharp_max")
        self.gridLayout.addWidget(self.doubleSpinBox_sharp_max, 3, 1, 1, 1)
        self.doubleSpinBox_maxdrawdowns_max = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_maxdrawdowns_max.setObjectName("doubleSpinBox_maxdrawdowns_max")
        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdowns_max, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.close_WinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.close_WinBtn.setGeometry(QtCore.QRect(500, 320, 80, 26))
        self.close_WinBtn.setObjectName("close_WinBtn")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(120, 350, 81, 24))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 420, 54, 18))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 410, 113, 26))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_4.setBuddy(self.doubleSpinBox_sharp_min)

        self.retranslateUi(MainWindow)
        self.close_WinBtn.clicked.connect(MainWindow.close)
        self.checkBox.clicked['bool'].connect(self.label_7.setVisible)
        self.checkBox.clicked['bool'].connect(self.lineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.doubleSpinBox_returns_min, self.doubleSpinBox_returns_max)
        MainWindow.setTabOrder(self.doubleSpinBox_returns_max, self.doubleSpinBox_maxdrawdowns_min)
        MainWindow.setTabOrder(self.doubleSpinBox_maxdrawdowns_min, self.doubleSpinBox_maxdrawdowns_max)
        MainWindow.setTabOrder(self.doubleSpinBox_maxdrawdowns_max, self.doubleSpinBox_sharp_min)
        MainWindow.setTabOrder(self.doubleSpinBox_sharp_min, self.doubleSpinBox_sharp_max)
        MainWindow.setTabOrder(self.doubleSpinBox_sharp_max, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "收益"))
        self.label_3.setText(_translate("MainWindow", "最大回撤"))
        self.label_4.setText(_translate("MainWindow", "&sharp比"))
        self.label_5.setText(_translate("MainWindow", "最大值"))
        self.label_2.setText(_translate("MainWindow", "最小值"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.close_WinBtn.setText(_translate("MainWindow", "close"))
        self.checkBox.setText(_translate("MainWindow", "选择"))
        self.label_7.setText(_translate("MainWindow", "显示1"))
        self.lineEdit.setText(_translate("MainWindow", "显示2"))


