# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\29393\Desktop\py项目\mini.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class main3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(342, 84)
        Form.setMaximumSize(QtCore.QSize(342, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(273, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        # ???? ?????????????? 
        # ?????Raised?Sunken?Plain???????????
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        # ??????
        self.label.setLineWidth(5)
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", ""))
        self.pushButton.setIcon(QIcon("image/search.png"))

