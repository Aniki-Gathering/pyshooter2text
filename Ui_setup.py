#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'c:\Users\29393\Desktop\py项目\setup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup


class main2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(526, 439)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 400, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 90, 81, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.imshow = QtWidgets.QLabel(Form)
        self.imshow.setGeometry(QtCore.QRect(190, 80, 301, 301))
        self.imshow.setObjectName("graphicsView")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(300, 40, 191, 31))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 91, 81))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 171, 21))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(20, 200, 115, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 230, 115, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        self.Box_1 = QButtonGroup(self)
        self.Box_2 = QButtonGroup(self)
        self.Box_1.addButton(self.radioButton)
        self.Box_1.addButton(self.radioButton_2)
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 171, 16))
        self.label_4.setObjectName("label_4")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 320, 115, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 350, 115, 20))
        self.radioButton_4.setObjectName("radioButton_4")

        self.Box_2.addButton(self.radioButton_3)
        self.Box_2.addButton(self.radioButton_4)

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 50, 81, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 50, 72, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 100, 72, 21))
        self.label_6.setObjectName("label_6")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.imshow.setFrameShape(QtWidgets.QFrame.Box)
        # 设置阴影 只有加了这步才能设置边框颜色 
        # 可选样式有Raised、Sunken、Plain（这个无法设置颜色）等
        self.imshow.setFrameShadow(QtWidgets.QFrame.Raised)
        # 设置线条宽度
        self.imshow.setLineWidth(5)
        # 设置背景颜色，包括边框颜色
        #self.imshow.setStyleSheet('background-color: rgb(255, 0, 0)')

        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "应用"))
        self.label.setText(_translate("Form", "快捷键"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.label_2.setText(_translate("Form", "皮肤选择"))
        self.comboBox.setItemText(0, _translate("MainWindow", "cold"))
        self.comboBox.setItemText(1, _translate("MainWindow", "enthusiasm"))
        self.comboBox.setItemText(2, _translate("MainWindow", "nature"))
        self.comboBox.setItemText(3, _translate("MainWindow", "mystery"))
        self.label_3.setText(_translate("Form", "窗口关闭时最小化到托盘"))
        self.radioButton.setText(_translate("Form", "是"))
        self.radioButton_2.setText(_translate("Form", "否"))
        self.label_4.setText(_translate("Form", "启动时弹出功能介绍"))
        self.radioButton_3.setText(_translate("Form", "是"))
        self.radioButton_4.setText(_translate("Form", "否"))
        self.label_5.setText(_translate("Form", "MINI模式"))
        self.label_6.setText(_translate("Form", "快速截屏"))
