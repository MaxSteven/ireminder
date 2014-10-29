# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message_ui.ui'
#
# Created: Tue Oct 28 18:47:33 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(366, 141)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.message_result = QtGui.QTextBrowser(Form)
        self.message_result.setObjectName(_fromUtf8("message_result"))
        self.horizontalLayout_2.addWidget(self.message_result)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.close_result_window = QtGui.QPushButton(Form)
        self.close_result_window.setMinimumSize(QtCore.QSize(100, 100))
        self.close_result_window.setMaximumSize(QtCore.QSize(100, 100))
        self.close_result_window.setStyleSheet(_fromUtf8("border-style: hidden;"))
        self.close_result_window.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/timeisup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_result_window.setIcon(icon)
        self.close_result_window.setIconSize(QtCore.QSize(100, 100))
        self.close_result_window.setObjectName(_fromUtf8("close_result_window"))
        self.horizontalLayout_2.addWidget(self.close_result_window)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Time\'s Up", None))

from icons import resource
